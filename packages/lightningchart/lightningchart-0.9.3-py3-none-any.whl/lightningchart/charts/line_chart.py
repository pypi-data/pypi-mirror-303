from __future__ import annotations

import lightningchart
from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYAxis
from lightningchart.charts.chart_xy import ChartXY
from lightningchart.instance import Instance
from lightningchart.series.point_line_series import PointLineSeries


class LineChart(ChartXY):
    """Chart for visualizing a list of Points (pair of X and Y coordinates), with a continuous stroke."""

    def __init__(
            self,
            x: list[int | float] = None,
            y: list[int | float] = None,
            line_type: str = 'line',
            line_color: lightningchart.Color = None,
            line_width: int | float = 2,
            point_shape: str = 'circle',
            point_color: lightningchart.Color = None,
            point_size: int | float = 2,
            title: str = 'Line Chart',
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
        """Create a line chart using declarative API.

        Args:
            x (list[int | float]): x-axis datapoints
            y (list[int | float]): y-axis datapoints

            line_type (str): "line" | "spline" | "step" | "step-after" | "step-before"
            line_color (Color): Color of the line
            line_width (int | float): Width of the line

            point_shape (str): "arrow" | "circle" | "cross" | "diamond" | "minus" | "plus" | "square" | "star" | "triangle"
            point_color (Color): Color of the points
            point_size (int | float): Size of the points

            title (str): Title of the chart
            xlabel (str): Title of the x-axis
            ylabel (str): Title of the y-axis

            theme (Themes): Overall theme of the chart
            license (str): License key
        """
        instance = Instance()
        ChartWithSeries.__init__(self, instance)
        self.instance.send(self.id, 'chartXY', {
            'theme': theme.value,
            'license': license or conf.LICENSE_KEY,
            'licenseInformation': license_information or conf.LICENSE_INFORMATION,
        })
        ChartWithXYAxis.__init__(self)

        self.series = PointLineSeries(
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

        if str(line_type).lower() == 'spline':
            self.instance.send(self.series.id, 'setCurvePreprocessing', {'type': 'spline'})
        elif str(line_type).lower() in ('step', 'step-middle'):
            self.instance.send(self.series.id, 'setCurvePreprocessing', {'type': 'step', 'step': 'middle'})
        elif str(line_type).lower() == 'step-after':
            self.instance.send(self.series.id, 'setCurvePreprocessing', {'type': 'step', 'step': 'after'})
        elif str(line_type).lower() == 'step-before':
            self.instance.send(self.series.id, 'setCurvePreprocessing', {'type': 'step', 'step': 'before'})

        if line_color:
            self.series.set_line_color(line_color)
        if line_width:
            self.series.set_line_thickness(line_width)
        if point_shape:
            self.series.set_point_shape(point_shape)
        if point_size:
            self.series.set_point_size(point_size)
        if point_color:
            self.series.set_point_color(point_color)

        if title:
            self.instance.send(self.id, 'setTitle', {'title': title})
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)

        self.add = self.series.add
        self.clear = self.series.clear

        if y is not None and x is None:
            self.series.append_samples(y_values=y)
        elif x is not None and y is not None:
            self.series.append_samples(
                x_values=x,
                y_values=y
            )
