# Table of Contents

* [src/drivecatplus/run\_dcp](#src/drivecatplus/run_dcp)
  * [get\_drivestats](#src/drivecatplus/run_dcp.get_drivestats)
  * [run\_dcp](#src/drivecatplus/run_dcp.run_dcp)

<a id="src/drivecatplus/run_dcp"></a>

# src/drivecatplus/run\_dcp

<a id="src/drivecatplus/run_dcp.get_drivestats"></a>

#### get\_drivestats

```python
def get_drivestats(filepath: str | Path, name_dict: dict) -> dict
```

This function creates a Cycle object for a given filepath to a drivecycle, runs DriveStats, and returns a stats dictionary

**Arguments**:

* `filepath` _str | Path_ - filepath of input drivecycle
* `name_dict` _dict_ - Dictionary containing column names for speed_mps, time_s, and elevation_m

**Returns**:

* `dict` - Dictionary containing DriveStats result

<a id="src/drivecatplus/run_dcp.run_dcp"></a>

#### run\_dcp

```python
def run_dcp(cycle_paths: List[str | Path], name_dict: dict,
            results_path: str | Path)
```

_summary_

**Arguments**:

* `cycle_paths` _List[str|Path]_ - List of filepaths of input drivecycles
* `name_dict` _dict_ - Dictionary containing column names for speed_mps, time_s, and elevation_m
* `results_path` _str | Path_ - Output filepath of DriveCAT+ results CSV
