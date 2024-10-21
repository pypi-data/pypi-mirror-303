from typing import List, Dict, TypedDict

# FFMPEG
StreamsVar = List[dict]

# Pair
class IntervalVar(TypedDict):
	start: int
	end: int
	text: str
	nl: int

class MatchesVar(TypedDict):
	start: int
	end: int
	original: List[IntervalVar]
	reference: List[IntervalVar]

SubtitleSetVar = List[IntervalVar]