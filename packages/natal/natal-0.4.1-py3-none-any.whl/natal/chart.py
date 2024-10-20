"""
This module provides the Chart class for generating SVG representations of natal charts.
It includes functionality for creating sign wheels, house wheels, body placements,
and aspect lines for both single and composite charts.
"""

from functools import cached_property
from math import cos, radians, sin
from natal.classes import Aspect
from natal.const import SIGN_MEMBERS
from natal.data import Data
from natal.utils import DotDict
from tagit import circle, line, path, svg, text


class Chart(DotDict):
    """
    SVG representation of a natal chart.

    This class generates the visual components of an astrological chart,
    including sign wheels, house wheels, planet placements, and aspect lines.
    It supports both single and composite charts.
    """

    def __init__(
        self,
        data1: Data,
        width: int,
        height: int | None = None,
        data2: Data | None = None,
    ):
        """
        Initialize a Chart object.

        Args:
            data1 (Data): Primary chart data.
            width (int): Width of the SVG.
            height (int | None): Height of the SVG. If None, set to width.
            data2 (Data | None): Secondary chart data for composite charts.
        """
        self.data1 = data1
        self.data2 = data2
        self.width = width
        self.height = height
        if self.height is None:
            self.height = self.width
        self.cx = self.width / 2
        self.cy = self.height / 2

        self.config = self.data1.config
        margin = min(self.width, self.height) * self.config.chart.margin_factor
        self.max_radius = min(self.width - margin, self.height - margin) // 2
        self.ring_thickness = self.max_radius * self.config.chart.ring_thickness_fraction
        self.font_size = self.ring_thickness * self.config.chart.font_size_fraction

    def svg_root(self, content: str | list[str]) -> str:
        """
        Generate an SVG root element with sensible defaults.

        Args:
            content (str | list[str]): The content to be included in the SVG root.

        Returns:
            str: An SVG root element as a string.
        """
        return svg(
            content,
            height=self.height,
            width=self.width,
            # viewbox=None,
            version="1.1",
            xmlns="http://www.w3.org/2000/svg",
        )

    def sector(
        self,
        radius: int,
        start_deg: float,
        end_deg: float,
        fill: str = "white",
        stroke_color: str = "black",
        stroke_width: float = 1,
        stroke_opacity: float = 1,
    ) -> str:
        """
        Create a sector shape in SVG format.

        Args:
            radius (int): Radius of the sector.
            start_deg (float): Starting angle in degrees.
            end_deg (float): Ending angle in degrees.
            fill (str): Fill color of the sector.
            stroke_color (str): Stroke color of the sector.
            stroke_width (float): Width of the stroke.
            stroke_opacity (float): Opacity of the stroke.

        Returns:
            Tag: An SVG path element representing the sector.
        """
        start_rad = radians(start_deg)
        end_rad = radians(end_deg)
        start_x = self.cx - radius * cos(start_rad)
        start_y = self.cy + radius * sin(start_rad)
        end_x = self.cx - radius * cos(end_rad)
        end_y = self.cy + radius * sin(end_rad)

        start_x, start_y, end_x, end_y = [
            round(val, 2) for val in (start_x, start_y, end_x, end_y)
        ]

        path_data = " ".join(
            (
                "M{} {}".format(self.cx, self.cy),
                "L{} {}".format(start_x, start_y),
                "A{} {} 0 0 0 {} {}".format(radius, radius, end_x, end_y),
                "Z",
            )
        )
        return path(
            "",
            d=path_data,
            fill=fill,
            stroke=stroke_color,
            stroke_width=stroke_width,
            stroke_opacity=stroke_opacity,
        )

    def background(self, radius: float, **kwargs) -> str:
        """
        Create a background circle for the chart.

        Args:
            radius (float): Radius of the background circle.
            **kwargs: Additional attributes for the circle element.

        Returns:
            Tag: An SVG circle element representing the background.
        """
        return circle(cx=self.cx, cy=self.cy, r=radius, **kwargs)

    def sign_wheel(self) -> list[str]:
        """
        Generate the zodiac sign wheel.

        Returns:
            list[Tag]: A list of SVG elements representing the sign wheel.
        """
        radius = self.max_radius

        wheel = [self.background(radius=radius, fill=self.config.theme.background)]
        for i in range(12):
            start_deg = self.data1.signs[i].normalized_degree
            end_deg = start_deg + 30
            wheel.append(
                self.sector(
                    radius=radius,
                    start_deg=start_deg,
                    end_deg=end_deg,
                    fill=self.fill_color(i, bg=True),
                    stroke_color=self.config.theme.foreground,
                    stroke_width=self.config.chart.stroke_width,
                )
            )

            # Add sign symbol
            symbol_width = self.font_size
            symbol_radius = radius - (self.ring_thickness / 2)
            symbol_angle = radians(start_deg + 15)  # Center of the sector
            symbol_x = self.cx - symbol_radius * cos(symbol_angle)
            symbol_y = self.cy + symbol_radius * sin(symbol_angle)
            wheel.append(
                text(
                    SIGN_MEMBERS[i].symbol,
                    x=symbol_x,
                    y=symbol_y,
                    fill=self.fill_color(i),
                    font_family=self.config.chart.font,
                    font_size=symbol_width,
                    text_anchor="middle",
                    dominant_baseline="central",
                )
            )

        return wheel

    def house_wheel(self) -> list[str]:
        """
        Generate the house wheel.

        Returns:
            list[Tag]: A list of SVG elements representing the house wheel.
        """
        radius = self.max_radius - self.ring_thickness
        wheel = [self.background(radius, fill=self.config.theme.background)]

        for i, (start_deg, end_deg) in enumerate(self.house_vertices):
            wheel.append(
                self.sector(
                    radius=radius,
                    start_deg=start_deg,
                    end_deg=end_deg,
                    fill=self.fill_color(i, bg=True),
                    stroke_color=self.config.theme.foreground,
                    stroke_width=self.config.chart.stroke_width,
                )
            )

            # Add house number
            number_width = self.font_size * 0.8
            number_radius = radius - (self.ring_thickness / 2)
            number_angle = radians(
                start_deg + ((end_deg - start_deg) % 360) / 2
            )  # Center of the house
            number_x = self.cx - number_radius * cos(number_angle)
            number_y = self.cy + number_radius * sin(number_angle)
            wheel.append(
                text(
                    str(i + 1),  # House numbers start from 1
                    x=number_x,
                    y=number_y,
                    fill=self.fill_color(i),
                    font_family=self.config.chart.font,
                    font_size=number_width,
                    text_anchor="middle",
                    dominant_baseline="central",
                )
            )

        return wheel

    def vertex_line(self) -> list[str]:
        """
        Generate vertex lines for the chart.

        Returns:
            list[Tag]: A list of SVG elements representing vertex lines.
        """
        vertex_radius = self.max_radius + self.ring_thickness
        house_radius = self.max_radius - 2 * self.ring_thickness
        body_radius = self.max_radius - 3 * self.ring_thickness

        lines = [
            self.background(
                house_radius,
                fill=self.config.theme.background,
                stroke=self.config.theme.foreground,
                stroke_width=self.config.chart.stroke_width,
            ),
            self.background(
                body_radius,
                fill="#88888800",  # transparent
                stroke=self.config.theme.dim,
                stroke_width=self.config.chart.stroke_width,
            ),
        ]
        for house in self.data1.houses:
            radius = house_radius
            stroke_width = self.config.chart.stroke_width
            stroke_color = self.config.theme.dim

            if house.value in [1, 4, 7, 10]:
                radius = vertex_radius
                stroke_color = self.config.theme.foreground

            angle = radians(house.normalized_degree)
            end_x = self.cx - radius * cos(angle)
            end_y = self.cy + radius * sin(angle)

            lines.append(
                line(
                    x1=self.cx,
                    y1=self.cy,
                    x2=end_x,
                    y2=end_y,
                    stroke=stroke_color,
                    stroke_width=stroke_width,
                    stroke_opacity=self.config.chart.stroke_opacity,
                )
            )

        return lines

    def outer_body_wheel(self) -> list[str]:
        """
        Generate the outer body wheel for single or composite charts.

        Returns:
            list[Tag]: A list of SVG elements representing the outer body wheel.
        """
        radius = self.max_radius - 3 * self.ring_thickness
        data = self.data2 or self.data1
        return self.body_wheel(radius, data, self.config.chart.outer_min_degree)

    def inner_body_wheel(self) -> list[str] | None:
        """
        Generate the inner body wheel for composite charts.

        Returns:
            list[Tag] | None: A list of SVG elements representing the inner body wheel,
            or None for single charts.
        """
        if self.data2 is None:
            return
        radius = self.max_radius - 4 * self.ring_thickness
        data = self.data1
        return self.body_wheel(radius, data, self.config.chart.inner_min_degree)

    def outer_aspect(self) -> list[str]:
        """
        Generate aspect lines for the outer wheel in single charts.

        Returns:
            list[Tag]: A list of SVG elements representing aspect lines.
        """
        if self.data2 is not None:
            return []
        radius = self.max_radius - 3 * self.ring_thickness
        aspects = self.data1.aspects
        return self.aspect_lines(radius, aspects)

    def inner_aspect(self) -> list[str]:
        """
        Generate aspect lines for the inner wheel in composite charts.

        Returns:
            list[Tag]: A list of SVG elements representing aspect lines.
        """
        if self.data2 is None:
            return []
        radius = self.max_radius - 4 * self.ring_thickness
        aspects = self.data1.calculate_aspects(
            self.data1.composite_aspects_pairs(self.data2)
        )
        return self.aspect_lines(radius, aspects)

    @property
    def svg(self) -> str:
        """
        Generate the SVG representation of the chart.

        Returns:
            str: SVG content.
        """
        return self.svg_root(
            [
                self.sign_wheel(),
                self.house_wheel(),
                self.vertex_line(),
                self.outer_body_wheel(),
                self.inner_body_wheel(),
                self.outer_aspect(),
                self.inner_aspect(),
            ]
        )

    # utils ======================================================

    def adjusted_degrees(self, degrees: list[float], min_degree: float) -> list[float]:
        """
        Adjust spacing between celestial bodies to avoid overlap.

        Args:
            degrees (list[float]): sorted normalized degrees of celestial bodies.
            min_degree (float): Minimum allowed degree separation.

        Returns:
            list[float]: Adjusted degrees of celestial bodies.
        """
        step = min_degree + 0.1  # prevent overlap for float precision
        n = len(degrees)

        fwd_degs = degrees.copy()
        bwd_degs = degrees[::-1]

        # Forward adjustment
        changed = True
        while changed:
            changed = False
            for i in range(n):
                prev_deg = fwd_degs[-1] - 360 if i == 0 else fwd_degs[i - 1]
                delta = fwd_degs[i] - prev_deg
                diff = min(delta, 360 - delta)
                if (fwd_degs[i] < prev_deg) or (diff < min_degree):
                    fwd_degs[i] = prev_deg + step
                    changed = True

        # Backward adjustment
        changed = True
        while changed:
            changed = False
            for i in range(n):
                prev_deg = bwd_degs[-1] + 360 if i == 0 else bwd_degs[i - 1]
                delta = prev_deg - bwd_degs[i]
                diff = min(delta, 360 - delta)
                if (prev_deg < bwd_degs[i]) or (diff < min_degree):
                    bwd_degs[i] = prev_deg - step
                    changed = True

        bwd_degs.reverse()

        # average forward and backward adjustments
        avg_adj = []
        for fwd, bwd in zip(fwd_degs, bwd_degs):
            fwd %= 360
            bwd %= 360
            if abs(fwd - bwd) < 180:
                avg = (fwd + bwd) / 2
            else:
                avg = ((fwd + bwd + 360) / 2) % 360
            avg_adj.append(avg)

        return avg_adj

    def fill_color(self, sign_no: int, bg: bool = False) -> str:
        """
        Get the fill color for a zodiac sign.

        Args:
            sign_no (int): Index of the zodiac sign.
            bg (bool): If True, return a transparent version of the color.

        Returns:
            str: Hexadecimal color code.
        """
        fill_hex = getattr(self.config.theme, SIGN_MEMBERS[sign_no].color)
        if not bg:
            return fill_hex
        trans_fill_hex = f"{fill_hex}{int(self.config.theme.transparency * 255):02x}"
        return trans_fill_hex

    def body_wheel(self, wheel_radius: float, data: Data, min_degree: float):
        """
        Generate elements for both inner and outer body wheels.

        Args:
            wheel_radius (float): Radius of the wheel.
            data (Data): Chart data to use.
            min_degree (float): Minimum degree separation between bodies.

        Returns:
            list[Tag]: A list of SVG elements representing the body wheel.
        """
        norm_deg = lambda x: self.data1.normalize(x.degree)

        sorted_norm_bodies = sorted(data.aspectables, key=norm_deg)
        sorted_norm_degs = [norm_deg(b) for b in sorted_norm_bodies]

        # Calculate adjusted positions
        adj_norm_degs = self.adjusted_degrees(sorted_norm_degs, min_degree)

        output = []
        for body, adj_deg in zip(sorted_norm_bodies, adj_norm_degs):
            font_size = self.font_size
            text_opt = {}

            # special handling for asc and mc
            if body.name in ["asc", "mc"]:
                text_opt = {
                    "lengthAdjust": "spacingAndGlyphs",
                    "textLength": self.font_size * 0.7,
                }
                font_size = self.font_size * 0.85

            symbol_radius = wheel_radius + (self.ring_thickness / 2)

            # Use original angle for line start position
            original_angle = radians(self.data1.normalize(body.degree))
            degree_x = self.cx - wheel_radius * cos(original_angle)
            degree_y = self.cy + wheel_radius * sin(original_angle)

            # Use adjusted angle for symbol position
            adjusted_angle = radians(adj_deg)
            symbol_x = self.cx - symbol_radius * cos(adjusted_angle)
            symbol_y = self.cy + symbol_radius * sin(adjusted_angle)

            # Add line connecting to the inner circle
            inner_radius = wheel_radius - self.ring_thickness
            inner_x = self.cx - inner_radius * cos(original_angle)
            inner_y = self.cy + inner_radius * sin(original_angle)

            output.extend(
                [
                    line(
                        x1=degree_x,
                        y1=degree_y,
                        x2=symbol_x,
                        y2=symbol_y,
                        stroke=self.config.theme[body.color],
                        stroke_width=self.config.chart.stroke_width / 2,
                    ),
                    circle(
                        cx=symbol_x,
                        cy=symbol_y,
                        r=self.font_size / 2,
                        fill=self.config.theme.background,
                    ),
                    line(
                        x1=degree_x,
                        y1=degree_y,
                        x2=inner_x,
                        y2=inner_y,
                        stroke=self.config.theme.dim,
                        stroke_width=self.config.chart.stroke_width / 2,
                        stroke_dasharray=self.ring_thickness / 11,
                    ),
                    text(
                        body.symbol,
                        x=symbol_x,
                        y=symbol_y,
                        fill=self.config.theme[body.color],
                        font_family=self.config.chart.font,
                        font_size=font_size,
                        text_anchor="middle",
                        dominant_baseline="central",
                        **text_opt,
                    ),
                ]
            )
        return output

    def aspect_lines(self, radius: float, aspects: list[Aspect]) -> list[str]:
        """
        Draw aspect lines between aspectable celestial bodies.

        Args:
            radius (float): Radius of the aspect wheel.
            aspects (list[Aspect]): List of aspects to draw.

        Returns:
            list[Tag]: A list of SVG elements representing aspect lines.
        """
        output = [
            self.background(
                radius,
                fill=self.config.theme.background,
                stroke=self.config.theme.dim,
                stroke_width=self.config.chart.stroke_width,
            )
        ]
        for aspect in aspects:
            start_angle = radians(self.data1.normalize(aspect.body1.degree))
            end_angle = radians(self.data1.normalize(aspect.body2.degree))
            orb_fraction = 1 - aspect.orb / self.config.orb[aspect.aspect_member.name]
            opacity_factor = (
                1 if aspect.aspect_member.name == "conjunction" else orb_fraction
            )
            output.append(
                line(
                    x1=self.cx - radius * cos(start_angle),
                    y1=self.cy + radius * sin(start_angle),
                    x2=self.cx - radius * cos(end_angle),
                    y2=self.cy + radius * sin(end_angle),
                    stroke=self.config.theme[aspect.aspect_member.color],
                    stroke_width=self.config.chart.stroke_width / 2,
                    stroke_opacity=self.config.chart.stroke_opacity * opacity_factor,
                )
            )
        return output

    @cached_property
    def house_vertices(self) -> list[tuple[float, float]]:
        """
        Calculate the vertices (start and end degrees) of each house.

        Returns:
            list[tuple[float, float]]: A list of tuples containing start and end degrees for each house.
        """
        vertices = []
        for i in range(12):
            next_i = (i + 1) % 12
            start_deg = self.data1.houses[i].normalized_degree
            end_deg = self.data1.houses[next_i].normalized_degree
            # Handle the case where end_deg is less than start_deg (crosses 0°)
            if end_deg < start_deg:
                end_deg += 360
            vertices.append((start_deg, end_deg))

        return vertices
