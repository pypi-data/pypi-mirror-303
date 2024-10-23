# %%


##################################################
# Unit-System Independent
##################################################
# * Time
HR_2_S = 3600  # hours to seconds
HR_2_MIN = 60  # hours to minutes

S_2_HR = 1 / 3600  # seconds to hours
S_2_MIN = 1 / 60  # Seconds to minutes

MIN_2_HR = 1 / 60  # minutes to hours
MIN_2_S = 60  # minutes to seconds


def minutes_to_seconds(s):
    return s * 60


##################################################
# Conversions to Metric Units
##################################################
# * Distance
# US To Metric
FT_2_M = 0.3048  # feet to meters
MI_2_KM = 1.60934  # mile to kilometers
# Metric to Metric
KM_2_M = 1e3  # kilometer to meter
KM_2_CM = 1e5  # kilometer to centimeter
KM_2_MM = 1e6  # kilometer to millimeter
M_2_KM = 1e-3  # meter to kilometer
CM_2_KM = 1e-5  # centimeter to kilometer
MM_2_KM = 1e-6  # millimeter to kilometer

# * Mass
LB_2_KG = 0.453592  # Pound to kilogram
# Metric to Metric
G_2_KG = 1e-3
KG_2_G = 1e3

# * Speed
# US To Metric
MPH_2_KPH = 1.60934  # Mile per Hour to Kilometer per Hour
MPH_2_MPS = 1.60934 / 3.6  # Mile per Hour to Meter per Second
FPS_2_KPH = 1.09728  # Feet per second to Kilometer per Hour
FPS_2_MPS = 0.3048  # Feet per second to Meter per Second
# Metric to Metric
KPH_2_MPS = 1 / 3.6

MPH_2_FTSS = 1.466667
# * Volume3
# US To Metric
# Metric to Metric
M3_2_L = 1e3  # Cubic meter to liter
L_2_M3 = 1e-3  # Liter to cubic meter
GAL_2_L = 3.78541  # Gallon to Liter
GAL_2_M3 = 0.00378541  # Gallon to cubic meter

# * Energy
J_2_KWH = 1 / (3.6e6)
KWH_2_J = 3.6e6

##################################################
# Conversions to US Standard Units
##################################################
# * Distance
# Metric to US
M_2_FT = 1 / 0.3048  # Meters to Feet
KM_2_MI = 0.621371  # Kilometer to miles
# US to US
FT_2_MI = 5280  # Feet to miles
FT_2_IN = 12  # Feet to inches

# * Mass
# Metric to US
KG_2_LB = 2.20462  # Kilogram to pound
# US to US

# * Speed
# Metric to US
KPH_2_MPH = 0.621371  # Kilometer per hour to mile per hour
MPH_2_FPS = 1.466667  # Mile per hour to feet per second
# US to US

# * Volume
# Metric to US
L_2_GAL = 1 / 3.78541  # Liter to gallon
L_PER_GAL = 3.78541
# US to US

acceleration_g_mps2 = 9.8

KWH_PER_GAL_DIESEL = 37.037037
