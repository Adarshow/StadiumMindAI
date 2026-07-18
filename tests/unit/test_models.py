import pytest
from pydantic import ValidationError
from src.domain.models import StadiumContext

def test_stadium_context_valid_payload():
    context = StadiumContext(
        timestamp="14:00 PM",
        active_events=["Event A"],
        weather="Sunny",
        attendance=65000,
        metrics={"density": 0.9}
    )
    assert context.attendance == 65000

def test_stadium_context_rejects_negative_attendance():
    with pytest.raises(ValidationError):
        StadiumContext(
            timestamp="14:00 PM",
            active_events=[],
            weather="Sunny",
            attendance=-500, # Invalid
            metrics={}
        )

def test_stadium_context_rejects_over_capacity_attendance():
    with pytest.raises(ValidationError):
        StadiumContext(
            timestamp="14:00 PM",
            active_events=[],
            weather="Sunny",
            attendance=300000, # Invalid
            metrics={}
        )

def test_stadium_context_rejects_long_strings():
    with pytest.raises(ValidationError):
        StadiumContext(
            timestamp="14:00 PM" * 50, # Invalid length
            active_events=[],
            weather="Sunny",
            attendance=65000,
            metrics={}
        )
