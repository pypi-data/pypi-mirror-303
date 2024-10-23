"""DriveStats/SpeedCalcs"""

from __future__ import annotations

import inspect

import numpy as np
import pandas as pd

import drivecatplus.Global as gl
from drivecatplus.units import Units
from typing_extensions import Self
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Cycle(object):
    """
    This class is used to initialize and manipulate an input drivecycle. The three main aspects of a drivecycle are Time, Speed, and Elevation (wherever applicable).
    """

    time_s: np.ndarray(1, dtype=float)
    speed_mps: np.ndarray(1, dtype=float)
    elevation_m: np.ndarray(1, dtype=float)

    # def __init__(self, speed_mps: list = None, time_s: list = None, elevation_m: list = None) -> None:
    #     self.speed_mps = speed_mps
    #     self.time_s = time_s
    #     if elevation_m:
    #         self.elevation_m = elevation_m

    @classmethod
    def from_file(
        cls,
        filepath: str | Path,
        var_name_dict: dict = {"speed_mps": "speed_mps", "time_s": "time_s"},
    ) -> Self:
        """
        This method is used to initialize a Cycle object from a CSV file.

        Args:
            filepath (str | Path): Filepath of the input drivecycle CSV file
            var_name_dict (dict, optional): Dictionary containing column names for 'speed_mps', 'time_s', and 'elevation_m'. Defaults to {"speed_mps": "speed_mps", "time_s": "time_s"}.

        Returns:
            Self: Cycle object
        """
        filepath = Path(filepath)
        if filepath.suffix in [".csv", ".CSV"]:
            columns = var_name_dict.values()
            cycle_df = pd.read_csv(filepath, usecols=columns)
            cycle_df = cycle_df.rename(columns={v: k for k, v in var_name_dict.items()})
            cycle_dict = cycle_df.to_dict(orient="list")
        return cls.from_dict(cycle_dict)

    @classmethod
    def from_dict(cls, cycle_dict: dict) -> Self:
        """
        This method is used to initialize a Cycle object using a dictionary of arrays/lists of Time, Speed, and Elevation traces.

        Args:
            cycle_dict (dict): Dictionary containing lists of equal length of Time, Speed, and Elevation

        Returns:
            Self: Cycle object instance
        """
        cycle_dict["elevation_m"] = cycle_dict.get(
            "elevation_m", np.zeros(len(cycle_dict["time_s"]))
        )
        return cls(**cycle_dict)

    @classmethod
    def generate_stats(self, units: str = "SI") -> DriveStats:
        """
        This method is used to calculate all DriveStats.

        Args:
            units (str, optional): Units system desired between ['SI', 'Imperial']. Defaults to "SI".

        Returns:
            DriveStats: DriveStats object instance
        """
        return DriveStats(self, units=units)

    def add_acceleration(self) -> None:
        """
        This method calculates acceleration_mps2 argument from speed_mps
        """
        self.acceleration_mps2 = np.diff(np.array(self.speed_mps), prepend=0.0)


