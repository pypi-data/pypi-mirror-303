import argparse
import json
from time import gmtime, strftime
from typing import List
import pandas as pd
from drivecatplus import drivestats, Global
from drivecatplus.drivestats import Cycle, DriveStats
from pathlib import Path


def get_drivestats(
    filepath: str | Path,
    name_dict: dict,
) -> dict:
    """This function creates a Cycle object for a given filepath to a drivecycle, runs DriveStats, and returns a stats dictionary

    Args:
        filepath (str | Path): filepath of input drivecycle
        name_dict (dict): Dictionary containing column names for speed_mps, time_s, and elevation_m

    Returns:
        dict: Dictionary containing DriveStats result
    """
    cycle = Cycle.from_file(
        filepath=filepath,
        var_name_dict=name_dict,
    )
    return DriveStats(cycle).to_dict(units_system="SI", include_prefix=False)


def run_dcp(cycle_paths: List[str | Path], name_dict: dict, results_path: str | Path):
    """_summary_

    Args:
        cycle_paths (List[str|Path]): List of filepaths of input drivecycles
        name_dict (dict):  Dictionary containing column names for speed_mps, time_s, and elevation_m
        results_path (str | Path): Output filepath of DriveCAT+ results CSV
    """
    reports = []
    for i, filepath in enumerate(cycle_paths):
        print(f"Running cycle: {filepath}")
        drivestats_dict = {"index": i, "filepath": filepath}
        drivestats_dict.update(get_drivestats(filepath, name_dict))
        reports.append(drivestats_dict)

    reports_df = pd.DataFrame(reports)
    reports_df.to_csv(results_path, index=False)
    print(f"DriveCAT+ Results: {results_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog="RUN_DCP",
        description="""The run_faqs.py module is the main script to run DCP""",
    )
    parser.add_argument(
        "--input-path",
        default=Path(__file__).parents[1] / "resources" / "cycles.json",
        type=str,
        help='filepath of one input drivecycle or directory containing multiple drivecycles or a JSON filepath containing drivecycle filepaths. Example: \{"cycles":["path/to/drivecycle1","path/to/drivecycle2"] \}',
    )
    parser.add_argument(
        "--name-dict",
        default=Path(__file__).parents[1] / "resources" / "name_dict.json",
        type=str,
        help='str: json filepath containing drivecycle filepaths. Example: \{"speed_mps":"<speed-col>","time_s":"<time-col>"\}',
    )
    parser.add_argument(
        "--dst-dir",
        help="destination directory to store results",
        type=str,
        default=Path(__file__).parents[2] / "results",
    )
    parser.add_argument(
        "--res-suffix",
        type=str,
        help="Suffix for results file",
        default="",
    )
    args = parser.parse_args()

    ts = strftime(
        "%Y-%m-%d_%H-%M-%S",
    )
    if not Path(args.dst_dir).exists():
        Path(args.dst_dir).mkdir(parents=True, exist_ok=True)

    if args.res_suffix:
        results_path = Path(args.dst_dir) / f"drivestats_{ts}_{args.res_suffix}.csv"
    else:
        results_path = Path(args.dst_dir) / f"drivestats_{ts}.csv"

    input_path = Path(args.input_path)
    if input_path.is_dir():
        cycle_paths = [p for p in input_path.rglob("*.csv")]
    elif input_path.suffix in [".JSON", ".json"]:
        with open(input_path, "r") as f:
            cycle_paths_dict = json.load(f)
        cycle_paths = cycle_paths_dict["cycles"]

    with open(args.name_dict, "r") as f:
        name_dict = json.load(f)
    run_dcp(cycle_paths, name_dict=name_dict, results_path=results_path)
