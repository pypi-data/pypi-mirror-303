from natal.const import *
from enum import StrEnum
from math import floor


class MovableBody(Body):
    """
    Represents a movable celestial body with additional properties.
    """

    degree: float = 0
    speed: float = 0
    normalized_degree: float = 0

    @property
    def signed_deg(self) -> int:
        """
        Degree in sign, between 0 and 29.

        Returns:
            int: The degree in sign.
        """
        return int(self.degree % 30)

    @property
    def minute(self) -> int:
        """
        Minute of the body, between 0 and 59.

        Returns:
            int: The minute of the body.
        """
        minutes = (self.degree % 30 - self.signed_deg) * 60
        return floor(minutes)

    @property
    def retro(self) -> bool:
        """
        Retrograde status.

        Returns:
            bool: True if retrograde, False otherwise.
        """
        return self.speed < 0

    @property
    def rx(self) -> str:
        """
        Retrograde symbol.

        Returns:
            str: The retrograde symbol if retrograde, empty string otherwise.
        """
        return "℞" if self.retro else ""

    @property
    def sign(self) -> SignMember:
        """
        Return sign name, symbol, element, quality, and polarity.

        Returns:
            SignMember: The sign member.
        """
        idx = int(self.degree // 30)
        return SIGN_MEMBERS[idx]

    @property
    def dms(self) -> str:
        """
        Degree Minute Second representation of the position.

        Returns:
            str: The DMS representation.
        """
        op = [f"{self.signed_deg:02d}°", f"{self.minute:02d}'"]
        if self.rx:
            op.append(self.rx)
        return "".join(op)

    @property
    def signed_dms(self) -> str:
        """
        Degree Minute representation with sign.

        Returns:
            str: The signed DMS representation.
        """
        op = [f"{self.signed_deg:02d}°", self.sign.symbol, f"{self.minute:02d}'"]
        if self.rx:
            op.append(self.rx)
        return "".join(op)


class Planet(MovableBody):
    """
    Represents a planet.
    """

    ...


class Extra(MovableBody):
    """
    Represents an extra celestial body (e.g. Moon's Node and Asteroids).
    """

    ...


class Vertex(MovableBody):
    """
    Represents a vertex (Asc, Dsc, MC, IC).
    """

    ...


class Aspectable(MovableBody):
    """
    Represents a celestial body that can form aspects.
    """

    ...


class Sign(MovableBody):
    """
    Represents a zodiac sign.
    """

    ruler: str
    classic_ruler: str
    quality: str
    element: str
    polarity: str


class House(MovableBody):
    """
    Represents a house.
    """

    ruler: str = None
    ruler_sign: str = None
    ruler_house: int = None
    classic_ruler: str = None
    classic_ruler_sign: str = None
    classic_ruler_house: int = None


class Aspect(DotDict):
    """
    Represents an aspect between two celestial bodies.
    """

    body1: Aspectable
    body2: Aspectable
    aspect_member: AspectMember
    applying: bool = None
    orb: float = None


class HouseSys(StrEnum):
    Placidus = "P"
    Koch = "K"
    Equal = "E"
    Campanus = "C"
    Regiomontanus = "R"
    Porphyry = "P"
    Whole_Sign = "W"
