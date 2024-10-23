# Table of Contents

* [src/drivecatplus/drivestats](#src/drivecatplus/drivestats)
  * [Cycle](#src/drivecatplus/drivestats.Cycle)
    * [from\_file](#src/drivecatplus/drivestats.Cycle.from_file)
    * [from\_dict](#src/drivecatplus/drivestats.Cycle.from_dict)
    * [generate\_stats](#src/drivecatplus/drivestats.Cycle.generate_stats)
    * [add\_acceleration](#src/drivecatplus/drivestats.Cycle.add_acceleration)
  * [DriveStats](#src/drivecatplus/drivestats.DriveStats)
    * [\_\_new\_\_](#src/drivecatplus/drivestats.DriveStats.__new__)
    * [\_\_init\_\_](#src/drivecatplus/drivestats.DriveStats.__init__)
    * [to\_dict](#src/drivecatplus/drivestats.DriveStats.to_dict)
    * [export\_to\_file](#src/drivecatplus/drivestats.DriveStats.export_to_file)
    * [\_TimeStats](#src/drivecatplus/drivestats.DriveStats._TimeStats)
    * [\_SamplingStats](#src/drivecatplus/drivestats.DriveStats._SamplingStats)
    * [\_TotalSpeedStats](#src/drivecatplus/drivestats.DriveStats._TotalSpeedStats)
    * [\_DrivingSpeedStats](#src/drivecatplus/drivestats.DriveStats._DrivingSpeedStats)
    * [\_SpeedCountingStats](#src/drivecatplus/drivestats.DriveStats._SpeedCountingStats)
    * [\_DistanceCountingStats](#src/drivecatplus/drivestats.DriveStats._DistanceCountingStats)
    * [\_AccelerationStats](#src/drivecatplus/drivestats.DriveStats._AccelerationStats)
    * [\_StopsCountingStats](#src/drivecatplus/drivestats.DriveStats._StopsCountingStats)
    * [\_ElevationStats](#src/drivecatplus/drivestats.DriveStats._ElevationStats)
    * [\_PowerDensityStats](#src/drivecatplus/drivestats.DriveStats._PowerDensityStats)
    * [\_EnergyDensityStats](#src/drivecatplus/drivestats.DriveStats._EnergyDensityStats)
    * [\_KineticIntensityStats](#src/drivecatplus/drivestats.DriveStats._KineticIntensityStats)
    * [\_DistanceStats](#src/drivecatplus/drivestats.DriveStats._DistanceStats)

<a id="src/drivecatplus/drivestats"></a>

# src/drivecatplus/drivestats

DriveStats/SpeedCalcs

<a id="src/drivecatplus/drivestats.Cycle"></a>

## Cycle Objects

```python
@dataclass
class Cycle(object)
```

This class is used to initialize and manipulate an input drivecycle. The three main aspects of a drivecycle are Time, Speed, and Elevation (wherever applicable).

<a id="src/drivecatplus/drivestats.Cycle.from_file"></a>

#### from\_file

```python
@classmethod
def from_file(
    cls,
    filepath: str | Path,
    var_name_dict: dict = {
        "speed_mps": "speed_mps",
        "time_s": "time_s"
    }) -> Self
```

This method is used to initialize a Cycle object from a CSV file.

**Arguments**:

- `filepath` _str | Path_ - Filepath of the input drivecycle CSV file
- `var_name_dict` _dict, optional_ - Dictionary containing column names for 'speed_mps', 'time_s', and 'elevation_m'. Defaults to {"speed_mps": "speed_mps", "time_s": "time_s"}.
  

**Returns**:

- `Self` - Cycle object

<a id="src/drivecatplus/drivestats.Cycle.from_dict"></a>

#### from\_dict

```python
@classmethod
def from_dict(cls, cycle_dict: dict) -> Self
```

This method is used to initialize a Cycle object using a dictionary of arrays/lists of Time, Speed, and Elevation traces.

**Arguments**:

- `cycle_dict` _dict_ - Dictionary containing lists of equal length of Time, Speed, and Elevation
  

**Returns**:

- `Self` - Cycle object instance

<a id="src/drivecatplus/drivestats.Cycle.generate_stats"></a>

#### generate\_stats

```python
@classmethod
def generate_stats(units: str = "SI")
```

This method is used to calculate all DriveStats.

**Arguments**:

- `units` _str, optional_ - Units system desired between ['SI', 'Imperial']. Defaults to "SI".
  

**Returns**:

- `DriveStats` - DriveStats object instance

<a id="src/drivecatplus/drivestats.Cycle.add_acceleration"></a>

#### add\_acceleration

```python
def add_acceleration()
```

This method calculates acceleration_mps2 argument from speed_mps

<a id="src/drivecatplus/drivestats.DriveStats"></a>

## DriveStats Objects

```python
class DriveStats(object)
```

This class contains methods and arguments for calculating all DriveStats metrics.

<a id="src/drivecatplus/drivestats.DriveStats.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls, cycle: Cycle, units="SI")
```

This constructor creates a new DriveStats class object

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
  

**Returns**:

- `DriveStats` - class instance of DriveStats

<a id="src/drivecatplus/drivestats.DriveStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units="SI") -> None
```

This constructor accepts a Cycle object and calls the DriveStats calculation methods.

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats.to_dict"></a>

#### to\_dict

```python
def to_dict(units_system: str = "", include_prefix: bool = True)
```

This method exports all DriveStats results to a dictionary

**Arguments**:

- `units_system` _str, optional_ - Units system desired between ['SI', 'Imperial']. Defaults to "SI".
- `include_prefix` _bool, optional_ - If True, exported column names contain the DriveStats category names as prefix.
- `Example` - 'total_speed_stats.total_median_speed.mps'. If False, it would be 'total_median_speed.mps'. Defaults to True.

<a id="src/drivecatplus/drivestats.DriveStats.export_to_file"></a>

#### export\_to\_file

```python
@classmethod
def export_to_file(cls,
                   filepath: str,
                   units_system: str = "SI",
                   include_prefix=True)
```

This method generates the stats_dict exports all DriveStats results for a given drivecycle to an output CSV

**Arguments**:

- `filepath` _str_ - Filepath of output file
- `units_system` _str, optional_ - Units system desired between ['SI', 'Imperial']. Defaults to "SI".
- `include_prefix` _bool, optional_ - If True, exported column names contain the DriveStats category names as prefix.
- `Example` - 'total_speed_stats.total_median_speed.mps'. If False, it would be 'total_median_speed.mps'. Defaults to True.

<a id="src/drivecatplus/drivestats.DriveStats._TimeStats"></a>

## \_TimeStats Objects

```python
class _TimeStats(object)
```

This subclass calculates all time-related attributes:
    - absolute_time_duration
    - speed_data_duration
    - driving_data_duration
    - non_recorded_duration
    - collected_vs_real_time_ratio

<a id="src/drivecatplus/drivestats.DriveStats._TimeStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system="SI")
```

This method initializes TimeStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._SamplingStats"></a>

## \_SamplingStats Objects

```python
class _SamplingStats(object)
```

This subclass calculates time-sampling and frequency-based stats:
    - mean_estimated_sampling_rate
    - median_estimated_sampling_rate
    - max_gap_between_samples
    - min_gap_between_samples
    - mean_gap_between_samples
    - median_gap_between_samples
    - std_gap_between_samples
    - var_gap_between_samples
    - gap_25th_percentile
    - gap_75th_percentile
    - gap_inter_quartile_range
    - gap_median_absolute_deviation

<a id="src/drivecatplus/drivestats.DriveStats._SamplingStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system="SI") -> None
```

This constructor initializes SamplingStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._TotalSpeedStats"></a>

## \_TotalSpeedStats Objects

```python
class _TotalSpeedStats(object)
```

This subclass contains total speed related stats
    - max_speed
    - total_average_speed
    - total_median_speed
    - total_root_mean_cubed_speed
    - total_speed_var
    - total_speed_std
    - total_speed_velocity_ratio
    - total_speed_25th_percentile
    - total_speed_75th_percentile
    - total_speed_inter_quartile_range
    - total_speed_median_absolute_deviation

<a id="src/drivecatplus/drivestats.DriveStats._TotalSpeedStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system="SI") -> None
```

This constructor initializes TotalSpeedStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._DrivingSpeedStats"></a>

## \_DrivingSpeedStats Objects

```python
class _DrivingSpeedStats(object)
```

This subclass calculates Driving Speed related stats (excludes timestamps where speed is zero)
    - max_speed
    - driving_average_speed
    - driving_median_speed
    - driving_root_mean_cubed_speed
    - driving_speed_var
    - driving_speed_std
    - driving_speed_velocity_ratio
    - driving_speed_25th_percentile
    - driving_speed_75th_percentile
    - driving_speed_inter_quartile_range
    - driving_speed_median_absolute_deviation

<a id="src/drivecatplus/drivestats.DriveStats._DrivingSpeedStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system="SI") -> None
```

This constructor initializes DrivingSpeedStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._SpeedCountingStats"></a>

## \_SpeedCountingStats Objects

```python
class _SpeedCountingStats(object)
```

This subclass contains stats related to percentiles of speed timestamps
        - speed_count_zero
        - speed_count_zero_five
        - speed_count_five_ten
        - speed_count_ten_fifteen
        - speed_count_fifteen_twenty
        - speed_count_twenty_twenty_five
        - speed_count_twenty_five_thirty
        - speed_count_thirty_thirty_five
        - speed_count_thirty_five_fourty
        - speed_count_fourty_fourty_five
        - speed_count_fourty_five_fifty
        - speed_count_fifty_fifty_five
        - speed_count_fifty_five_sixty
        - speed_count_sixty_sixty_five
        - speed_count_sixty_five_seventy
        - speed_count_seventy_seventy_five
        - speed_count_seventy_five_plus
        - driving_time
        - percent_zero
        - percent_zero_five
        - percent_five_ten
        - percent_ten_fifteen
        - percent_fifteen_twenty
        - percent_twenty_twenty_five
        - percent_twenty_five_thirty
        - percent_thirty_thirty_five
        - percent_thirty_five_fourty
        - percent_fourty_fourty_five
        - percent_fourty_five_fifty
        - percent_fifty_fifty_five
        - percent_fifty_five_sixty
        - percent_sixty_sixty_five
        - percent_sixty_five_seventy
        - percent_seventy_seventy_five
        - percent_seventy_five_plus
        - percent_total
-

<a id="src/drivecatplus/drivestats.DriveStats._SpeedCountingStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes SpeedCountingStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._DistanceCountingStats"></a>

## \_DistanceCountingStats Objects

```python
class _DistanceCountingStats(object)
```

This subclass contains stats related to speed percentiles in distance
    - distance_count_zero_five
    - distance_count_five_ten
    - distance_count_ten_fifteen
    - distance_count_fifteen_twenty
    - distance_count_twenty_twenty_five
    - distance_count_twenty_five_thirty
    - distance_count_thirty_thirty_five
    - distance_count_thirty_five_fourty
    - distance_count_fourty_fourty_five
    - distance_count_fourty_five_fifty
    - distance_count_fifty_fifty_five
    - distance_count_fifty_five_sixty
    - distance_count_sixty_sixty_five
    - distance_count_sixty_five_seventy
    - distance_count_seventy_seventy_five
    - distance_count_seventy_five_plus
    - distance_total
    - percent_distance_zero_five
    - percent_distance_five_ten
    - percent_distance_ten_fifteen
    - percent_distance_fifteen_twenty
    - percent_distance_twenty_twenty_five
    - percent_distance_twenty_five_thirty
    - percent_distance_thirty_thirty_five
    - percent_distance_thirty_five_fourty
    - percent_distance_fourty_fourty_five
    - percent_distance_fourty_five_fifty
    - percent_distance_fifty_fifty_five
    - percent_distance_fifty_five_sixty
    - percent_distance_sixty_sixty_five
    - percent_distance_sixty_five_seventy
    - percent_distance_seventy_seventy_five
    - percent_distance_seventy_five_plus
    - percent_distance_total

<a id="src/drivecatplus/drivestats.DriveStats._DistanceCountingStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes all DistanceCountingStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._AccelerationStats"></a>

## \_AccelerationStats Objects

```python
class _AccelerationStats(object)
```

This subclass contains acceleration-related stats
        - total_number_of_acceleration_events
        - total_number_of_deceleration_events
        - acceleration_events_per_mile
        - deceleration_events_per_mile
        - max_acceleration
        - max_deceleration
        - average_acceleration
        - average_deceleration
        - median_acceleration
        - median_deceleration
        - std_acceleration
        - std_deceleration
        - var_acceleration
        - var_deceleration
        - acceleration_25th_percentile
        - deceleration_25th_percentile
        - acceleration_75th_percentile
        - deceleration_75th_percentile
        - acceleration_inter_quartile_range
        - deceleration_inter_quartile_range
        - acceleration_median_absolute_deviation
        - deceleration_median_absolute_deviation
        - cumulative_acceleration_duration
        - cumulative_deceleration_duration
        - cumulative_acceleration_cycle_duration_percent
        - cumulative_deceleration_cycle_duration_percent
        - absolute_time_cumulative_acceleration_duration
        - absolute_time_cumulative_deceleration_duration
        - absolute_time_cumulative_acceleration_cycle_duration_percent
        - absolute_time_cumulative_deceleration_cycle_duration_percent
        - average_acceleration_event_duration
        - average_deceleration_event_duration
        - min_acceleration_event_duration
        - min_deceleration_event_duration
        - max_acceleration_event_duration
        - max_deceleration_event_duration
        - std_acceleration_event_duration
        - std_deceleration_event_duration
        - var_acceleration_event_duration
        - var_deceleration_event_duration
        - median_acceleration_event_duration
        - median_deceleration_event_duration
        - acceleration_event_duration_25th_percentile
        - deceleration_event_duration_25th_percentile
        - acceleration_event_duration_75th_percentile
        - deceleration_event_duration_75th_percentile
        - acceleration_event_duration_inter_quartile_range
        - deceleration_event_duration_inter_quartile_range
        - acceleration_event_duration_median_absolute_deviation
        - deceleration_event_duration_median_absolute_deviation
-
        -

<a id="src/drivecatplus/drivestats.DriveStats._AccelerationStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes AccelerationStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._StopsCountingStats"></a>

## \_StopsCountingStats Objects

```python
class _StopsCountingStats(object)
```

This subclass contains stops related stats.
    - total_stops
    - stops_0_30
    - stops_30_60
    - stops_60_plus
    - stops_300_plus
    - stops_1800_plus
    - stops_3600_plus
    - stops_per_mile
    - average_stop_duration
    - min_stop_duration
    - max_stop_duration
    - median_stop_duration
    - mean_stop_duration
    - std_stop_duration
    - var_stop_duration
    - stop_duration_25th_percentile
    - stop_duration_75th_percentile
    - stop_duration_inter_quartile_range
    - stop_duration_median_absolute_deviation

<a id="src/drivecatplus/drivestats.DriveStats._StopsCountingStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes the StopsCountingStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._ElevationStats"></a>

## \_ElevationStats Objects

```python
class _ElevationStats(object)
```

This subclass contains elevation and grade related stats
    - max_elevation
    - min_elevation
    - mean_elevation
    - median_elevation
    - std_of_elevation
    - var_of_elevation
    - elevation_25th_percentile
    - elevation_75th_percentile
    - elevation_inter_quartile_range
    - elevation_median_absolute_deviation
    - delta_elevation
    - delta_elevation_cumulative
    - absolute_delta_elevation_cumulative
    - total_elevation_gained
    - total_elevation_lost
    - average_absolute_elevation_rate_change
    - max_climbing_rate
    - average_climbing_rate
    - median_climbing_rate
    - max_descending_rate
    - average_descending_rate
    - median_descending_rate
    - climbing_rate_25th_percentile
    - descending_rate_25th_percentile
    - climbing_rate_75th_percentile
    - descending_rate_75th_percentile
    - climbing_rate_inter_quartile_range
    - descending_rate_inter_quartile_range
    - climbing_rate_median_absolute_deviation
    - descending_rate_median_absolute_deviation
    - max_road_grade
    - min_road_grade
    - mean_road_grade
    - median_road_grade
    - std_of_road_grade
    - var_of_road_grade
    - road_grade_25th_percentile
    - road_grade_75th_percentile
    - road_grade_inter_quartile_range
    - road_grade_median_absolute_deviation

<a id="src/drivecatplus/drivestats.DriveStats._ElevationStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes the ElevationStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._PowerDensityStats"></a>

## \_PowerDensityStats Objects

```python
class _PowerDensityStats(object)
```

This subclass contains kinetic and potential power density stats. Potential power density stats are calculated where elevation data is available

    - maximum_kinetic_power_density_demand
    - total_kinetic_power_density_demand
    - average_kinetic_power_density_demand
    - variance_kinetic_power_density_demand
    - standard_deivation_kinetic_power_density_demand
    - maximum_kinetic_power_density_regen
    - total_kinetic_power_density_regen
    - average_kinetic_power_density_regen
    - variance_kinetic_power_density_regen
    - standard_deivation_kinetic_power_density_regen
    - maximum_potential_power_density_demand
    - total_potential_power_density_demand
    - average_potential_power_density_demand
    - variance_potential_power_density_demand
    - standard_deivation_potential_power_density_demand
    - maximum_potential_power_density_regen
    - total_potential_power_density_regen
    - average_potential_power_density_regen
    - variance_potential_power_density_regen
    - standard_deivation_potential_power_density_regen
    - maximum_aerodynamic_power_density_demand
    - total_aerodynamic_power_density_demand
    - average_aerodynamic_power_density_demand
    - variance_aerodynamic_power_density_demand
    - standard_deivation_aerodynamic_power_density_demand
    - maximum_aerodynamic_power_density_regen
    - total_aerodynamic_power_density_regen
    - average_aerodynamic_power_density_regen
    - variance_aerodynamic_power_density_regen
    - standard_deivation_aerodynamic_power_density_regen
    - maximum_rolling_power_density_demand
    - total_rolling_power_density_demand
    - average_rolling_power_density_demand
    - variance_rolling_power_density_demand
    - standard_deivation_rolling_power_density_demand
    - maximum_rolling_power_density_regen
    - total_rolling_power_density_regen
    - average_rolling_power_density_regen
    - variance_rolling_power_density_regen
    - standard_deivation_rolling_power_density_regen

<a id="src/drivecatplus/drivestats.DriveStats._PowerDensityStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes the PowerDensityStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._EnergyDensityStats"></a>

## \_EnergyDensityStats Objects

```python
class _EnergyDensityStats(object)
```

This subclass contains kinetic, potential, aerodynamic, and rolling energy density stats. Potential power density stats are calculated where elevation data is available

    - maximum_instantanteous_potential_energy_density
    - average_instantanteous_potential_energy_density
    - cumulative_instanteous_potential_energy_density
    - maximum_instantanteous_kinetic_energy_density
    - average_instantanteous_kinetic_energy_density
    - cumulative_instanteous_kinetic_energy_density
    - maximum_instantanteous_aerodynamic_energy_density
    - average_instantanteous_aerodynamic_energy_density
    - cumulative_instanteous_aerodynamic_energy_density
    - maximum_instantanteous_rolling_energy_density
    - average_instantanteous_rolling_energy_density
    - cumulative_instanteous_rolling_energy_density

<a id="src/drivecatplus/drivestats.DriveStats._EnergyDensityStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes the EnergyDensityStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._KineticIntensityStats"></a>

## \_KineticIntensityStats Objects

```python
class _KineticIntensityStats(object)
```

This subclass contains kinetic intensity related calculations

    - characteristic_acceleration
    - characteristic_deceleration
    - aerodynamic_speed
    - kinetic_intensity

<a id="src/drivecatplus/drivestats.DriveStats._KineticIntensityStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes the KineticIntensityStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

<a id="src/drivecatplus/drivestats.DriveStats._DistanceStats"></a>

## \_DistanceStats Objects

```python
class _DistanceStats(object)
```

This subclass calculates total distance.
    - distance_total

<a id="src/drivecatplus/drivestats.DriveStats._DistanceStats.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cycle: Cycle, units_system: str = "SI")
```

This constructor initializes the DistanceStats calculations

**Arguments**:

- `cycle` _Cycle_ - Input Cycle object
- `units` _str, optional_ - Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

