from enum import Enum
from pydantic import BaseModel, Field

class LengthClass(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class LameLevel(str, Enum):
    DECENT = "decent"       # 1
    MODERATE = "moderate"   # 2
    HIGH = "high"           # 3

class JokeRequest(BaseModel):
    length_class: LengthClass
    lame_level: LameLevel

class JokeResponse(BaseModel):
    text: str
    length_class: LengthClass
    lame_level: LameLevel

