from __future__ import annotations

import lightningchart
from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYAxis
from lightningchart.charts.chart_xy import ChartXY
from lightningchart.instance import Instance
from lightningchart.series.heatmap_grid_series import HeatmapGridSeries


class Heatmap(ChartXY):
    """Chart for visualizing a Intensity Heatmap Grid with a static column and grid count."""

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
            license: str = None,
            license_information: str = None,
    ):
        """Crate a heat map.

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

        self.series = HeatmapGridSeries(self, columns=len(data), rows=len(data[0]))
        self.series_list.append(self.series)
        self.series.invalidate_intensity_values(data).set_intensity_interpolation('disabled')
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
