from __future__ import annotations

import lightningchart
from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYAxis
from lightningchart.charts.chart_xy import ChartXY
from lightningchart.instance import Instance
from lightningchart.series.point_series import PointSeries

try:
    import numpy as np
except ImportError:
    np = None


class ScatterChart(ChartXY):
    """Chart type for visualizing collection of two-dimensional points."""

    def __init__(
            self,
            x: list[int | float] = None,
            y: list[int | float] = None,
            point_shape: str = 'circle',
            point_color: lightningchart.Color = None,
            point_size: int | float = 5,
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            theme: Themes = Themes.White,
            license: str = None,
            data_pattern=None,
            individual_colors=False,
            individual_lookup_values=False,
            individual_ids=False,
            individual_sizes=False,
            individual_rotations=False,
            license_information: str = None,
    ):
        """Create a scatter chart using declarative API

        Args:
            x (list[int | float]): x-axis datapoints
            y (list[int | float]): y-axis datapoints

            point_shape (str):  "arrow" | "circle" | "cross" | "diamond" | "minus" | "plus" | "square" | "star" | "triangle"
            point_color (Color): Color of the points
            point_size (int | float): Size of the points

            title (str): Title of the chart
            xlabel (str): Title of the x-axis
            ylabel (str): Title of the y-axis

            theme (Themes): Overall theme of the chart
            license (str): License key.
        """
        instance = Instance()
        ChartWithSeries.__init__(self, instance)
        self.instance.send(self.id, 'chartXY', {
            'theme': theme.value,
            'license': license or conf.LICENSE_KEY,
            'licenseInformation': license_information or conf.LICENSE_INFORMATION,
        })
        ChartWithXYAxis.__init__(self)

        self.series = PointSeries(
            chart=self,
            data_pattern=data_pattern,
            colors=individual_colors,
            lookup_values=individual_lookup_values,
            ids=individual_ids,
            sizes=individual_sizes,
            rotations=individual_rotations,
            # auto_sorting_enabled=True,
            # x_axis=None,
            # y_axis=None,
        )
        self.series_list.append(self.series)

        if point_shape:
            self.series.set_point_shape(point_shape)
        if point_color:
            self.series.set_point_color(point_color)
        if point_size:
            self.series.set_point_size(point_size)

        if title:
            self.set_title(title)
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)

        self.add = self.series.add
        self.clear = self.series.clear

        if x is not None or y is not None:
            self.add(x, y)

    def create_regression_line(self, x=None, y=None, datapoints=None, degree=1):
        """Create automatic regression lines based on scatter point data.
        (EXPERIMENTAL FEATURE)

        Args:
            x: x datapoints.
            y: y datapoints.
            datapoints: list of {x,y} datapoints.
            degree: The degree of the regression curve.

        Returns:
            Reference to the regression line (Line Series).
        """
        if np is None:
            raise ImportError("NumPy is not installed. Please install it to use this functionality.")

        if datapoints and not x and not y:
            x = [d['x'] for d in datapoints]
            y = [d['y'] for d in datapoints]
        elif x and y:
            x = np.array(x)
            y = np.array(y)
        else:
            return False
        coefficients = np.polyfit(x, y, degree)
        polynomial = np.poly1d(coefficients)
        x_curve = np.linspace(np.min(x), np.max(x), 100)
        y_curve = polynomial(x_curve)
        x_curve = x_curve.tolist()
        y_curve = y_curve.tolist()
        return self.add_line_series().add(x_curve, y_curve).set_line_thickness(5)
