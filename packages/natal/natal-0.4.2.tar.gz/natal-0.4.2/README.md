# Natal

[![ci-badge]][ci-url] [![pypi-badge]][pypi-url] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

> create Natal Chart with ease

## Features

- SVG natal chart generation in pure python
    - light, dark or auto theme based on user's computer settings
    - printing friendly mono theme
- highly configurable with yaml file
    - all planets, asteroids, vertices can be enabled / disabled
    - orbs for each apect
    - light and dark theme color definitions
    - chart stroke, opacity, font, spacing between planets ...etc
- high precision astrological data with [Swiss Ephemeris]
- timezone, latitude and longitude database from [GeoNames]
    - auto aware of daylight saving for given time and location
- natal chart data statistics
    - element, quality, and polarity counts
    - planets in each houses
    - aspect pair counts
    - aspects cross reference table
- thoroughly tested with `pytest`

## Sample Charts

- default dark theme

<img src="https://bit.ly/4eufbuW" width=600/>

- default light theme

<img src="https://bit.ly/3MT86Zl" width=600/>

- mono theme

<img src="https://bit.ly/3ZygoNw" width=600/>

[Swiss Ephemeris]: https://www.astro.com/swisseph/swephinfo_e.htm
[GeoNames]: https://www.geonames.org

## Quick Start

- installation

`pip install natal`

- generate a chart

```python
from natal import Data, Chart

# create chart data object
mimi = Data(
  name = "MiMi",
  city = "Taipei",
  dt = "1980-04-20 14:30"
)

# return natal chart in SVG string
Chart(mimi, width=600).svg

# create transit data object
current = Data(
  name = "Current",
  city = "Taipei",
  dt = datetime.now()
)

# create a transit chart
transit_chart = Chart(
    data1=mimi, 
    data2=current, 
    width=600
)

# view the composite chart in jupyter notebook
from IPython.display import HTML

HTML(transit_chart.svg)
```

following SVG chart will be produced:

<img src="https://bit.ly/3MX7H8e" width=600/>

## Data Object

```python
## -- retrieve natal chart properties -- ##

mimi.planets     # list[Planet]
mimi.houses      # list[House]
mimi.extras      # list[Extra]
mimi.vertices    # list[Vertex]
mimi.signs       # list[Sign]
mimi.aspects     # list[Aspect]
mimi.quadrants   # list[list[Aspectable]]

# Planet object 
sun = mimi.planets[0]

sun.degree # 30.33039116987769
sun.normalized_degree # 230.62043431588035 # degree relative to Asc
sun.color # fire
sun.speed # 0.9761994105153413
sun.retro # False
sun.dms # 00°19'
sun.signed_dms # 00°♉19'
sun.signed_deg # 0
sun.sign.name # taurus
sun.sign.symbol # ♉
sun.sign.value # 2
sun.sign.color # earth
sun.sign.ruler # venus
sun.sign.classic_ruler # venus
sun.sign.element # earth
sun.sign.quality # fixed
sun.sign.polarity # negative

# Aspect object
aspect = mimi.aspects[0]

aspect.body1 # sun Planet obj 
aspect.body2 # mars Planet obj
aspect.aspect_member # AspectMember(name='trine', symbol='△', value=120, color='air')
aspect.applying # False
aspect.orb # 3.3424
```

## Stats

- statistics of Data object in tabular form

```python
from natal import Data, Stats

mimi = Data(
    name = "MiMi",
    city = "Taipei",
    dt = "1980-04-20 14:30"
)

transit = Data(
    name = "Transit",
    city = "Taipei",
    dt = "2024-10-10 12:00"
)

stats = Stats(data1=mimi, data2=transit)

print(stats.full_report("ascii"))
```

- following ascii report will be created
- Note: fonts with double space char support is suggested for better ascii table display eg. `Sarasa Mono TC`