class DriveStats(object):
    """
    This class contains methods and arguments for calculating all DriveStats metrics.
    """

    cycle: Cycle = None

    def __new__(cls, cycle: Cycle, units="SI"):
        """This constructor creates a new DriveStats class object

        Args:
            cycle (Cycle):  Input Cycle object
            units (str, optional):  Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

        Returns:
            DriveStats: class instance of DriveStats
        """
        if units == "SI":
            return super().__new__(cls)

    # mean_speed_mps: float = None
    def __init__(self, cycle: Cycle, units="SI") -> None:
        """
        This constructor accepts a Cycle object and calls the DriveStats calculation methods.

        Args:
            cycle (Cycle): Input Cycle object
            units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
        """
        self.cycle = cycle
        self.cycle.speed_mps = np.array(self.cycle.speed_mps)
        self.cycle.time_s = np.array(self.cycle.time_s)
        self.time_stats = self._TimeStats(self.cycle, units_system=units)
        self.distance_stats = self._DistanceStats(self.cycle, units_system=units)
        self.total_speed_stats = self._TotalSpeedStats(self.cycle, units_system=units)

        self.driving_speed_stats = self._DrivingSpeedStats(
            self.cycle, units_system=units
        )
        self.acceleration_stats = self._AccelerationStats(
            self.cycle, units_system=units
        )
        self.sampling_stats = self._SamplingStats(self.cycle, units_system=units)

        self.speed_count_stats = self._SpeedCountingStats(
            self.cycle, units_system=units
        )
        self.distance_count_stats = self._DistanceCountingStats(
            self.cycle, units_system=units
        )
        self.stop_count_stats = self._StopsCountingStats(self.cycle, units_system=units)

        self.elevation_stats = self._ElevationStats(self.cycle, units_system=units)
        self.power_density_stats = self._PowerDensityStats(
            self.cycle, units_system=units
        )
        self.energy_density_stats = self._EnergyDensityStats(
            self.cycle, units_system=units
        )
        self.kinetic_intensity_stats = self._KineticIntensityStats(
            self.cycle, units_system=units
        )

    def to_dict(self, units_system: str = "SI", include_prefix: bool = True):
        """
        This method exports all DriveStats results to a dictionary

        Args:
            units_system (str, optional): Units system desired between ['SI', 'Imperial']. Defaults to "SI".
            include_prefix (bool, optional): If True, exported column names contain the DriveStats category names as prefix.
                                            Example: 'total_speed_stats.total_median_speed.mps'. If False, it would be 'total_median_speed.mps'. Defaults to True.
        """
        stats_dict = {}
        if units_system in ["SI", "SI_units", "si"]:
            units_list = ["m", "s", "mps", "mps2", "hz", "pm", "Jpkg", "m2ps3"]
        for key, value in self.__dict__.items():
            if "_stats" in key:
                for key2 in value.__dir__():
                    if "__" not in key2:
                        value2 = value.__getattribute__(key2)

                        if isinstance(value2, (np.floating, float)):
                            if include_prefix:
                                stats_dict[key + "." + key2] = value2
                            else:
                                stats_dict[key2] = value2
                        elif hasattr(value2, "__dict__"):
                            for item in units_list:
                                value3 = value2.__dict__.get(item)
                                if value3 != None:
                                    unit_value = value3
                                    unit = item
                                    break
                            if include_prefix:
                                stats_dict[key + "." + key2 + "." + unit] = unit_value
                            else:
                                stats_dict[key2 + "." + unit] = unit_value
        return stats_dict

    def export_to_file(
        self, filepath: str, units_system: str = "SI", include_prefix=True
    ):
        """
        This method generates the stats_dict exports all DriveStats results for a given drivecycle to an output CSV

        Args:
            filepath (str): Filepath of output file
            units_system (str, optional): Units system desired between ['SI', 'Imperial']. Defaults to "SI".
            include_prefix (bool, optional): If True, exported column names contain the DriveStats category names as prefix.
                                            Example: 'total_speed_stats.total_median_speed.mps'. If False, it would be 'total_median_speed.mps'. Defaults to True.
        """
        export_dict = {}
        export_dict["filename"] = filepath
        stats_dict = self.to_dict(
            units_system=units_system, include_prefix=include_prefix
        )
        export_dict.update(stats_dict)

        export_df = pd.DataFrame(export_dict, index=[0]).reset_index()
        export_df.to_csv(filepath, index=False)
        print(f"DriveCAT+ Results: {filepath}")

    class _TimeStats(object):
        """
        This subclass calculates all time-related attributes:
            - absolute_time_duration
            - speed_data_duration
            - driving_data_duration
            - non_recorded_duration
            - collected_vs_real_time_ratio
        """

        absolute_time_duration = Units.TimeUnits()
        speed_data_duration = Units.TimeUnits()
        driving_data_duration = Units.TimeUnits()
        non_recorded_duration = Units.TimeUnits()
        collected_vs_real_time_ratio: float = 0

        def __init__(self, cycle: Cycle, units_system="SI"):
            """
            This method initializes TimeStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".

            """
            self.absolute_time_duration.s = cycle.time_s[-1] - cycle.time_s[0] + 1
            self.speed_data_duration.s = len(cycle.time_s)
            self.driving_data_duration.s = len(cycle.speed_mps[cycle.speed_mps > 0])
            self.non_recorded_duration.s = (
                self.absolute_time_duration.s - self.speed_data_duration.s
            )
            self.collected_vs_real_time_ratio = (
                self.speed_data_duration.s / self.absolute_time_duration.s
                if self.absolute_time_duration.s
                else 0.0
            )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _SamplingStats(object):
        """
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

        """

        mean_estimated_sampling_rate = Units.FrequencyUnits()
        median_estimated_sampling_rate = Units.FrequencyUnits()
        max_gap_between_samples = Units.TimeUnits()
        min_gap_between_samples = Units.TimeUnits()
        mean_gap_between_samples = Units.TimeUnits()
        median_gap_between_samples = Units.TimeUnits()
        std_gap_between_samples = Units.TimeUnits()
        var_gap_between_samples = Units.TimeUnits()
        gap_25th_percentile = Units.TimeUnits()
        gap_75th_percentile = Units.TimeUnits()
        gap_inter_quartile_range = Units.TimeUnits()
        gap_median_absolute_deviation = Units.TimeUnits()

        def __init__(self, cycle: Cycle, units_system="SI") -> None:
            """
            This constructor initializes SamplingStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            delta_time_s = np.diff(cycle.time_s)
            self.mean_estimated_sampling_rate.hz = (
                1 / np.mean(delta_time_s) if np.mean(delta_time_s) else np.nan
            )
            self.median_estimated_sampling_rate_hz = (
                1 / np.median(delta_time_s) if np.median(delta_time_s) else np.nan
            )
            self.max_gap_between_samples.s = np.max(delta_time_s)
            self.min_gap_between_samples.s = np.min(delta_time_s)
            self.mean_gap_between_samples.s = np.mean(delta_time_s)
            self.median_gap_between_samples.s = np.median(delta_time_s)
            self.std_gap_between_samples.s = np.std(delta_time_s)
            self.var_gap_between_samples.s = np.var(delta_time_s)
            self.gap_25th_percentile.s = np.percentile(delta_time_s, 25)
            self.gap_75th_percentile.s = np.percentile(delta_time_s, 75)
            self.gap_inter_quartile_range.s = (
                self.gap_75th_percentile.s - self.gap_25th_percentile.s
            )
            self.gap_median_absolute_deviation.s = np.median(
                np.abs(delta_time_s - np.median(delta_time_s))
            )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _TotalSpeedStats(object):
        """
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

        """

        max_speed = Units.SpeedUnits()
        total_average_speed = Units.SpeedUnits()
        total_median_speed = Units.SpeedUnits()
        total_root_mean_cubed_speed = Units.SpeedUnits()
        total_speed_var = Units.SpeedUnits()
        total_speed_std = Units.SpeedUnits()
        total_speed_velocity_ratio: float = 0
        total_speed_25th_percentile = Units.SpeedUnits()
        total_speed_75th_percentile = Units.SpeedUnits()
        total_speed_inter_quartile_range = Units.SpeedUnits()
        total_speed_median_absolute_deviation = Units.SpeedUnits()

        def __init__(self, cycle: Cycle, units_system="SI") -> None:
            """
            This constructor initializes TotalSpeedStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            self.max_speed.mps = np.max(cycle.speed_mps)
            self.total_average_speed.mps = np.mean(cycle.speed_mps)
            self.total_median_speed.mps = np.median(cycle.speed_mps)
            self.total_root_mean_cubed_speed.mps = np.mean(cycle.speed_mps**3.0) ** (
                1.0 / 3.0
            )
            self.total_speed_var.mps = np.var(cycle.speed_mps)
            self.total_speed_std.mps = np.std(cycle.speed_mps)
            self.total_speed_velocity_ratio = (
                self.total_root_mean_cubed_speed.mps / self.total_average_speed.mps
                if self.total_average_speed.mps
                else np.nan
            )
            self.total_speed_25th_percentile.mps = np.percentile(cycle.speed_mps, 25)
            self.total_speed_75th_percentile.mps = np.percentile(cycle.speed_mps, 75)
            self.total_speed_inter_quartile_range.mps = (
                self.total_speed_75th_percentile.mps
                - self.total_speed_25th_percentile.mps
            )
            self.total_speed_median_absolute_deviation.mps = np.median(
                np.abs(cycle.speed_mps - np.median(cycle.speed_mps))
            )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _DrivingSpeedStats(object):
        """
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

        """

        max_speed = Units.SpeedUnits()
        driving_average_speed = Units.SpeedUnits()
        driving_median_speed = Units.SpeedUnits()
        driving_root_mean_cubed_speed = Units.SpeedUnits()
        driving_speed_var = Units.SpeedUnits()
        driving_speed_std = Units.SpeedUnits()
        driving_speed_velocity_ratio: float = 0
        driving_speed_25th_percentile = Units.SpeedUnits()
        driving_speed_75th_percentile = Units.SpeedUnits()
        driving_speed_inter_quartile_range = Units.SpeedUnits()
        driving_speed_median_absolute_deviation = Units.SpeedUnits()

        def __init__(self, cycle: Cycle, units_system="SI") -> None:
            """
            This constructor initializes DrivingSpeedStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            driving_speed_mps = cycle.speed_mps[cycle.speed_mps > 0.0]
            self.max_speed.kmph = np.max(driving_speed_mps)
            self.driving_average_speed.mps = np.mean(driving_speed_mps)
            self.driving_median_speed.mps = np.median(driving_speed_mps)
            self.driving_root_mean_cubed_speed.mps = np.mean(
                driving_speed_mps**3.0
            ) ** (1.0 / 3.0)
            self.driving_speed_var.mps = np.var(driving_speed_mps)
            self.driving_speed_std.mps = np.std(driving_speed_mps)
            self.driving_speed_velocity_ratio = (
                self.driving_root_mean_cubed_speed.mps / self.driving_average_speed.mps
                if self.driving_average_speed.mps
                else np.nan
            )
            self.driving_speed_25th_percentile.mps = np.percentile(
                driving_speed_mps, 25
            )
            self.driving_speed_75th_percentile.mps = np.percentile(
                driving_speed_mps, 75
            )
            self.driving_speed_inter_quartile_range.mps = (
                self.driving_speed_75th_percentile.mps
                - self.driving_speed_25th_percentile.mps
            )
            self.driving_speed_median_absolute_deviation.mps = np.median(
                np.abs(driving_speed_mps - np.median(driving_speed_mps))
            )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _SpeedCountingStats(object):
        """
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
        """

        speed_count_zero = Units.TimeUnits()
        speed_count_zero_five = Units.TimeUnits()
        speed_count_five_ten = Units.TimeUnits()
        speed_count_ten_fifteen = Units.TimeUnits()
        speed_count_fifteen_twenty = Units.TimeUnits()
        speed_count_twenty_twenty_five = Units.TimeUnits()
        speed_count_twenty_five_thirty = Units.TimeUnits()
        speed_count_thirty_thirty_five = Units.TimeUnits()
        speed_count_thirty_five_fourty = Units.TimeUnits()
        speed_count_fourty_fourty_five = Units.TimeUnits()
        speed_count_fourty_five_fifty = Units.TimeUnits()
        speed_count_fifty_fifty_five = Units.TimeUnits()
        speed_count_fifty_five_sixty = Units.TimeUnits()
        speed_count_sixty_sixty_five = Units.TimeUnits()
        speed_count_sixty_five_seventy = Units.TimeUnits()
        speed_count_seventy_seventy_five = Units.TimeUnits()
        speed_count_seventy_five_plus = Units.TimeUnits()
        driving_time = Units.TimeUnits()
        percent_zero: float = 0
        percent_zero_five: float = 0
        percent_five_ten: float = 0
        percent_ten_fifteen: float = 0
        percent_fifteen_twenty: float = 0
        percent_twenty_twenty_five: float = 0
        percent_twenty_five_thirty: float = 0
        percent_thirty_thirty_five: float = 0
        percent_thirty_five_fourty: float = 0
        percent_fourty_fourty_five: float = 0
        percent_fourty_five_fifty: float = 0
        percent_fifty_fifty_five: float = 0
        percent_fifty_five_sixty: float = 0
        percent_sixty_sixty_five: float = 0
        percent_sixty_five_seventy: float = 0
        percent_seventy_seventy_five: float = 0
        percent_seventy_five_plus: float = 0
        percent_total: float = 0

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """
            This constructor initializes SpeedCountingStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            speed_kmph = cycle.speed_mps * gl.KPH_2_MPS
            self.speed_count_zero.s = len(np.argwhere(speed_kmph == 0.0))
            self.speed_count_zero_five.s = len(
                np.argwhere(np.logical_and(speed_kmph > 0.0, speed_kmph <= 5.0))
            )
            self.speed_count_five_ten.s = len(
                np.argwhere(np.logical_and(speed_kmph > 5.0, speed_kmph <= 10.0))
            )
            self.speed_count_ten_fifteen.s = len(
                np.argwhere(np.logical_and(speed_kmph > 10.0, speed_kmph <= 15.0))
            )
            self.speed_count_fifteen_twenty.s = len(
                np.argwhere(np.logical_and(speed_kmph > 15.0, speed_kmph <= 20.0))
            )
            self.speed_count_twenty_twenty_five.s = len(
                np.argwhere(np.logical_and(speed_kmph > 20.0, speed_kmph <= 25.0))
            )
            self.speed_count_twenty_five_thirty.s = len(
                np.argwhere(np.logical_and(speed_kmph > 25.0, speed_kmph <= 30.0))
            )
            self.speed_count_thirty_thirty_five.s = len(
                np.argwhere(np.logical_and(speed_kmph > 30.0, speed_kmph <= 35.0))
            )
            self.speed_count_thirty_five_fourty.s = len(
                np.argwhere(np.logical_and(speed_kmph > 35.0, speed_kmph <= 40.0))
            )
            self.speed_count_fourty_fourty_five.s = len(
                np.argwhere(np.logical_and(speed_kmph > 40.0, speed_kmph <= 45.0))
            )
            self.speed_count_fourty_five_fifty.s = len(
                np.argwhere(np.logical_and(speed_kmph > 45.0, speed_kmph <= 50.0))
            )
            self.speed_count_fifty_fifty_five.s = len(
                np.argwhere(np.logical_and(speed_kmph > 50.0, speed_kmph <= 55.0))
            )
            self.speed_count_fifty_five_sixty.s = len(
                np.argwhere(np.logical_and(speed_kmph > 55.0, speed_kmph <= 60.0))
            )
            self.speed_count_sixty_sixty_five.s = len(
                np.argwhere(np.logical_and(speed_kmph > 60.0, speed_kmph <= 65.0))
            )
            self.speed_count_sixty_five_seventy.s = len(
                np.argwhere(np.logical_and(speed_kmph > 65.0, speed_kmph <= 70.0))
            )
            self.speed_count_seventy_seventy_five.s = len(
                np.argwhere(np.logical_and(speed_kmph > 70.0, speed_kmph <= 75.0))
            )
            self.speed_count_seventy_five_plus.s = len(np.argwhere(speed_kmph > 75.0))
            self.driving_time.s = len(np.argwhere(speed_kmph > 0.0))

            num_samples = len(speed_kmph)
            if num_samples:
                self.percent_zero = self.speed_count_zero.s / num_samples
                self.percent_zero_five = self.speed_count_zero_five.s / num_samples
                self.percent_five_ten = self.speed_count_five_ten.s / num_samples
                self.percent_ten_fifteen = self.speed_count_ten_fifteen.s / num_samples
                self.percent_fifteen_twenty = (
                    self.speed_count_fifteen_twenty.s / num_samples
                )
                self.percent_twenty_twenty_five = (
                    self.speed_count_twenty_twenty_five.s / num_samples
                )
                self.percent_twenty_five_thirty = (
                    self.speed_count_twenty_five_thirty.s / num_samples
                )
                self.percent_thirty_thirty_five = (
                    self.speed_count_thirty_thirty_five.s / num_samples
                )
                self.percent_thirty_five_fourty = (
                    self.speed_count_thirty_five_fourty.s / num_samples
                )
                self.percent_fourty_fourty_five = (
                    self.speed_count_fourty_fourty_five.s / num_samples
                )
                self.percent_fourty_five_fifty = (
                    self.speed_count_fourty_five_fifty.s / num_samples
                )
                self.percent_fifty_fifty_five = (
                    self.speed_count_fifty_fifty_five.s / num_samples
                )
                self.percent_fifty_five_sixty = (
                    self.speed_count_fifty_five_sixty.s / num_samples
                )
                self.percent_sixty_sixty_five = (
                    self.speed_count_sixty_sixty_five.s / num_samples
                )
                self.percent_sixty_five_seventy = (
                    self.speed_count_sixty_five_seventy.s / num_samples
                )
                self.percent_seventy_seventy_five = (
                    self.speed_count_seventy_seventy_five.s / num_samples
                )
                self.percent_seventy_five_plus = (
                    self.speed_count_seventy_five_plus.s / num_samples
                )
                self.percent_total = (
                    self.percent_zero
                    + self.percent_zero_five
                    + self.percent_five_ten
                    + self.percent_ten_fifteen
                    + self.percent_fifteen_twenty
                    + self.percent_twenty_twenty_five
                    + self.percent_twenty_five_thirty
                    + self.percent_thirty_thirty_five
                    + self.percent_thirty_five_fourty
                    + self.percent_fourty_fourty_five
                    + self.percent_fourty_five_fifty
                    + self.percent_fifty_fifty_five
                    + self.percent_fifty_five_sixty
                    + self.percent_sixty_sixty_five
                    + self.percent_sixty_five_seventy
                )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _DistanceCountingStats(object):
        """
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
        """

        distance_count_zero_five = Units.DistanceUnits()
        distance_count_five_ten = Units.DistanceUnits()
        distance_count_ten_fifteen = Units.DistanceUnits()
        distance_count_fifteen_twenty = Units.DistanceUnits()
        distance_count_twenty_twenty_five = Units.DistanceUnits()
        distance_count_twenty_five_thirty = Units.DistanceUnits()
        distance_count_thirty_thirty_five = Units.DistanceUnits()
        distance_count_thirty_five_fourty = Units.DistanceUnits()
        distance_count_fourty_fourty_five = Units.DistanceUnits()
        distance_count_fourty_five_fifty = Units.DistanceUnits()
        distance_count_fifty_fifty_five = Units.DistanceUnits()
        distance_count_fifty_five_sixty = Units.DistanceUnits()
        distance_count_sixty_sixty_five = Units.DistanceUnits()
        distance_count_sixty_five_seventy = Units.DistanceUnits()
        distance_count_seventy_seventy_five = Units.DistanceUnits()
        distance_count_seventy_five_plus = Units.DistanceUnits()
        distance_total = Units.DistanceUnits()
        percent_distance_zero_five: float = 0
        percent_distance_five_ten: float = 0
        percent_distance_ten_fifteen: float = 0
        percent_distance_fifteen_twenty: float = 0
        percent_distance_twenty_twenty_five: float = 0
        percent_distance_twenty_five_thirty: float = 0
        percent_distance_thirty_thirty_five: float = 0
        percent_distance_thirty_five_fourty: float = 0
        percent_distance_fourty_fourty_five: float = 0
        percent_distance_fourty_five_fifty: float = 0
        percent_distance_fifty_fifty_five: float = 0
        percent_distance_fifty_five_sixty: float = 0
        percent_distance_sixty_sixty_five: float = 0
        percent_distance_sixty_five_seventy: float = 0
        percent_distance_seventy_seventy_five: float = 0
        percent_distance_seventy_five_plus: float = 0
        percent_distance_total: float = 0

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """
            This constructor initializes all DistanceCountingStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            delta_distance_m = cycle.speed_mps * np.diff(cycle.time_s, append=0)
            speed_kmph = cycle.speed_mps * gl.KPH_2_MPS

            self.distance_count_zero_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph >= 0.0, speed_kmph <= 5.0))
                ]
            )
            self.distance_count_zero_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 0.0, speed_kmph <= 5.0))
                ]
            )
            self.distance_count_five_ten.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 5.0, speed_kmph <= 10.0))
                ]
            )
            self.distance_count_ten_fifteen.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 10.0, speed_kmph <= 15.0))
                ]
            )
            self.distance_count_fifteen_twenty.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 15.0, speed_kmph <= 20.0))
                ]
            )
            self.distance_count_twenty_twenty_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 20.0, speed_kmph <= 25.0))
                ]
            )
            self.distance_count_twenty_five_thirty.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 25.0, speed_kmph <= 30.0))
                ]
            )
            self.distance_count_thirty_thirty_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 30.0, speed_kmph <= 35.0))
                ]
            )
            self.distance_count_thirty_five_fourty.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 35.0, speed_kmph <= 40.0))
                ]
            )
            self.distance_count_fourty_fourty_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 40.0, speed_kmph <= 45.0))
                ]
            )
            self.distance_count_fourty_five_fifty.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 45.0, speed_kmph <= 50.0))
                ]
            )
            self.distance_count_fifty_fifty_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 50.0, speed_kmph <= 55.0))
                ]
            )
            self.distance_count_fifty_five_sixty.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 55.0, speed_kmph <= 60.0))
                ]
            )
            self.distance_count_sixty_sixty_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 60.0, speed_kmph <= 65.0))
                ]
            )
            self.distance_count_sixty_five_seventy.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 65.0, speed_kmph <= 70.0))
                ]
            )
            self.distance_count_seventy_seventy_five.m = np.sum(
                delta_distance_m[
                    np.argwhere(np.logical_and(speed_kmph > 70.0, speed_kmph <= 75.0))
                ]
            )
            self.distance_count_seventy_five_plus.m = np.sum(
                delta_distance_m[np.argwhere(speed_kmph > 75.0)]
            )
            self.distance_total.m = np.sum(delta_distance_m)

            self.percent_distance_zero_five = (
                self.distance_count_zero_five.m / self.distance_total.m
            )
            self.percent_distance_five_ten = (
                self.distance_count_five_ten.m / self.distance_total.m
            )
            self.percent_distance_ten_fifteen = (
                self.distance_count_ten_fifteen.m / self.distance_total.m
            )
            self.percent_distance_fifteen_twenty = (
                self.distance_count_fifteen_twenty.m / self.distance_total.m
            )
            self.percent_distance_twenty_twenty_five = (
                self.distance_count_twenty_twenty_five.m / self.distance_total.m
            )
            self.percent_distance_twenty_five_thirty = (
                self.distance_count_twenty_five_thirty.m / self.distance_total.m
            )
            self.percent_distance_thirty_thirty_five = (
                self.distance_count_thirty_thirty_five.m / self.distance_total.m
            )
            self.percent_distance_thirty_five_fourty = (
                self.distance_count_thirty_five_fourty.m / self.distance_total.m
            )
            self.percent_distance_fourty_fourty_five = (
                self.distance_count_fourty_fourty_five.m / self.distance_total.m
            )
            self.percent_distance_fourty_five_fifty = (
                self.distance_count_fourty_five_fifty.m / self.distance_total.m
            )
            self.percent_distance_fifty_fifty_five = (
                self.distance_count_fifty_fifty_five.m / self.distance_total.m
            )
            self.percent_distance_fifty_five_sixty = (
                self.distance_count_fifty_five_sixty.m / self.distance_total.m
            )
            self.percent_distance_sixty_sixty_five = (
                self.distance_count_sixty_sixty_five.m / self.distance_total.m
            )
            self.percent_distance_sixty_five_seventy = (
                self.distance_count_sixty_five_seventy.m / self.distance_total.m
            )
            self.percent_distance_seventy_seventy_five = (
                self.distance_count_seventy_seventy_five.m / self.distance_total.m
            )
            self.percent_distance_seventy_five_plus = (
                self.distance_count_seventy_five_plus.m / self.distance_total.m
            )
            self.percent_distance_total = (
                self.percent_distance_zero_five
                + self.percent_distance_five_ten
                + self.percent_distance_ten_fifteen
                + self.percent_distance_fifteen_twenty
                + self.percent_distance_twenty_twenty_five
                + self.percent_distance_twenty_five_thirty
                + self.percent_distance_thirty_thirty_five
                + self.percent_distance_thirty_five_fourty
                + self.percent_distance_fourty_fourty_five
                + self.percent_distance_fourty_five_fifty
                + self.percent_distance_fifty_fifty_five
                + self.percent_distance_fifty_five_sixty
                + self.percent_distance_sixty_sixty_five
                + self.percent_distance_sixty_five_seventy
            )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _AccelerationStats(object):
        """
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
                -"""

        total_number_of_acceleration_events = Units.AccelerationUnits()
        total_number_of_deceleration_events = Units.AccelerationUnits()
        acceleration_events_per_mile = Units.PerDistanceUnits()
        deceleration_events_per_mile = Units.PerDistanceUnits()
        max_acceleration = Units.AccelerationUnits()
        max_deceleration = Units.AccelerationUnits()
        average_acceleration = Units.AccelerationUnits()
        average_deceleration = Units.AccelerationUnits()
        median_acceleration = Units.AccelerationUnits()
        median_deceleration = Units.AccelerationUnits()
        std_acceleration = Units.AccelerationUnits()
        std_deceleration = Units.AccelerationUnits()
        var_acceleration = Units.AccelerationUnits()
        var_deceleration = Units.AccelerationUnits()
        acceleration_25th_percentile = Units.AccelerationUnits()
        deceleration_25th_percentile = Units.AccelerationUnits()
        acceleration_75th_percentile = Units.AccelerationUnits()
        deceleration_75th_percentile = Units.AccelerationUnits()
        acceleration_inter_quartile_range = Units.AccelerationUnits()
        deceleration_inter_quartile_range = Units.AccelerationUnits()
        acceleration_median_absolute_deviation = Units.AccelerationUnits()
        deceleration_median_absolute_deviation = Units.AccelerationUnits()
        cumulative_acceleration_duration = Units.TimeUnits()
        cumulative_deceleration_duration = Units.TimeUnits()
        cumulative_acceleration_cycle_duration_percent = Units.TimeUnits()
        cumulative_deceleration_cycle_duration_percent = Units.TimeUnits()
        absolute_time_cumulative_acceleration_duration = Units.TimeUnits()
        absolute_time_cumulative_deceleration_duration = Units.TimeUnits()
        absolute_time_cumulative_acceleration_cycle_duration_percent: float = 0
        absolute_time_cumulative_deceleration_cycle_duration_percent: float = 0
        average_acceleration_event_duration = Units.TimeUnits()
        average_deceleration_event_duration = Units.TimeUnits()
        min_acceleration_event_duration = Units.TimeUnits()
        min_deceleration_event_duration = Units.TimeUnits()
        max_acceleration_event_duration = Units.TimeUnits()
        max_deceleration_event_duration = Units.TimeUnits()
        std_acceleration_event_duration = Units.TimeUnits()
        std_deceleration_event_duration = Units.TimeUnits()
        var_acceleration_event_duration = Units.TimeUnits()
        var_deceleration_event_duration = Units.TimeUnits()
        median_acceleration_event_duration = Units.TimeUnits()
        median_deceleration_event_duration = Units.TimeUnits()
        acceleration_event_duration_25th_percentile = Units.TimeUnits()
        deceleration_event_duration_25th_percentile = Units.TimeUnits()
        acceleration_event_duration_75th_percentile = Units.TimeUnits()
        deceleration_event_duration_75th_percentile = Units.TimeUnits()
        acceleration_event_duration_inter_quartile_range = Units.TimeUnits()
        deceleration_event_duration_inter_quartile_range = Units.TimeUnits()
        acceleration_event_duration_median_absolute_deviation = Units.TimeUnits()
        deceleration_event_duration_median_absolute_deviation = Units.TimeUnits()

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """
            This constructor initializes AccelerationStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            delta_time_s = np.diff(cycle.time_s)
            delta_speed = np.divide(
                np.diff(cycle.speed_mps),
                delta_time_s,
                out=np.zeros_like(np.diff(cycle.speed_mps)),
                where=delta_time_s != 0,
            )
            delta_square_speed = np.diff(delta_speed, append=0.0)
            acceleration = np.r_[
                0.0,
                np.divide(
                    delta_square_speed,
                    delta_time_s,
                    out=np.zeros_like(delta_square_speed),
                    where=delta_time_s != 0,
                )
                * gl.MPH_2_FTSS,
            ]
            accel_start_index = (
                np.argwhere(
                    np.logical_and(acceleration[0:-1] <= 0.0, acceleration[1:] > 0.0)
                )
                .flatten()
                .astype(int)
                + 1
            )
            accel_end_index = []
            decel_start_index = (
                np.argwhere(
                    np.logical_and(acceleration[0:-1] > 0.0, acceleration[1:] < 0.0)
                )
                .flatten()
                .astype(int)
                + 1
            )
            decel_end_index = []
            decel_durations = []

            average_accels = []
            max_accels = []
            average_decels = []
            max_decels = []
            accel_durations = []
            num_samples = len(cycle.speed_mps)
            delta_distance_m = cycle.speed_mps * np.diff(cycle.time_s, append=0)
            distance_total = sum(delta_distance_m)

            # Start of the acceleration index for loop
            for i in range(len(accel_start_index)):
                if i != len(accel_start_index) - 1:
                    accel_end_index.append(
                        int(
                            accel_start_index[i]
                            + np.argwhere(
                                acceleration[
                                    accel_start_index[i] : accel_start_index[i + 1]
                                ]
                                <= 0
                            )[0]
                        )
                    )
                else:
                    if any(np.argwhere(acceleration[accel_start_index[i] :] <= 0)):
                        accel_end_index.append(
                            int(
                                accel_start_index[i]
                                + np.argwhere(
                                    acceleration[accel_start_index[i] :] <= 0
                                )[0]
                            )
                        )
                    else:
                        accel_end_index.append(int(len(acceleration) - 1))

                if len(accel_start_index) != 0.0:
                    average_accels.append(
                        np.mean(acceleration[accel_start_index[i] : accel_end_index[i]])
                    )
                    max_accels.append(
                        np.max(acceleration[accel_start_index[i] : accel_end_index[i]])
                    )

            # Start of the deceleration index for loop
            for i in range(len(decel_start_index)):
                if i != len(decel_start_index) - 1:
                    decel_end_index.append(
                        int(
                            decel_start_index[i]
                            + np.argwhere(
                                acceleration[
                                    decel_start_index[i] : decel_start_index[i + 1]
                                ]
                                >= 0
                            )[0]
                        )
                    )
                else:
                    if any(np.argwhere(acceleration[decel_start_index[i] :] >= 0)):
                        decel_end_index.append(
                            int(
                                decel_start_index[i]
                                + np.argwhere(
                                    acceleration[decel_start_index[i] :] >= 0
                                )[0]
                            )
                        )
                    else:
                        decel_end_index.append(int(len(acceleration) - 1))
                if len(decel_start_index) != 0:
                    average_decels.append(
                        np.nanmean(
                            acceleration[decel_start_index[i] : decel_end_index[i]]
                        )
                    )
                    max_decels.append(
                        np.nanmax(
                            acceleration[decel_start_index[i] : decel_end_index[i]]
                        )
                    )

            # End of the deceleration index for loop
            self.total_number_of_acceleration_events = len(accel_start_index)
            self.total_number_of_deceleration_events = len(decel_start_index)
            if distance_total:
                self.acceleration_events_per_mile.pm = (
                    self.total_number_of_acceleration_events / distance_total
                )
                self.deceleration_events_per_mile.pm = (
                    self.total_number_of_deceleration_events / distance_total
                )

            # Calculate acceleration and decelerations stats for total cycle, all units in ft/s^2 or s
            self.max_acceleration.ftps2 = np.max(acceleration[acceleration > 0.0])
            self.max_deceleration.ftps2 = np.min(acceleration[acceleration < 0.0])
            self.average_acceleration.ftps2 = np.mean(acceleration[acceleration > 0.0])
            self.average_deceleration.ftps2 = np.mean(acceleration[acceleration < 0.0])
            self.median_acceleration.ftps2 = np.median(acceleration[acceleration > 0.0])
            self.median_deceleration.ftps2 = np.median(acceleration[acceleration < 0.0])
            self.std_acceleration.ftps2 = np.std(acceleration[acceleration > 0.0])
            self.std_deceleration.ftps2 = np.std(acceleration[acceleration < 0.0])
            self.var_acceleration.ftps2 = np.var(acceleration[acceleration > 0.0])
            self.var_deceleration.ftps2 = np.var(acceleration[acceleration < 0.0])
            self.acceleration_25th_percentile.ftps2 = np.percentile(
                acceleration[acceleration > 0.0], 25
            )
            self.deceleration_25th_percentile.ftps2 = np.percentile(
                acceleration[acceleration < 0.0], 25
            )
            self.acceleration_75th_percentile.ftps2 = np.percentile(
                acceleration[acceleration > 0.0], 75
            )
            self.deceleration_75th_percentile.ftps2 = np.percentile(
                acceleration[acceleration < 0.0], 75
            )
            self.acceleration_inter_quartile_range.ftps2 = np.percentile(
                acceleration[acceleration > 0.0], 75
            ) - np.percentile(acceleration[acceleration > 0.0], 25)
            self.deceleration_inter_quartile_range.ftps2 = np.percentile(
                acceleration[acceleration < 0.0], 75
            ) - np.percentile(acceleration[acceleration < 0.0], 25)
            self.acceleration_median_absolute_deviation.ftps2 = np.median(
                np.abs(acceleration[acceleration > 0.0])
                - np.median(acceleration[acceleration > 0.0])
            )
            self.deceleration_median_absolute_deviation.ftps2 = np.median(
                np.abs(acceleration[acceleration < 0.0])
                - np.median(acceleration[acceleration < 0.0])
            )
            speed_data_duration_hrs = num_samples / 3600.0
            absolute_time_duration_hrs = (
                cycle.time_s[-1] - cycle.time_s[0] + 1.0
            ) / 3600.0
            if num_samples:
                self.cumulative_acceleration_duration.s = (
                    len(cycle.time_s[acceleration > 0.0]) / num_samples
                )
                self.cumulative_deceleration_duration.s = (
                    len(cycle.time_s[acceleration < 0.0]) / num_samples
                )
            if speed_data_duration_hrs:
                self.cumulative_acceleration_cycle_duration_percent = (
                    self.cumulative_acceleration_duration.s
                    / speed_data_duration_hrs
                    * 100.0
                )
                self.cumulative_deceleration_cycle_duration_percent = (
                    self.cumulative_deceleration_duration.s
                    / speed_data_duration_hrs
                    * 100.0
                )

            accel_durations = (
                cycle.time_s[accel_end_index] - cycle.time_s[accel_start_index]
            )
            decel_durations = (
                cycle.time_s[decel_end_index] - cycle.time_s[decel_start_index]
            )
            self.absolute_time_cumulative_acceleration_duration.s = np.sum(
                accel_durations
            )
            self.absolute_time_cumulative_deceleration_duration.s = np.sum(
                decel_durations
            )
            if absolute_time_duration_hrs:
                self.absolute_time_cumulative_acceleration_cycle_duration_percent = (
                    self.absolute_time_cumulative_acceleration_duration.s
                    / (absolute_time_duration_hrs * 3600.0)
                ) * 100.0
                self.absolute_time_cumulative_deceleration_cycle_duration_percent = (
                    self.absolute_time_cumulative_deceleration_duration.s
                    / (absolute_time_duration_hrs * 3600.0)
                ) * 100.0
            # Calculate acceleration and deceleration stats for events
            self.average_acceleration_event_duration.s = np.mean(accel_durations)
            self.average_deceleration_event_duration.s = np.mean(decel_durations)
            self.min_acceleration_event_duration.s = np.min(accel_durations)
            self.min_deceleration_event_duration.s = np.min(decel_durations)
            self.max_acceleration_event_duration.s = np.max(accel_durations)
            self.max_deceleration_event_duration.s = np.max(decel_durations)
            self.std_acceleration_event_duration.s = np.std(accel_durations)
            self.std_deceleration_event_duration.s = np.std(decel_durations)
            self.var_acceleration_event_duration.s = np.var(accel_durations)
            self.var_deceleration_event_duration.s = np.var(decel_durations)
            self.median_acceleration_event_duration.s = np.median(accel_durations)
            self.median_deceleration_event_duration.s = np.median(decel_durations)
            self.acceleration_event_duration_25th_percentile.s = np.percentile(
                accel_durations, 25
            )
            self.deceleration_event_duration_25th_percentile.s = np.percentile(
                decel_durations, 25
            )
            self.acceleration_event_duration_75th_percentile.s = np.percentile(
                accel_durations, 75
            )
            self.deceleration_event_duration_75th_percentile.s = np.percentile(
                decel_durations, 75
            )
            self.acceleration_event_duration_inter_quartile_range.s = np.percentile(
                accel_durations, 75
            ) - np.percentile(accel_durations, 25)
            self.deceleration_event_duration_inter_quartile_range.s = np.percentile(
                decel_durations, 75
            ) - np.percentile(decel_durations, 25)
            self.acceleration_event_duration_median_absolute_deviation.s = np.median(
                np.abs(accel_durations) - np.median(accel_durations)
            )
            self.deceleration_event_duration_median_absolute_deviation.s = np.median(
                np.abs(decel_durations) - np.median(decel_durations)
            )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _StopsCountingStats(object):
        """
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
        """

        total_stops: int = 0
        stops_0_30: int = 0
        stops_30_60: int = 0
        stops_60_plus: int = 0
        stops_300_plus: int = 0
        stops_1800_plus: int = 0
        stops_3600_plus: int = 0
        stops_per_mile: int = 0
        average_stop_duration = Units.TimeUnits()
        min_stop_duration = Units.TimeUnits()
        max_stop_duration = Units.TimeUnits()
        median_stop_duration = Units.TimeUnits()
        mean_stop_duration = Units.TimeUnits()
        std_stop_duration = Units.TimeUnits()
        var_stop_duration = Units.TimeUnits()
        stop_duration_25th_percentile = Units.TimeUnits()
        stop_duration_75th_percentile = Units.TimeUnits()
        stop_duration_inter_quartile_range = Units.TimeUnits()
        stop_duration_median_absolute_deviation = Units.TimeUnits()

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """
            This constructor initializes the StopsCountingStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            stop_durations = []
            delta_time_s = np.diff(cycle.time_s)
            delta_speed = np.divide(
                np.diff(cycle.speed_mps),
                delta_time_s,
                out=np.zeros_like(np.diff(cycle.speed_mps)),
                where=delta_time_s != 0,
            )
            delta_square_speed = np.diff(delta_speed, append=0.0)
            acceleration = np.r_[
                0.0,
                np.divide(
                    delta_square_speed,
                    delta_time_s,
                    out=np.zeros_like(delta_square_speed),
                    where=delta_time_s != 0,
                )
                * gl.MPH_2_FTSS,
            ]
            stop_index_start = (
                np.argwhere(np.logical_and(acceleration < 0.0, cycle.speed_mps == 0.0))
                .flatten()
                .astype(int)
            )
            stop_index_end = []

            for i in range(len(stop_index_start)):
                if i != len(stop_index_start) - 1:
                    stop_index_end.append(
                        stop_index_start[i]
                        + np.argwhere(
                            cycle.speed_mps[
                                stop_index_start[i] : stop_index_start[i + 1]
                            ]
                        )[0]
                    )
                else:
                    if any(np.argwhere(cycle.speed_mps[stop_index_start[-1] + 1 : -1])):
                        stop_index_end.append(
                            np.argwhere(cycle.speed_mps[stop_index_start[-1] + 1 : -1])[
                                0
                            ]
                        )
                    else:
                        stop_index_end.append(len(cycle.speed_mps) - 1)
                stop_durations.append(
                    cycle.time_s[stop_index_end[i]] - cycle.time_s[stop_index_start[i]]
                )
            stop_durations = np.array([int(s) for s in stop_durations if int(s) > 0])
            if stop_durations:
                self.total_stops = len(stop_durations)
                self.stops_0_30 = len(
                    np.argwhere(
                        np.logical_and(stop_durations > 0.0, stop_durations <= 30.0)
                    )
                )
                self.stops_30_60 = len(
                    np.argwhere(
                        np.logical_and(stop_durations > 30.0, stop_durations <= 60.0)
                    )
                )
                self.stops_60_plus = len(np.nonzero(stop_durations > 60.0))
                self.stops_300_plus = len(np.nonzero(stop_durations > 300.0))
                self.stops_1800_plus = len(np.nonzero(stop_durations > 1800.0))
                self.stops_3600_plus = len(np.nonzero(stop_durations > 3600.0))
                delta_distance_m = cycle.speed_mps * np.diff(cycle.time_s, append=0)
                distance_total = sum(delta_distance_m)
                self.stops_per_mile = (
                    self.total_stops / distance_total if distance_total else 0
                )

                # Calculate the number of stops per mile for each of the cases above
                self.average_stop_duration.s = np.mean(stop_durations)
                self.min_stop_duration.s = np.min(stop_durations)
                self.max_stop_duration.s = np.max(stop_durations)
                self.median_stop_duration.s = np.median(stop_durations)
                self.mean_stop_duration.s = np.mean(stop_durations)
                self.std_stop_duration.s = np.std(stop_durations)
                self.var_stop_duration.s = np.var(stop_durations)
                self.stop_duration_25th_percentile.s = np.percentile(stop_durations, 25)
                self.stop_duration_75th_percentile.s = np.percentile(stop_durations, 75)
                self.stop_duration_inter_quartile_range.s = np.percentile(
                    stop_durations, 75
                ) - np.percentile(stop_durations, 25)
                self.stop_duration_median_absolute_deviation.s = np.median(
                    np.abs(stop_durations - np.median(stop_durations))
                )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _ElevationStats(object):
        """
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
        """

        max_elevation = Units.DistanceUnits()
        min_elevation = Units.DistanceUnits()
        mean_elevation = Units.DistanceUnits()
        median_elevation = Units.DistanceUnits()
        std_of_elevation = Units.DistanceUnits()
        var_of_elevation = Units.DistanceUnits()
        elevation_25th_percentile = Units.DistanceUnits()
        elevation_75th_percentile = Units.DistanceUnits()
        elevation_inter_quartile_range = Units.DistanceUnits()
        elevation_median_absolute_deviation = Units.DistanceUnits()
        delta_elevation = Units.DistanceUnits()
        delta_elevation_cumulative = Units.DistanceUnits()
        absolute_delta_elevation_cumulative = Units.DistanceUnits()
        total_elevation_gained = Units.DistanceUnits()
        total_elevation_lost = Units.DistanceUnits()
        average_absolute_elevation_rate_change = Units.SpeedUnits()
        max_climbing_rate = Units.SpeedUnits()
        average_climbing_rate = Units.SpeedUnits()
        median_climbing_rate = Units.SpeedUnits()
        max_descending_rate = Units.SpeedUnits()
        average_descending_rate = Units.SpeedUnits()
        median_descending_rate = Units.SpeedUnits()
        climbing_rate_25th_percentile = Units.SpeedUnits()
        descending_rate_25th_percentile = Units.SpeedUnits()
        climbing_rate_75th_percentile = Units.SpeedUnits()
        descending_rate_75th_percentile = Units.SpeedUnits()
        climbing_rate_inter_quartile_range = Units.SpeedUnits()
        descending_rate_inter_quartile_range = Units.SpeedUnits()
        climbing_rate_median_absolute_deviation = Units.SpeedUnits()
        descending_rate_median_absolute_deviation = Units.SpeedUnits()
        max_road_grade: float = 0
        min_road_grade: float = 0
        mean_road_grade: float = 0
        median_road_grade: float = 0
        std_of_road_grade: float = 0
        var_of_road_grade: float = 0
        road_grade_25th_percentile: float = 0
        road_grade_75th_percentile: float = 0
        road_grade_inter_quartile_range: float = 0
        road_grade_median_absolute_deviation: float = 0

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """This constructor initializes the ElevationStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            if not np.all(cycle.elevation_m == 0):
                delta_distance_m = cycle.speed_mps * np.diff(cycle.time_s, append=0)
                delta_elevation_m = np.diff(cycle.elevation_m, append=0)
                elevation_rate_mps = np.r_[
                    0.0, delta_distance_m / np.diff(cycle.time_s, append=0)
                ]
                road_grade = delta_elevation_m / (
                    delta_distance_m
                )  # calculate the road grade of the road section
                road_grade[delta_distance_m == 0] = 0

                self.max_elevation.m = np.max(cycle.elevation_m)
                self.min_elevation.m = np.min(cycle.elevation_m)
                self.mean_elevation.m = np.mean(cycle.elevation_m)
                self.median_elevation.m = np.median(cycle.elevation_m)
                self.std_of_elevation.m = np.std(cycle.elevation_m)
                self.var_of_elevation.m = np.var(cycle.elevation_m)
                self.elevation_25th_percentile.m = np.percentile(cycle.elevation_m, 25)
                self.elevation_75th_percentile.m = np.percentile(cycle.elevation_m, 75)
                self.elevation_inter_quartile_range.m = np.percentile(
                    cycle.elevation_m, 75
                ) - np.percentile(cycle.elevation_m, 25)
                self.elevation_median_absolute_deviation.m = np.median(
                    np.abs(cycle.elevation_m) - np.median(cycle.elevation_m)
                )

                self.delta_elevation.m = cycle.elevation_m[-1] - cycle.elevation_m[0]
                self.delta_elevation_cumulative.m = np.sum(delta_elevation_m)
                self.absolute_delta_elevation_cumulative.m = np.sum(
                    np.abs(delta_elevation_m)
                )
                self.total_elevation_gained.m = np.sum(
                    delta_elevation_m[delta_elevation_m > 0.0]
                )
                self.total_elevation_lost.m = np.sum(
                    delta_elevation_m[delta_elevation_m > 0.0]
                )

                self.average_absolute_elevation_rate_change.mps = np.mean(
                    np.abs(elevation_rate_mps)
                )
                self.max_climbing_rate.mps = np.max(
                    elevation_rate_mps[elevation_rate_mps > 0]
                )
                self.average_climbing_rate.mps = np.mean(
                    elevation_rate_mps[elevation_rate_mps > 0]
                )
                self.median_climbing_rate.mps = np.median(
                    elevation_rate_mps[elevation_rate_mps > 0]
                )
                self.max_descending_rate.mps = np.max(
                    elevation_rate_mps[elevation_rate_mps < 0]
                )
                self.average_descending_rate.mps = np.mean(
                    elevation_rate_mps[elevation_rate_mps < 0]
                )
                self.median_descending_rate.mps = np.median(
                    elevation_rate_mps[elevation_rate_mps < 0]
                )
                self.climbing_rate_25th_percentile.mps = np.percentile(
                    elevation_rate_mps[elevation_rate_mps > 0], 25
                )
                self.descending_rate_25th_percentile.mps = np.percentile(
                    elevation_rate_mps[elevation_rate_mps < 0], 25
                )
                self.climbing_rate_75th_percentile.mps = np.percentile(
                    elevation_rate_mps[elevation_rate_mps > 0], 75
                )
                self.descending_rate_75th_percentile.mps = np.percentile(
                    elevation_rate_mps[elevation_rate_mps < 0], 75
                )
                self.climbing_rate_inter_quartile_range.mps = np.percentile(
                    elevation_rate_mps[elevation_rate_mps > 0], 75
                ) - np.percentile(elevation_rate_mps[elevation_rate_mps > 0], 25)
                self.descending_rate_inter_quartile_range.mps = np.percentile(
                    elevation_rate_mps[elevation_rate_mps < 0], 75
                ) - np.percentile(elevation_rate_mps[elevation_rate_mps < 0], 25)
                self.climbing_rate_median_absolute_deviation.mps = np.median(
                    np.abs(elevation_rate_mps[elevation_rate_mps > 0])
                    - np.median(elevation_rate_mps[elevation_rate_mps > 0])
                )
                self.descending_rate_median_absolute_deviation.mps = np.median(
                    np.abs(elevation_rate_mps[elevation_rate_mps < 0])
                    - np.median(elevation_rate_mps[elevation_rate_mps < 0])
                )

                self.max_road_grade = np.max(road_grade)
                self.min_road_grade = np.min(road_grade)
                self.mean_road_grade = np.mean(road_grade)
                self.median_road_grade = np.median(road_grade)
                self.std_of_road_grade = np.std(road_grade)
                self.var_of_road_grade = np.var(road_grade)
                self.road_grade_25th_percentile = np.percentile(road_grade, 25)
                self.road_grade_75th_percentile = np.percentile(road_grade, 75)
                self.road_grade_inter_quartile_range = np.percentile(
                    road_grade, 75
                ) - np.percentile(road_grade, 25)
                self.road_grade_median_absolute_deviation = np.median(
                    np.abs(road_grade - np.median(road_grade))
                )

                units_inner_class_types = Units.list_inner_classes(Units)
                for key in dir(self):
                    if type(self.__getattribute__(key)) in units_inner_class_types:
                        self.__getattribute__(key).convert_units()

    class _PowerDensityStats(object):
        """
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

        """

        maximum_kinetic_power_density_demand = Units.PowerDensityUnits()
        total_kinetic_power_density_demand = Units.PowerDensityUnits()
        average_kinetic_power_density_demand = Units.PowerDensityUnits()
        variance_kinetic_power_density_demand = Units.PowerDensityUnits()
        standard_deivation_kinetic_power_density_demand = Units.PowerDensityUnits()
        maximum_kinetic_power_density_regen = Units.PowerDensityUnits()
        total_kinetic_power_density_regen = Units.PowerDensityUnits()
        average_kinetic_power_density_regen = Units.PowerDensityUnits()
        variance_kinetic_power_density_regen = Units.PowerDensityUnits()
        standard_deivation_kinetic_power_density_regen = Units.PowerDensityUnits()
        maximum_potential_power_density_demand = Units.PowerDensityUnits()
        total_potential_power_density_demand = Units.PowerDensityUnits()
        average_potential_power_density_demand = Units.PowerDensityUnits()
        variance_potential_power_density_demand = Units.PowerDensityUnits()
        standard_deivation_potential_power_density_demand = Units.PowerDensityUnits()
        maximum_potential_power_density_regen = Units.PowerDensityUnits()
        total_potential_power_density_regen = Units.PowerDensityUnits()
        average_potential_power_density_regen = Units.PowerDensityUnits()
        variance_potential_power_density_regen = Units.PowerDensityUnits()
        standard_deivation_potential_power_density_regen = Units.PowerDensityUnits()
        maximum_aerodynamic_power_density_demand = Units.PowerDensityUnits()
        total_aerodynamic_power_density_demand = Units.PowerDensityUnits()
        average_aerodynamic_power_density_demand = Units.PowerDensityUnits()
        variance_aerodynamic_power_density_demand = Units.PowerDensityUnits()
        standard_deivation_aerodynamic_power_density_demand = Units.PowerDensityUnits()
        maximum_aerodynamic_power_density_regen = Units.PowerDensityUnits()
        total_aerodynamic_power_density_regen = Units.PowerDensityUnits()
        average_aerodynamic_power_density_regen = Units.PowerDensityUnits()
        variance_aerodynamic_power_density_regen = Units.PowerDensityUnits()
        standard_deivation_aerodynamic_power_density_regen = Units.PowerDensityUnits()
        maximum_rolling_power_density_demand = Units.PowerDensityUnits()
        total_rolling_power_density_demand = Units.PowerDensityUnits()
        average_rolling_power_density_demand = Units.PowerDensityUnits()
        variance_rolling_power_density_demand = Units.PowerDensityUnits()
        standard_deivation_rolling_power_density_demand = Units.PowerDensityUnits()
        maximum_rolling_power_density_regen = Units.PowerDensityUnits()
        total_rolling_power_density_regen = Units.PowerDensityUnits()
        average_rolling_power_density_regen = Units.PowerDensityUnits()
        variance_rolling_power_density_regen = Units.PowerDensityUnits()
        standard_deivation_rolling_power_density_regen = Units.PowerDensityUnits()

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """This constructor initializes the PowerDensityStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            vbar = ((cycle.speed_mps[0:-1]) + (cycle.speed_mps[1:])) / 2.0
            kinetic_power_density = (
                cycle.speed_mps
                * np.diff(cycle.speed_mps, append=0)
                / np.diff(cycle.time_s, append=1)
            )

            v3bar = (
                (cycle.speed_mps[1:]) ** 3.0
                + ((cycle.speed_mps[1:]) ** 2.0) * (cycle.speed_mps[0:-1])
                + (cycle.speed_mps[1:]) * ((cycle.speed_mps[0:-1]) ** 2.0)
                + (cycle.speed_mps[0:-1]) ** 3.0
            ) / 4.0
            aerodynamic_power_density = v3bar / 2.0
            rolling_power_density = vbar * gl.acceleration_g_mps2
            if not np.all(cycle.elevation_m == 0):
                potential_power_density = gl.acceleration_g_mps2 * np.diff(
                    cycle.elevation_m
                )

            if len(kinetic_power_density[kinetic_power_density < 0]):
                # Perform Kinetic Power Consumption Calculations
                self.maximum_kinetic_power_density_demand.m2ps3 = np.max(
                    kinetic_power_density
                )
                self.total_kinetic_power_density_demand.m2ps3 = np.sum(
                    kinetic_power_density[kinetic_power_density > 0]
                )
                self.average_kinetic_power_density_demand.m2ps3 = np.mean(
                    kinetic_power_density[kinetic_power_density > 0]
                )
                self.variance_kinetic_power_density_demand.m2ps3 = np.var(
                    kinetic_power_density[kinetic_power_density > 0]
                )
                self.standard_deivation_kinetic_power_density_demand.m2ps3 = np.std(
                    kinetic_power_density[kinetic_power_density > 0]
                )

                # Perform Kinetic Power Regeneration Calculations
                self.maximum_kinetic_power_density_regen.m2ps3 = np.min(
                    kinetic_power_density
                )
                self.total_kinetic_power_density_regen.m2ps3 = np.sum(
                    kinetic_power_density[kinetic_power_density < 0]
                )
                self.average_kinetic_power_density_regen.m2ps3 = np.mean(
                    kinetic_power_density[kinetic_power_density < 0]
                )
                self.variance_kinetic_power_density_regen.m2ps3 = np.var(
                    kinetic_power_density[kinetic_power_density < 0]
                )
                self.standard_deivation_kinetic_power_density_regen.m2ps3 = np.std(
                    kinetic_power_density[kinetic_power_density < 0]
                )

            # Perform Potential Power Consumption Calculations
            if not np.all(cycle.elevation_m == 0):
                self.maximum_potential_power_density_demand.m2ps3 = np.max(
                    potential_power_density
                )
                self.total_potential_power_density_demand.m2ps3 = np.sum(
                    potential_power_density[potential_power_density > 0]
                )
                self.average_potential_power_density_demand.m2ps3 = np.mean(
                    potential_power_density[potential_power_density > 0]
                )
                self.variance_potential_power_density_demand.m2ps3 = np.var(
                    potential_power_density[potential_power_density > 0]
                )
                self.standard_deivation_potential_power_density_demand.m2ps3 = np.std(
                    potential_power_density[potential_power_density > 0]
                )

                # Perform Potential Power Regeneration Calculations
                self.maximum_potential_power_density_regen.m2ps3 = np.min(
                    potential_power_density
                )
                self.total_potential_power_density_regen.m2ps3 = np.sum(
                    potential_power_density[potential_power_density < 0]
                )
                self.average_potential_power_density_regen.m2ps3 = np.mean(
                    potential_power_density[potential_power_density < 0]
                )
                self.variance_potential_power_density_regen.m2ps3 = np.var(
                    potential_power_density[potential_power_density < 0]
                )
                self.standard_deivation_potential_power_density_regen.m2ps3 = np.std(
                    potential_power_density[potential_power_density < 0]
                )
            if len(aerodynamic_power_density[aerodynamic_power_density < 0]):
                # Perform Aerodynamic Power Consumption Calculations
                self.maximum_aerodynamic_power_density_demand.m2ps3 = np.max(
                    aerodynamic_power_density
                )
                self.total_aerodynamic_power_density_demand.m2ps3 = np.sum(
                    aerodynamic_power_density[aerodynamic_power_density > 0]
                )
                self.average_aerodynamic_power_density_demand.m2ps3 = np.mean(
                    aerodynamic_power_density[aerodynamic_power_density > 0]
                )
                self.variance_aerodynamic_power_density_demand.m2ps3 = np.var(
                    aerodynamic_power_density[aerodynamic_power_density > 0]
                )
                self.standard_deivation_aerodynamic_power_density_demand.m2ps3 = np.std(
                    aerodynamic_power_density[aerodynamic_power_density > 0]
                )

                # Perform Aerdynamic Power Regeneration Calculations
                self.maximum_aerodynamic_power_density_regen.m2ps3 = np.min(
                    aerodynamic_power_density
                )
                self.total_aerodynamic_power_density_regen.m2ps3 = np.sum(
                    aerodynamic_power_density[aerodynamic_power_density < 0]
                )
                self.average_aerodynamic_power_density_regen.m2ps3 = np.mean(
                    aerodynamic_power_density[aerodynamic_power_density < 0]
                )
                self.variance_aerodynamic_power_density_regen.m2ps3 = np.var(
                    aerodynamic_power_density[aerodynamic_power_density < 0]
                )
                self.standard_deivation_aerodynamic_power_density_regen.m2ps3 = np.std(
                    aerodynamic_power_density[aerodynamic_power_density < 0]
                )
            if len(rolling_power_density[rolling_power_density < 0]):
                # Perform Rolling Power Consumption Calculations
                self.maximum_rolling_power_density_demand.m2ps3 = np.max(
                    rolling_power_density
                )
                self.total_rolling_power_density_demand.m2ps3 = np.sum(
                    rolling_power_density[rolling_power_density > 0]
                )
                self.average_rolling_power_density_demand.m2ps3 = np.mean(
                    rolling_power_density[rolling_power_density > 0]
                )
                self.variance_rolling_power_density_demand.m2ps3 = np.var(
                    rolling_power_density[rolling_power_density > 0]
                )
                self.standard_deivation_rolling_power_density_demand.m2ps3 = np.std(
                    rolling_power_density[rolling_power_density > 0]
                )

                # Perform Rolling Power Regeneration Calculations
                self.maximum_rolling_power_density_regen.m2ps3 = np.min(
                    rolling_power_density
                )
                self.total_rolling_power_density_regen.m2ps3 = np.sum(
                    rolling_power_density[rolling_power_density < 0]
                )
                self.average_rolling_power_density_regen.m2ps3 = np.mean(
                    rolling_power_density[rolling_power_density < 0]
                )
                self.variance_rolling_power_density_regen.m2ps3 = np.var(
                    rolling_power_density[rolling_power_density < 0]
                )
                self.standard_deivation_rolling_power_density_regen.m2ps3 = np.std(
                    rolling_power_density[rolling_power_density < 0]
                )

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _EnergyDensityStats(object):
        """
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

        """

        maximum_instantanteous_potential_energy_density = Units.EnergyDensityUnits()
        average_instantanteous_potential_energy_density = Units.EnergyDensityUnits()
        cumulative_instanteous_potential_energy_density = Units.EnergyDensityUnits()
        maximum_instantanteous_kinetic_energy_density = Units.EnergyDensityUnits()
        average_instantanteous_kinetic_energy_density = Units.EnergyDensityUnits()
        cumulative_instanteous_kinetic_energy_density = Units.EnergyDensityUnits()
        maximum_instantanteous_aerodynamic_energy_density = Units.EnergyDensityUnits()
        average_instantanteous_aerodynamic_energy_density = Units.EnergyDensityUnits()
        cumulative_instanteous_aerodynamic_energy_density = Units.EnergyDensityUnits()
        maximum_instantanteous_rolling_energy_density = Units.EnergyDensityUnits()
        average_instantanteous_rolling_energy_density = Units.EnergyDensityUnits()
        cumulative_instanteous_rolling_energy_density = Units.EnergyDensityUnits()

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """This constructor initializes the EnergyDensityStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            if not np.all(cycle.elevation_m == 0):
                iped = gl.acceleration_g_mps2 * cycle.elevation_m
                self.maximum_instantanteous_potential_energy_density.Jpkg = np.max(iped)
                self.average_instantanteous_potential_energy_density.Jpkg = np.mean(
                    iped
                )
                self.cumulative_instanteous_potential_energy_density.Jpkg = np.sum(iped)

            iked = 0.5 * (cycle.speed_mps) ** 2.0  # units in J/kg
            self.maximum_instantanteous_kinetic_energy_density.Jpkg = np.max(iked)
            self.average_instantanteous_kinetic_energy_density.Jpkg = np.mean(iked)
            self.cumulative_instanteous_kinetic_energy_density.Jpkg = np.sum(iked)

            iaed = 0.5 * (cycle.speed_mps) ** 3.0  # units in J/kg/rho/Cd/FA
            self.maximum_instantanteous_aerodynamic_energy_density.Jpkg = np.max(iaed)
            self.average_instantanteous_aerodynamic_energy_density.Jpkg = np.mean(iaed)
            self.cumulative_instanteous_aerodynamic_energy_density.Jpkg = np.sum(iaed)

            # Instantanteous Rolling Energy Calculations
            ired = gl.acceleration_g_mps2 * (cycle.speed_mps)  # units in J/kg/RRCo
            self.maximum_instantanteous_rolling_energy_density.Jpkg = np.max(ired)
            self.average_instantanteous_rolling_energy_density.Jpkg = np.mean(ired)
            self.cumulative_instanteous_rolling_energy_density.Jpkg = np.sum(ired)

    class _KineticIntensityStats(object):
        """
        This subclass contains kinetic intensity related calculations

            - characteristic_acceleration
            - characteristic_deceleration
            - aerodynamic_speed
            - kinetic_intensity


        """

        characteristic_acceleration = Units.AccelerationUnits()
        characteristic_deceleration = Units.AccelerationUnits()
        aerodynamic_speed = Units.SpeedUnits()
        kinetic_intensity = Units.PerDistanceUnits()

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """This constructor initializes the KineticIntensityStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """

            if not np.all(cycle.elevation_m == 0):
                a = 0.5 * (
                    (cycle.speed_mps[1:]) ** 2.0 - (cycle.speed_mps[0:-1]) ** 2.0
                ) + gl.acceleration_g_mps2 * (
                    cycle.elevation_m[1:] - cycle.elevation_m[0:-1]
                )
            else:
                a = 0.5 * (
                    (cycle.speed_mps[1:]) ** 2.0 - (cycle.speed_mps[0:-1]) ** 2.0
                )
            v3bar = (
                (cycle.speed_mps[1:]) ** 3.0
                + ((cycle.speed_mps[1:]) ** 2.0) * (cycle.speed_mps[0:-1])
                + (cycle.speed_mps[1:]) * ((cycle.speed_mps[0:-1]) ** 2.0)
                + (cycle.speed_mps[0:-1]) ** 3.0
            ) / 4.0
            delta_distance_m = cycle.speed_mps * np.diff(cycle.time_s, append=0)

            distance_total = np.sum(delta_distance_m)
            if distance_total:
                self.characteristic_acceleration.mps2 = np.sum(a[a > 0.0]) / (
                    distance_total
                )  # units m/s^2
                self.characteristic_deceleration.mps2 = np.sum(a[a < 0.0]) / (
                    distance_total
                )
                self.aerodynamic_speed.mps = np.sqrt(
                    (
                        np.sum(
                            v3bar
                            * (cycle.time_s[1:] - cycle.time_s[0:-1])
                            / (distance_total)
                        )
                        if distance_total != 0
                        else 0
                    )
                )  # units m/s
                self.kinetic_intensity.pm = (
                    self.characteristic_acceleration.mps2
                    / self.aerodynamic_speed.mps**2.0
                ) * 1000.0

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()

    class _DistanceStats(object):
        """
        This subclass calculates total distance.
            - distance_total

        """

        distance_total = Units.DistanceUnits()

        def __init__(self, cycle: Cycle, units_system: str = "SI"):
            """This constructor initializes the DistanceStats calculations

            Args:
                cycle (Cycle): Input Cycle object
                units (str, optional): Units system desired between ['SI', 'Imperial'] . Defaults to "SI".
            """
            delta_distance_m = cycle.speed_mps * np.diff(cycle.time_s, append=0)
            self.distance_total.m = np.sum(delta_distance_m)

            units_inner_class_types = Units.list_inner_classes(Units)
            for key in dir(self):
                if type(self.__getattribute__(key)) in units_inner_class_types:
                    self.__getattribute__(key).convert_units()
