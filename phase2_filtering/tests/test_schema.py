import pytest
from pydantic import ValidationError
from phase2_filtering.schema import JokeRequest, LengthClass, LameLevel

def test_valid_request():
    req = JokeRequest(length_class="short", lame_level="decent")
    assert req.length_class == LengthClass.SHORT
    assert req.lame_level == LameLevel.DECENT

def test_invalid_length():
    with pytest.raises(ValidationError):
        JokeRequest(length_class="extra-long", lame_level="moderate")

def test_invalid_lame_level():
    with pytest.raises(ValidationError):
        JokeRequest(length_class="short", lame_level="super-lame")