```text
# Element Distribution (MiMi)

| element   |  count  | bodies                                        |
|-----------|---------|-----------------------------------------------|
| earth     |    4    | sun ♉, jupiter ♍, saturn ♍, asc ♍         |
| water     |    2    | moon ♋, uranus ♏                            |
| fire      |    4    | mercury ♈, mars ♌, neptune ♐, mean_node ♌ |
| air       |    3    | venus ♊, pluto ♎, mc ♊                     |


# Quality Distribution (MiMi)

| quality   |  count  | bodies                                                     |
|-----------|---------|------------------------------------------------------------|
| fixed     |    4    | sun ♉, mars ♌, uranus ♏, mean_node ♌                   |
| cardinal  |    3    | moon ♋, mercury ♈, pluto ♎                              |
| mutable   |    6    | venus ♊, jupiter ♍, saturn ♍, neptune ♐, asc ♍, mc ♊ |


# Polarity Distribution (MiMi)

| polarity   |  count  | bodies                                                                   |
|------------|---------|--------------------------------------------------------------------------|
| negative   |    6    | sun ♉, moon ♋, jupiter ♍, saturn ♍, uranus ♏, asc ♍                |
| positive   |    7    | mercury ♈, venus ♊, mars ♌, neptune ♐, pluto ♎, mean_node ♌, mc ♊ |


# Celestial Bodies (MiMi)

| body      | sign      |  house  |
|-----------|-----------|---------|
| sun       | 00°♉19'  |    8    |
| moon      | 08°♋29'  |   10    |
| mercury   | 08°♈28'  |    8    |
| venus     | 15°♊12'  |   10    |
| mars      | 26°♌59'  |   12    |
| jupiter   | 00°♍17'℞ |   12    |
| saturn    | 21°♍03'℞ |    1    |
| uranus    | 24°♏31'℞ |    3    |
| neptune   | 22°♐29'℞ |    4    |
| pluto     | 20°♎06'℞ |    2    |
| mean_node | 26°♌03'℞ |   12    |
| asc       | 09°♍42'  |    1    |
| mc        | 09°♊13'  |   10    |


# Houses (MiMi)

|  house  | sign     | ruler   | ruler sign   |  ruler house  |
|---------|----------|---------|--------------|---------------|
|    1    | 09°♍41' | mercury | ♈           |       8       |
|    2    | 07°♎13' | venus   | ♊           |      10       |
|    3    | 07°♏38' | pluto   | ♎           |       2       |
|    4    | 09°♐13' | jupiter | ♍           |      12       |
|    5    | 10°♑25' | saturn  | ♍           |       1       |
|    6    | 10°♒44' | uranus  | ♏           |       3       |
|    7    | 09°♓41' | neptune | ♐           |       4       |
|    8    | 07°♈13' | mars    | ♌           |      12       |
|    9    | 07°♉38' | venus   | ♊           |      10       |
|   10    | 09°♊13' | mercury | ♈           |       8       |
|   11    | 10°♋25' | moon    | ♋           |      10       |
|   12    | 10°♌44' | sun     | ♉           |       8       |


# Quadrants (MiMi)

| quadrant   |  count  | bodies                                |
|------------|---------|---------------------------------------|
| 1st ◵      |    3    | saturn, uranus, pluto                 |
| 2nd ◶      |    1    | neptune                               |
| 3rd ◷      |    2    | sun, mercury                          |
| 4th ◴      |    5    | moon, venus, mars, jupiter, mean_node |


# Hemispheres (MiMi)

| hemisphere   |  count  | bodies                                                       |
|--------------|---------|--------------------------------------------------------------|
| ←            |    8    | saturn, uranus, pluto, moon, venus, mars, jupiter, mean_node |
| →            |    3    | neptune, sun, mercury                                        |
| ↑            |    7    | sun, mercury, moon, venus, mars, jupiter, mean_node          |
| ↓            |    4    | saturn, uranus, pluto, neptune                               |


# Celestial Bodies of Transit in MiMi's chart

| Transit   | sign      |  house  |
|-----------|-----------|---------|
| sun       | 17°♎20'  |    2    |
| moon      | 09°♑49'  |    4    |
| mercury   | 24°♎04'  |    2    |
| venus     | 20°♏44'  |    3    |
| mars      | 19°♋29'  |   11    |
| jupiter   | 21°♊20'℞ |   10    |
| saturn    | 13°♓47'℞ |    7    |
| uranus    | 26°♉39'℞ |    9    |
| neptune   | 27°♓59'℞ |    7    |
| pluto     | 29°♑38'℞ |    5    |
| mean_node | 05°♈52'℞ |    7    |
| asc       | 08°♑29'  |    4    |
| mc        | 22°♎28'  |    2    |


# Aspects of Transit vs MiMi

| Transit   |  aspect  | MiMi      |  phase  | orb    |
|-----------|----------|-----------|---------|--------|
| sun       |    △     | venus     |   ← →   | 2° 08' |
| sun       |    ☌     | pluto     |   → ←   | 2° 46' |
| moon      |    ☍     | moon      |   → ←   | 1° 20' |
| moon      |    □     | mercury   |   ← →   | 1° 21' |
| moon      |    △     | asc       |   ← →   | 0° 07' |
| mercury   |    ⚹     | mars      |   → ←   | 2° 55' |
| mercury   |    ⚹     | neptune   |   ← →   | 1° 35' |
| mercury   |    ☌     | pluto     |   ← →   | 3° 58' |
| mercury   |    ⚹     | mean_node |   → ←   | 1° 59' |
| venus     |    ⚹     | saturn    |   → ←   | 0° 19' |
| venus     |    ☌     | uranus    |   → ←   | 3° 47' |
| venus     |    □     | mean_node |   → ←   | 5° 19' |
| mars      |    ⚹     | saturn    |   → ←   | 1° 34' |
| mars      |    △     | uranus    |   → ←   | 5° 02' |
| mars      |    □     | pluto     |   → ←   | 0° 38' |
| jupiter   |    ☌     | venus     |   → ←   | 6° 08' |
| jupiter   |    □     | saturn    |   ← →   | 0° 17' |
| jupiter   |    ☍     | neptune   |   → ←   | 1° 09' |
| jupiter   |    △     | pluto     |   ← →   | 1° 13' |
| jupiter   |    ⚹     | mean_node |   → ←   | 4° 43' |
| saturn    |    △     | moon      |   → ←   | 5° 18' |
| saturn    |    □     | venus     |   ← →   | 1° 25' |
| saturn    |    ☍     | asc       |   → ←   | 4° 05' |
| saturn    |    □     | mc        |   → ←   | 4° 34' |
| uranus    |    □     | mars      |   ← →   | 0° 20' |
| uranus    |    □     | jupiter   |   ← →   | 3° 38' |
| uranus    |    △     | saturn    |   ← →   | 5° 36' |
| uranus    |    ☍     | uranus    |   ← →   | 2° 08' |
| uranus    |    □     | mean_node |   ← →   | 0° 36' |
| neptune   |    △     | uranus    |   ← →   | 3° 28' |
| neptune   |    □     | neptune   |   → ←   | 5° 31' |
| pluto     |    □     | sun       |   ← →   | 0° 41' |
| mean_node |    □     | moon      |   ← →   | 2° 36' |
| mean_node |    ☌     | mercury   |   ← →   | 2° 35' |
| mean_node |    ⚹     | mc        |   ← →   | 3° 20' |
| asc       |    ☍     | moon      |   → ←   | 0° 01' |
| asc       |    □     | mercury   |   → ←   | 0° 02' |
| asc       |    △     | asc       |   → ←   | 1° 13' |
| mc        |    ⚹     | mars      |   ← →   | 4° 31' |
| mc        |    ⚹     | neptune   |   → ←   | 0° 01' |
| mc        |    ☌     | pluto     |   ← →   | 2° 22' |
| mc        |    ⚹     | mean_node |   → ←   | 3° 35' |


# Aspect Cross Reference of Transit(cols) vs MiMi(rows)

╭─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬───────┬──────┬─────────╮
│     │ ☉   │ ☽   │ ☿   │ ♀   │ ♂   │ ♃   │ ♄   │ ♅   │ ♆   │ ♇   │ ☊   │ Asc   │ MC   │  Total  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ☉   │     │     │     │     │     │     │     │     │     │ □   │     │       │      │    1    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ☽   │     │ ☍   │     │     │     │     │ △   │     │     │     │ □   │ ☍     │      │    4    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ☿   │     │ □   │     │     │     │     │     │     │     │     │ ☌   │ □     │      │    3    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ♀   │ △   │     │     │     │     │ ☌   │ □   │     │     │     │     │       │      │    3    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ♂   │     │     │ ⚹   │     │     │     │     │ □   │     │     │     │       │ ⚹    │    3    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ♃   │     │     │     │     │     │     │     │ □   │     │     │     │       │      │    1    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ♄   │     │     │     │ ⚹   │ ⚹   │ □   │     │ △   │     │     │     │       │      │    4    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ♅   │     │     │     │ ☌   │ △   │     │     │ ☍   │ △   │     │     │       │      │    4    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ♆   │     │     │ ⚹   │     │     │ ☍   │     │     │ □   │     │     │       │ ⚹    │    4    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ♇   │ ☌   │     │ ☌   │     │ □   │ △   │     │     │     │     │     │       │ ☌    │    5    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ ☊   │     │     │ ⚹   │ □   │     │ ⚹   │     │ □   │     │     │     │       │ ⚹    │    5    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ Asc │     │ △   │     │     │     │     │ ☍   │     │     │     │     │ △     │      │    3    │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼───────┼──────┼─────────┤
│ MC  │     │     │     │     │     │     │ □   │     │     │     │ ⚹   │       │      │    2    │
╰─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴───────┴──────┴─────────╯

```

