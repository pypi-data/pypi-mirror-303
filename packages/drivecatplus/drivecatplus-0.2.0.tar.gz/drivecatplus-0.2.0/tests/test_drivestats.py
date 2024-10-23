from __future__ import annotations

from drivecatplus.drivestats import DriveStats, Cycle
from pathlib import Path


def test_intialize_cycle():
    cycle = Cycle(
        time_s=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        speed_mps=[0, 1, 2, 3, 4, 5, 4, 3, 2, 0],
        elevation_m=[0, 0, 0, 0, 0, 0, 0, 0, 0],
    )
    assert cycle.time_s == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and cycle.speed_mps == [0, 1, 2, 3, 4, 5, 4, 3, 2, 0]


def test_check_cycle_length():
    cycle = Cycle(
        time_s=range(0, 10), speed_mps=[0, 1, 2, 3, 4, 5, 4, 3, 2, 0], elevation_m=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    )
    assert len(cycle.time_s) == len(cycle.speed_mps) == len(cycle.elevation_m)


def test_create_cycle_from_file():
    cycle_file = Path(__file__).parents[1] / "src/resources/demo_cycle_without_elevation.csv"
    cycle = Cycle.from_file(cycle_file)
    assert isinstance(cycle, Cycle)


def test_create_cycle_from_dict():
    cycle_dict = {
        "time_s": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "speed_mps": [0, 1, 2, 3, 4, 5, 4, 3, 2, 0],
        "elevation_m": [0, 0, 0, 0, 0, 0, 0, 0, 0],
    }

    cycle = Cycle.from_dict(cycle_dict)
    assert isinstance(cycle, Cycle)
