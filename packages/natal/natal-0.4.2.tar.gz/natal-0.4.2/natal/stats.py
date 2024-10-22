"""
This module provides statistical analysis for natal charts.

It contains the Stats class, which calculates and presents various astrological statistics
for a single natal chart or a comparison between two charts.
"""

from collections import defaultdict
from math import floor
from natal.classes import Aspect
from natal.data import Data
from tagit import div, h4
from tabulate import tabulate
from typing import Iterable, Literal, NamedTuple

DistKind = Literal["element", "quality", "polarity"]
ReportKind = Literal["ascii", "html"]
Grid = list[Iterable[str | int]]


class StatData(NamedTuple):
    title: str
    grid: Grid


class Stats:
    """
    Statistics for a natal chart data.

    This class calculates and presents various astrological statistics for a single natal chart
    or a comparison between two charts.

    Attributes:
        data1 (Data): The primary natal chart data.
        data2 (Data | None): The secondary natal chart data for comparisons (optional).
        tb_option (dict): Default options for table formatting.
    """

    data1: Data
    data2: Data | None = None

    def __init__(self, data1: Data, data2: Data = None) -> None:
        """
        Initialize the Stats object with one or two natal chart data sets.

        Args:
            data1 (Data): The primary natal chart data.
            data2 (Data, optional): The secondary natal chart data for comparisons.
        """
        self.data1 = data1
        self.data2 = data2
        if self.data2:
            self.composite_pairs = data2.composite_aspects_pairs(self.data1)
            self.composite_aspects = data1.calculate_aspects(self.composite_pairs)

    # data grids =================================================================

    def distribution(self, kind: DistKind) -> StatData:
        """
        Generate distribution statistics for elements, qualities, or polarities.

        Args:
            kind (DistKind): The type of distribution to calculate ("element", "quality", or "polarity").

        Returns:
            StatData: A named tuple containing the title and grid of distribution data.
        """
        title = f"{kind.capitalize()} Distribution ({self.data1.name})"
        bodies = defaultdict(lambda: [0, []])
        for body in self.data1.aspectables:
            key = body.sign[kind]
            bodies[key][0] += 1  # act as a counter
            bodies[key][1].append(f"{body.name} {body.sign.symbol}")
        grid = [(kind, "count", "bodies")]
        data = [(key, val[0], ", ".join(val[1])) for key, val in bodies.items()]
        grid.extend(data)
        return StatData(title, grid)

    @property
    def celestial_body(self) -> StatData:
        """
        Generate a grid of celestial body positions for the primary chart.

        Returns:
            StatData: A named tuple containing the title and grid of celestial body data.
        """
        title = f"Celestial Bodies ({self.data1.name})"
        grid = [("body", "sign", "house")]
        for body in self.data1.aspectables:
            grid.append((body.name, body.signed_dms, self.data1.house_of(body)))
        return StatData(title, grid)

    @property
    def data2_celestial_body(self) -> StatData:
        """
        Generate a grid of celestial body positions for the secondary chart.

        Returns:
            StatData: A named tuple containing the title and grid of celestial body data.
        """
        title = f"Celestial Bodies of {self.data2.name} in {self.data1.name}'s chart"
        grid = [(self.data2.name, "sign", "house")]
        for body in self.data2.aspectables:
            grid.append((body.name, body.signed_dms, self.data1.house_of(body)))
        return StatData(title, grid)

    @property
    def house(self) -> StatData:
        """
        Generate a grid of house data for the primary chart.

        Returns:
            StatData: A named tuple containing the title and grid of house data.
        """
        title = f"Houses ({self.data1.name})"
        grid = [("house", "sign", "ruler", "ruler sign", "ruler house")]
        for house in self.data1.houses:
            grid.append(
                (
                    house.value,
                    house.signed_dms,
                    house.ruler,
                    house.ruler_sign,
                    house.ruler_house,
                )
            )
        return StatData(title, grid)

    @property
    def quadrant(self) -> StatData:
        """
        Generate a grid of celestial body distribution in quadrants.

        Returns:
            StatData: A named tuple containing the title and grid of quadrant distribution data.
        """
        title = f"Quadrants ({self.data1.name})"
        quad_names = ["1st ◵", "2nd ◶", "3rd ◷", "4th ◴"]
        quadrants = defaultdict(lambda: [0, []])
        for i, quad in enumerate(self.data1.quadrants):
            if quad:
                for body in quad:
                    quadrants[i][0] += 1  # act as a counter
                    quadrants[i][1].append(f"{body.name}")
            else:
                # no celestial body in this quadrant
                quadrants[i][0] = 0
        grid = [("quadrant", "count", "bodies")]
        data = [
            (quad_names[quad_no], val[0], ", ".join(val[1]))
            for quad_no, val in quadrants.items()
        ]
        return StatData(title, grid + data)

    @property
    def hemisphere(self) -> StatData:
        """
        Generate a grid of celestial body distribution in hemispheres.

        Returns:
            StatData: A named tuple containing the title and grid of hemisphere distribution data.
        """
        title = f"Hemispheres ({self.data1.name})"
        grid = [("hemisphere", "count", "bodies")]
        data = self.quadrant.grid[1:]
        left = ("←", data[0][1] + data[3][1], f"{data[0][2]}, {data[3][2]}")
        right = ("→", data[1][1] + data[2][1], f"{data[1][2]}, {data[2][2]}")
        top = ("↑", data[2][1] + data[3][1], f"{data[2][2]}, {data[3][2]}")
        bottom = ("↓", data[0][1] + data[1][1], f"{data[0][2]}, {data[1][2]}")
        return StatData(title, grid + [left, right, top, bottom])

    @property
    def aspect(self) -> StatData:
        """
        Generate a grid of aspects for the primary chart.

        Returns:
            StatData: A named tuple containing the title and grid of aspect data.
        """
        title = f"Aspects ({self.data1.name})"
        headers = ["body 1", "aspect", "body 2", "phase", "orb"]
        return StatData(title, _aspect_grid(self.data1.aspects, headers))

    @property
    def composite_aspect(self) -> StatData:
        """
        Generate a grid of composite aspects between two charts.

        Returns:
            StatData: A named tuple containing the title and grid of composite aspect data.
        """
        title = f"Aspects of {self.data2.name} vs {self.data1.name}"
        headers = [self.data2.name, "aspect", self.data1.name, "phase", "orb"]
        return StatData(title, _aspect_grid(self.composite_aspects, headers))

    @property
    def cross_ref(self) -> StatData:
        """
        Generate a grid for aspect cross-reference between charts or within a single chart.

        Returns:
            StatData: A named tuple containing the title and grid of aspect cross-reference data.
        """
        name = (
            f"{self.data2.name}(cols) vs {self.data1.name}(rows)"
            if self.data2
            else self.data1.name
        )
        title = f"Aspect Cross Reference of {name}"
        aspectable1 = self.data1.aspectables
        aspectable2 = self.data2.aspectables if self.data2 else self.data1.aspectables
        aspects = self.composite_aspects if self.data2 else self.data1.aspects
        body_symbols = [body.symbol for body in aspectable1]
        grid = [[""] + body_symbols + ["Total"]]  # Header row with Total column
        for body1 in aspectable1:
            row = [body1.symbol]
            aspect_count = 0
            for body2 in aspectable2:
                aspect = next(
                    (
                        asp
                        for asp in aspects
                        if (asp.body1 == body1 and asp.body2 == body2)
                        or (asp.body1 == body2 and asp.body2 == body1)
                    ),
                    None,
                )
                if aspect:
                    row.append(aspect.aspect_member.symbol)
                    aspect_count += 1
                else:
                    row.append("")

            row.append(str(aspect_count))  # Add total count to the end of the row
            grid.append(row)
        return StatData(title, grid)

    def full_report(self, kind: ReportKind) -> str:
        """
        Generate a full report containing all statistical tables.

        Returns:
            str: A formatted string containing the full statistical report.
        """
        output = "\n"
        for dist in DistKind.__args__:
            output += self.table_of("distribution", kind, dist)
        output += self.table_of("celestial_body", kind)
        output += self.table_of("house", kind)
        output += self.table_of("quadrant", kind)
        output += self.table_of("hemisphere", kind)
        if self.data2:
            output += self.table_of("data2_celestial_body", kind)
            output += self.table_of(
                "composite_aspect", kind, colalign=("left", "center", "left", "center")
            )
        else:
            output += self.table_of("aspect", kind)
        output += self.table_of("cross_ref", kind, tablefmt="rounded_grid")
        return output

    def table_of(
        self, fn_name: str, kind: ReportKind, *fn_args, **ascii_options
    ) -> str:
        """
        Format a table with a title.

        Args:
            stat (StatData): A named tuple containing the title and the table.
            kind (ReportKind): The kind of report to generate ("ascii" or "html").
            fmt (str): The format of the table ("github" or "html").
            options (dict): Additional options for `tabulate`.

        Returns:
            str: A formatted string containing the titled table.
        """
        stat = getattr(self, fn_name)
        if fn_args:
            stat = stat(*fn_args)
        base_option = dict(headers="firstrow", numalign="center")

        if kind == "ascii":
            options = base_option | {"tablefmt": "github"} | ascii_options
            output = f"# {stat.title}\n\n"
            output += tabulate(stat.grid, **options)
            output += "\n\n\n"
            return output
        elif kind == "html":
            options = base_option | {"tablefmt": "html"}
            tb = tabulate(stat.grid, **options)
            output = div([h4(stat.title), tb], class_=f"tabulate {fn_name}")
            return str(output)


# utils ======================================================================


def _aspect_grid(aspects: list[Aspect], headers: list[str]) -> Grid:
    """
    Generate a grid of aspect data.

    Args:
        aspects (list[Aspect]): A list of Aspect objects.
        headers (list[str]): The headers for the aspect grid.

    Returns:
        Grid: A grid containing aspect data.
    """
    grid = [headers]
    for aspect in aspects:
        degree = floor(aspect.orb)
        minutes = round((aspect.orb - degree) * 60)
        grid.append(
            (
                aspect.body1.name,
                aspect.aspect_member.symbol,
                aspect.body2.name,
                "→ ←" if aspect.applying else "← →",
                f"{degree}° {minutes:02d}'",
            )
        )
    return grid


# for quick testing
if __name__ == "__main__":
    from tests import person1, person2

    shing = Data(**person1)
    belle = Data(**person2)
    stats = Stats(data1=shing, data2=belle)
    print(stats.full_report(kind="ascii"))
