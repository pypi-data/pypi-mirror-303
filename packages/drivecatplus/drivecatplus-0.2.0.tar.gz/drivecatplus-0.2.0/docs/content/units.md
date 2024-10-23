# Table of Contents

* [src/drivecatplus/units](#src/drivecatplus/units)
  * [Units](#src/drivecatplus/units.Units)
    * [\_\_init\_\_](#src/drivecatplus/units.Units.__init__)
    * [DistanceUnits](#src/drivecatplus/units.Units.DistanceUnits)
    * [TimeUnits](#src/drivecatplus/units.Units.TimeUnits)
    * [FrequencyUnits](#src/drivecatplus/units.Units.FrequencyUnits)
    * [SpeedUnits](#src/drivecatplus/units.Units.SpeedUnits)
    * [AccelerationUnits](#src/drivecatplus/units.Units.AccelerationUnits)
    * [PowerDensityUnits](#src/drivecatplus/units.Units.PowerDensityUnits)
    * [EnergyDensityUnits](#src/drivecatplus/units.Units.EnergyDensityUnits)
    * [PerDistanceUnits](#src/drivecatplus/units.Units.PerDistanceUnits)
    * [list\_inner\_classes](#src/drivecatplus/units.Units.list_inner_classes)

<a id="src/drivecatplus/units"></a>

# src/drivecatplus/units

<a id="src/drivecatplus/units.Units"></a>

## Units Objects

```python
class Units(object)
```

This class contains all Units subclasses
- DistanceUnits
- TimeUnits
- FrequencyUnits
- SpeedUnits
- AccelerationUnits
- PowerDensityUnits
- EnergyDensityUnits
- PerDistanceUnits

<a id="src/drivecatplus/units.Units.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes Units systems

<a id="src/drivecatplus/units.Units.DistanceUnits"></a>

## DistanceUnits Objects

```python
class DistanceUnits(object)
```

This subclass contains distance units
- m
- km
- mi

<a id="src/drivecatplus/units.Units.DistanceUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes m

<a id="src/drivecatplus/units.Units.DistanceUnits.convert_units"></a>

#### convert\_units

```python
def convert_units() -> None
```

This method converts DistanceUnits to km and mi

<a id="src/drivecatplus/units.Units.TimeUnits"></a>

## TimeUnits Objects

```python
class TimeUnits(object)
```

This subclass contains Time units
- s
- min
- h

<a id="src/drivecatplus/units.Units.TimeUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes s, min, and h

<a id="src/drivecatplus/units.Units.TimeUnits.convert_units"></a>

#### convert\_units

```python
def convert_units() -> None
```

This method converts s to min and hr

<a id="src/drivecatplus/units.Units.FrequencyUnits"></a>

## FrequencyUnits Objects

```python
class FrequencyUnits(object)
```

This subclass contains frequency units
- Hz

<a id="src/drivecatplus/units.Units.FrequencyUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes FrequencyUnits

<a id="src/drivecatplus/units.Units.FrequencyUnits.convert_units"></a>

#### convert\_units

```python
def convert_units() -> None
```

This method converts units. Currently no conversions

<a id="src/drivecatplus/units.Units.SpeedUnits"></a>

## SpeedUnits Objects

```python
class SpeedUnits(object)
```

This subclass contains Speed units
- mps
- kmph
- mph

<a id="src/drivecatplus/units.Units.SpeedUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes mps, kmph, and mph

<a id="src/drivecatplus/units.Units.SpeedUnits.convert_units"></a>

#### convert\_units

```python
def convert_units() -> None
```

This method converts mps to kmph and mph

<a id="src/drivecatplus/units.Units.AccelerationUnits"></a>

## AccelerationUnits Objects

```python
class AccelerationUnits(object)
```

This subclass contains acceleration units
- mps2
- kmph2
- ftps2

<a id="src/drivecatplus/units.Units.AccelerationUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes mps2

<a id="src/drivecatplus/units.Units.PowerDensityUnits"></a>

## PowerDensityUnits Objects

```python
class PowerDensityUnits(object)
```

This subclass contains power density units
- m2ps3

<a id="src/drivecatplus/units.Units.PowerDensityUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes PowerDensityUnits

<a id="src/drivecatplus/units.Units.PowerDensityUnits.convert_units"></a>

#### convert\_units

```python
def convert_units() -> None
```

This method converts m2ps3. Currently no conversions

<a id="src/drivecatplus/units.Units.EnergyDensityUnits"></a>

## EnergyDensityUnits Objects

```python
class EnergyDensityUnits(object)
```

This subclass contains energy density units
- Jpkg

<a id="src/drivecatplus/units.Units.EnergyDensityUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes EnergyDensityUnits

<a id="src/drivecatplus/units.Units.EnergyDensityUnits.convert_units"></a>

#### convert\_units

```python
def convert_units() -> None
```

This constructor converts EnergyDensityUnits. Currently no conversions

<a id="src/drivecatplus/units.Units.PerDistanceUnits"></a>

## PerDistanceUnits Objects

```python
class PerDistanceUnits(object)
```

This subclass contains per distance units
- pm
- pkm
- pmi

<a id="src/drivecatplus/units.Units.PerDistanceUnits.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

This constructor initializes PerDistanceUnits

<a id="src/drivecatplus/units.Units.PerDistanceUnits.convert_units"></a>

#### convert\_units

```python
def convert_units() -> None
```

This method converts pm to pkm and pmi

<a id="src/drivecatplus/units.Units.list_inner_classes"></a>

#### list\_inner\_classes

```python
def list_inner_classes()
```

This method returns all Units subclasses as a list

**Returns**:

- `list` - list of Units subclasses and their arguments

