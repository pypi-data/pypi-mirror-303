"""
Constants and utility functions for the natal package.
"""

from natal.utils import DotDict


class Body(DotDict):
    """
    Represents a celestial body in raw data.
    Base class for all members.
    """

    name: str
    symbol: str
    value: int
    color: str


class PlanetMember(Body):
    """
    Represents a planet in raw data.
    """

    ...


class AspectMember(Body):
    """
    Represents an aspect in raw data.
    (conjunction, opposition, trine, square, sextile)
    """

    ...


class ElementMember(Body):
    """
    Represents an element in raw data.
    (fire, earth, air, water)
    """

    ...


class QualityMember(Body):
    """
    Represents a quality in raw data.
    (cardinal, fixed, mutable)
    """

    ...


class PolarityMember(Body):
    """
    Represents a polarity in raw data.
    (positive, negative)
    """

    ...


class HouseMember(Body):
    """
    Represents a house in raw data.
    """

    ...


class ExtraMember(Body):
    """
    Represents an extra celestial body in raw data.
    (e.g. asteroids, nodes)
    """

    ...


class VertexMember(Body):
    """
    Represents a vertex in raw data (asc, ic, dsc, mc).
    """

    ...


class SignMember(Body):
    """
    Represents a zodiac sign in raw data.
    """

    ruler: str
    classic_ruler: str
    quality: str
    element: str
    polarity: str


# utils ==================================


def get_member(raw_data: dict, name: str) -> DotDict:
    """
    Get a member from raw data by name.

    Args:
        raw_data (dict): The raw data dictionary.
        name (str): The name of the member.

    Returns:
        DotDict: The member as a DotDict.
    """
    idx = raw_data["name"].index(name)
    member = {key: raw_data[key][idx] for key in raw_data.keys()}
    return DotDict(**member)


def get_members(raw_data: dict) -> list[DotDict]:
    """
    Get all members from raw data.

    Args:
        raw_data (dict): The raw data dictionary.

    Returns:
        list[DotDict]: A list of members as DotDicts.
    """
    return [get_member(raw_data, name) for name in raw_data["name"]]


# Raw Data ===============================

# fmt: off
PLANET_NAMES = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
EXTRA_NAMES = ["mean_node", "chiron", "pholus", "ceres", "pallas", "juno", "vesta"]
ELEMENT_NAMES = ["fire", "earth", "air", "water"]
QUALITY_NAMES = ["cardinal", "fixed", "mutable"]
POLARITY_NAMES = ["positive", "negative"]
SIGN_NAMES = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
HOUSE_NAMES = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
ASPECT_NAMES = ["conjunction", "opposition", "trine", "square", "sextile"]
VERTEX_NAMES = ["asc", "ic", "dsc", "mc"]
# fmt: on

PLANETS = dict(
    name=PLANET_NAMES,
    symbol="☉☽☿♀♂♃♄♅♆♇",
    value=list(range(10)),
    color="fire water air earth fire fire earth air water water".split(),
)

ASPECTS = dict(
    name=ASPECT_NAMES,
    symbol="☌☍△□⚹",
    value=[0, 180, 120, 90, 60],
    color=["others", "water", "air", "fire", "points"],
)

ELEMENTS = dict(
    name=ELEMENT_NAMES,
    symbol="🜂🜃🜁🜄",
    value=[0, 1, 2, 3],
    color=["fire", "earth", "air", "water"],
)

QUALITY = dict(
    name=QUALITY_NAMES,
    symbol="⟑⊟𛰣",
    value=[0, 1, 2],
    color=["fire", "earth", "air"],
)

POLARITY = dict(
    name=POLARITY_NAMES,
    symbol=["+", "-"],
    value=[1, -1],
    color=["positive", "negative"],
)

SIGNS = dict(
    name=SIGN_NAMES,
    symbol="♈♉♊♋♌♍♎♏♐♑♒♓",
    value=list(range(1, 13)),
    color=["fire", "earth", "air", "water"] * 3,
    ruler="mars venus mercury moon sun mercury venus pluto jupiter saturn uranus neptune".split(),
    classic_ruler="mars venus mercury moon sun mercury venus mars jupiter saturn saturn jupiter".split(),
    quality=list(QUALITY["name"]) * 4,
    element=list(ELEMENTS["name"]) * 3,
    polarity=list(POLARITY["name"]) * 6,
)

HOUSES = dict(
    name=HOUSE_NAMES,
    symbol=[str(i) for i in range(1, 13)],
    value=list(range(1, 13)),
    color=["fire", "earth", "air", "water"] * 3,
)

EXTRAS = dict(
    name=EXTRA_NAMES,
    symbol="☊⚷⯛⚳⚴⚵⚶",
    value=[10, 15, 16, 17, 18, 19, 20],
    color=["points"] + ["asteroids"] * 6,
)

VERTICES = dict(
    name=VERTEX_NAMES,
    symbol=["Asc", "IC", "Dsc", "MC"],
    value=[1, 4, 7, 10],
    color=["fire", "water", "air", "earth"],
)

# Derived Members =================================

PLANET_MEMBERS = get_members(PLANETS)
ASPECT_MEMBERS = get_members(ASPECTS)
ELEMENT_MEMBERS = get_members(ELEMENTS)
QUALITY_MEMBERS = get_members(QUALITY)
POLARITY_MEMBERS = get_members(POLARITY)
SIGN_MEMBERS = get_members(SIGNS)
HOUSE_MEMBERS = get_members(HOUSES)
EXTRA_MEMBERS = get_members(EXTRAS)
VERTEX_MEMBERS = get_members(VERTICES)
