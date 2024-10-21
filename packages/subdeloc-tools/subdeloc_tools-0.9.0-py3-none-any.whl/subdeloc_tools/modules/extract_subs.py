from .merger import Merger

merger = Merger()

def get_index(file: str, language: str="eng") -> int:
	try:
		streams = merger.get_streams()
		index = merger.get_language_index(language)

		return index
	except Exception as e:
		print(e)
		return -1

def extract_sub(f: str, index: int) -> str:
	subfile = False
	if index > -1:
		if merger.codec_name == "ass":
			outputf = "subfile.ass"
		elif merger.codec_name == "subrip":
			outputf = "subfile.srt"
		else:
			raise Exception("Subtitle codec not recognized")
			
		subfile = merger.demux(f, index, outputf)
	return subfile

def extract_subs_by_lang(f:str, lang:str="eng") -> bool:
	try:
		merger.set_file(f)
		index = get_index(f, lang)

		subfile = extract_sub(f, index)
		if subfile:
			print("Subfile:", subfile)
			return True
		return False
	except Exception as e:
		print(e)
		return False

def extract_subs_by_index(f:str, index:int) -> bool:
	try:
		res = extract_sub(f, index)
		if res:
			print("Subfile:", subfile)
			return True
		return False
	except Exception as e:
		print(e)
		return False