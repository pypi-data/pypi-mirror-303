from __future__ import annotations

import lightningchart
from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYZAxis
from lightningchart.charts.chart_3d import Chart3D
from lightningchart.instance import Instance
from lightningchart.series.box_series_3d import BoxSeries3D


class Box3D(Chart3D):
    """Chart for visualizing large sets of individually configurable 3D Boxes."""

    def __init__(
            self,
            data=None,
            box_color: lightningchart.Color = None,
            theme: Themes = Themes.White,
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            zlabel: str = None,
            license: str = None,
            license_information: str = None,
    ):
        """Create a 3D box chart.

        Args:
            data: List of {xCenter, yCenter, zCenter, xSize, ySize, zSize}.
            box_color (Color): Color of the boxes.
            theme (Themes): Theme of the chart.
            title (str): Title of the chart.
            xlabel (str): Title of the x-axis.
            ylabel (str): Title of the y-axis.
            zlabel (str): Title of the z-axis.
        """
        instance = Instance()
        ChartWithSeries.__init__(self, instance)
        self.instance.send(self.id, 'chart3D', {
            'theme': theme.value,
            'license': license or conf.LICENSE_KEY,
            'licenseInformation': license_information or conf.LICENSE_INFORMATION,
        })
        ChartWithXYZAxis.__init__(self)

        self.series = BoxSeries3D(self)
        self.series_list.append(self.series)
        if box_color:
            self.series.set_color(box_color)
        if title:
            self.set_title(title)
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)
        if zlabel:
            self.get_default_z_axis().set_title(zlabel)
        if data:
            self.series.add(data)

    def add(self, data: list[dict]):
        """Add box data to the chart.

        Args:
            data: List of {xCenter, yCenter, zCenter, xSize, ySize, zSize}.

        Returns:
            The instance of the class for fluent interface.
        """
        self.series.add(data)
        return self
