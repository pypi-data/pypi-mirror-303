from __future__ import annotations

import lightningchart
from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYZAxis
from lightningchart.charts.chart_3d import Chart3D
from lightningchart.instance import Instance
from lightningchart.series.point_series_3d import PointSeries3D


class ScatterChart3D(Chart3D):
    """Series type for visualizing a collection of { x, y, z } coordinates by different markers."""

    def __init__(
            self,
            x: list[int | float] = None,
            y: list[int | float] = None,
            z: list[int | float] = None,
            point_type: str = 'sphere',
            point_color: lightningchart.Color = None,
            point_size: int | float = 4,
            theme: Themes = Themes.White,
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            zlabel: str = None,
            license: str = None,
            license_information: str = None,
    ):
        """Create a 3D scatter chart using declarative API

        Args:
            x (list[int | float]): x-axis datapoints
            y (list[int | float]): y-axis datapoints
            z (list[int | float]): z-axis datapoints
            point_type (str): "sphere" | "cube"
            point_color (Color): Color of the points
            point_size (int | float): Size of the points
            theme (Themes): Overall theme of the chart
            title (str): Title of the chart
            xlabel (str): Title of the x-axis
            ylabel (str): Title of the y-axis
            zlabel (str): Title of the z-axis
            license (str): License key.
        """
        instance = Instance()
        ChartWithSeries.__init__(self, instance)
        self.instance.send(self.id, 'chart3D', {
            'theme': theme.value,
            'license': license or conf.LICENSE_KEY,
            'licenseInformation': license_information or conf.LICENSE_INFORMATION,
        })
        ChartWithXYZAxis.__init__(self)

        self.series = PointSeries3D(self)
        self.series_list.append(self.series)
        self.series.set_point_shape(point_type)
        self.series.set_point_size(point_size)

        self.add = self.series.add
        self.clear = self.series.clear

        if point_color:
            self.series.set_point_color(point_color)
        if title:
            self.set_title(title)
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)
        if zlabel:
            self.get_default_z_axis().set_title(zlabel)
        if x is not None and y is not None and z is not None:
            self.add(x, y, z)
