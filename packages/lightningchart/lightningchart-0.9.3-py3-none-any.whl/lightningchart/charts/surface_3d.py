from __future__ import annotations

import lightningchart
from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYZAxis
from lightningchart.charts.chart_3d import Chart3D
from lightningchart.instance import Instance
from lightningchart.series.surface_grid_series import SurfaceGridSeries


class Surface3D(Chart3D):
    """Series for visualizing a three-dimensional Surface Grid. The grid is defined by
    imagining a plane along X and Z axis, split to columns (cells along X axis) and rows (cells along Z axis)
    """

    def __init__(
            self,
            data: list[list[int | float]],
            min_value: int | float = None,
            max_value: int | float = None,
            min_color: lightningchart.Color = lightningchart.Color('#000000'),
            max_color: lightningchart.Color = lightningchart.Color('#ffffff'),
            theme: Themes = Themes.White,
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            zlabel: str = None,
            license: str = None,
            license_information: str = None,
    ):
        """Create a 3D surface chart.

        Args:
            data (list[list[int | float]]): Matrix of datapoints, i.e., list of lists.
            min_value (int | float): Minimum value of a datapoint.
            max_value (int | float): Maximum value of a datapoint.
            min_color (Color): Color of the minimum value.
            max_color (Color): Color of the maximum value.
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

        self.series = SurfaceGridSeries(self, rows=len(data), columns=len(data[0]))
        self.series_list.append(self.series)
        self.series.invalidate_intensity_values(data).invalidate_height_map(data)
        if min_value is None:
            min_value = min(min(sublist) for sublist in data)
        if max_value is None:
            max_value = max(max(sublist) for sublist in data)
        self.series.set_min_max_palette_colors(
            min_value=min_value, max_value=max_value, min_color=min_color, max_color=max_color
        )
        if title:
            self.set_title(title)
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)
        if zlabel:
            self.get_default_z_axis().set_title(zlabel)