- for html report, see [demo.ipynb]

## Configuration

- create a `natal_config.yml` file in project root to override the defaults in `config.py`
- a sample config as follow:

```yaml
theme_type: light

light_theme:
    fire: "#ff0000"
    earth: "#ffff00"
    air: "#00ff00"
    water: "#0000ff"
    points: "#00ffff"

display:
    mean_node: True
    chiron: True

orb:
    conjunction: 8
    opposition: 8
    trine: 6
    square: 6
    sextile: 6
```

read the [docs] for complete references

[docs]: https://hoishing.github.io/natal

## Tech Stack

- [tagit] for creating and manipulating SVG
- [pyswisseph] python extension to the Swiss Ephemeris
- [mkdocs-material] for docs site generation

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[ci-badge]: https://github.com/hoishing/natal/actions/workflows/ci.yml/badge.svg
[ci-url]: https://github.com/hoishing/natal/actions/workflows/ci.yml
[demo.ipynb]: https://github.com/hoishing/natal/blob/main/demo.ipynb
[MIT-badge]: https://img.shields.io/github/license/hoishing/natal
[MIT-url]: https://opensource.org/licenses/MIT
[mkdocs-material]: https://github.com/squidfunk/mkdocs-material
[tagit]: https://github.com/hoishing/tagit
[pypi-badge]: https://img.shields.io/pypi/v/natal
[pypi-url]: https://pypi.org/project/natal
[pyswisseph]: https://github.com/astrorigin/pyswisseph
