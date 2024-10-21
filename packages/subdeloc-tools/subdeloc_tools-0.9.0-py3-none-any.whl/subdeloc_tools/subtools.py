import json
import re
import os.path
import sys
import pkg_resources
from typing import Dict, Union, List, Tuple, Set

from subdeloc_tools.modules import extract_subs
from subdeloc_tools.modules import pairsubs
from subdeloc_tools.modules import honorific_fixer
from subdeloc_tools.modules.types.types import MatchesVar
from modify_subs import find_key_by_string_wrapper as find_key_by_string

HONORIFICS_PATH = pkg_resources.resource_filename('subdeloc_tools', 'samples/honorifics.json')

class SubTools:
	honorifics = {}
	names = {}

	def __init__(self, main_sub: str, ref_sub: str, names_path: str, honorifics_name: str=HONORIFICS_PATH, output_name: str="edited.ass", load_from_lambda: bool=False, jap_ref: bool=True):
		"""
		If load_from_lambda is True, names_path and honorifics_name should be the address to a public HTTP lambda. TODO
		"""
		self.main_sub = main_sub
		self.ref_sub = ref_sub
		self.output_name = output_name
		self.jap_ref = jap_ref
		with open(honorifics_name, encoding='utf-8') as f:
			self.honorifics = json.load(f)
		with open(names_path, encoding='utf-8') as f:
			self.names = json.load(f)

	def print_to_file(self, data: dict, filename: str="result.json"):
		"""Writes the data to a JSON file."""
		with open(filename, "w", encoding="utf8") as output:
			json.dump(data, output, ensure_ascii=False, indent=2)

	def main(self) -> str:
		# Assuming pairsubs.pair_files is defined elsewhere and returns a list of subtitles
		res = pairsubs.pair_files(self.main_sub, self.ref_sub)
		s = self.search_honorifics(res)
		return honorific_fixer.fix_original(self.main_sub, s, self.output_name)


	def prepare_honor_array(self) -> List[str]:
		"""Prepares an array of all kanjis from the honorifics."""
		return [kanji for h in self.honorifics["honorifics"].values() for kanji in h["kanjis"]]

	def prepare_tokens_array(self) -> Set[str]:
		return set(self.names.keys())

	def find_exact_name_in_string(self, name, string):
		pattern = r"\b" + re.escape(name) + r"\b"
		return bool(re.search(pattern, string, flags=re.I))

	def check_tokens(self, text, tokens):
		for i in tokens:
			if self.find_exact_name_in_string(i, text):
				return True
		return False

	def search_tokens(self, text, tokens):
		for i in text.split(" "):
			if self.check_tokens(i, tokens):
				yield i

	def search_honorifics(self, subs: List[MatchesVar]) -> List[MatchesVar]:
		"""Searches for honorifics in the subtitles and processes them."""
		if self.jap_ref:
			print("Searching honorifics")
			honor = self.prepare_honor_array()

			for sub in subs:
				for reference in sub["reference"]:
					for h in honor:
						if h in reference["text"]:
							self.check_sub(sub, h, reference["text"])
							break  # Exit loop after first match to avoid redundant checks
		else:
			print("Searching tokens")
			tokens = self.prepare_tokens_array()

			for sub in subs:
				for reference in sub["reference"]:
					for word in self.search_tokens(reference["text"], tokens):
						if "-" in word:
							self.fix_sub(sub, word)

		return subs

	def check_sub(self, sub:MatchesVar, honor:str, reference_text:str) -> bool:
		"""Checks and replaces honorifics in the subtitles."""
		honorific = find_key_by_string(self.honorifics, honor, "kanjis")

		if not honorific:
			return False

		for name, name_value in self.names.items():
			if name_value in reference_text:
				for orig in sub["original"]:
					if name in orig["text"]:
						# Perform replacements for name and honorifics
						orig["text"] = re.sub(name, f"{name}-{honorific}", orig["text"], flags=re.I)
						
						for alternative in self.honorifics["honorifics"][honorific]["alternatives"]:
							orig["text"] = re.sub(alternative, "", orig["text"], flags=re.I)

						orig["text"] = orig["text"].strip()
		return True

	def clean_left(self, word):
		r = ""
		for i in word[::-1]:
			if i.isalpha():
				r += i
			else:
				break

		return r[::-1]

	def clean_right(self, word):
		r = ""
		for i in word:
			if i.isalpha():
				r += i
			else:
				break

		return r

	def replace_word(self, k,v, text):
		return re.sub(k, v, text, flags=re.I)

	def replace_english_honorifics(self, text, honorific=""):
		for alternative in self.honorifics["honorifics"][honorific]["alternatives"]:
			text = re.sub(alternative, "", text, flags=re.I)

		return text

	def fix_sub(self, sub:MatchesVar, word:str) -> bool:
		name = self.clean_left(word.split("-")[-2])
		honorific = self.clean_right(word.split("-")[-1])

		new_word = name+"-"+honorific

		for orig in sub["original"]:
			if not new_word in orig["text"]:
				orig["text"] = self.replace_word(name, new_word, orig["text"])
				orig["text"] = self.replace_english_honorifics(orig["text"], honorific)

				orig["text"] = orig["text"].strip()

		return True


	@classmethod
	def get_default_honorifics_file(self):
		with open(HONORIFICS_PATH, encoding='utf-8') as f:
			return json.load(f)