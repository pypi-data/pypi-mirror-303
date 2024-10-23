# %%
from time import gmtime, strftime
from drivecatplus.drivestats import DriveStats, Cycle
from pathlib import Path

# drivecycle_file = Path(__file__).parents[1] / "resources" / "demo_cycle_without_elevation.csv"
drivecycle_file = "/Users/hpanneer/Documents/GitHub/EPA-T3CO/tco_inputs/medoid_cycle_9/cyccluster_cluster_9_medoid_cycle.csv"
outputfilepath = "/Users/hpanneer/Documents/GitHub/drivecatplus/src/results/"
cycle1 = Cycle.from_file(
    str(drivecycle_file), var_name_dict={"speed_mps": "mps", "time_s": "time_s"}
)
stats = DriveStats(cycle1)
print(f"Average Speed kmph: {stats.total_speed_stats.total_average_speed.kmph}")
ts = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
outputfile = outputfilepath + "drivecat_plus_results_" + ts + ".csv"
stats.export_to_file(outputfile, units_system="SI", include_prefix=False)
# print(f"Drivecatplus results: {outputfile}")

# %%
