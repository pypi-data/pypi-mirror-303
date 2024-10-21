from __future__ import annotations

from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYAxis
from lightningchart.charts.chart_xy import ChartXY
from lightningchart.instance import Instance
from lightningchart.series.area_series import AreaSeries, AreaSeriesNegative, AreaSeriesBipolar


class AreaChart(ChartXY):
    """Chart for visualizing a collection of progressive Points
    by filling the area between the points Y-values and a static baseline value.
    """
    
    def __init__(
            self,
            x: list[int | float] = None,
            y: list[int | float] = None,
            area_type: str = 'positive',
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            theme: Themes = Themes.White,
            license: str = None,
            license_information: str = None,
    ):
        """Create an area chart.

        Args:
            x (list[int | float]): List of lists containing y values.
            y (list[int | float]): List of lists containing y values.
            area_type (str): "positive" | "negative" | "bipolar"
            theme (Themes): Theme of the chart.
            title (str): Title of the chart.
            xlabel (str): Title of the x-axis.
            ylabel (str): Title of the y-axis.
        """
        instance = Instance()
        ChartWithSeries.__init__(self, instance)
        self.instance.send(self.id, 'chartXY', {
            'theme': theme.value,
            'license': license or conf.LICENSE_KEY,
            'licenseInformation': license_information or conf.LICENSE_INFORMATION,
        })
        ChartWithXYAxis.__init__(self)

        if area_type == 'negative':
            self.series = AreaSeriesNegative(chart=self)
        elif area_type == 'bipolar':
            self.series = AreaSeriesBipolar(chart=self)
        else:
            self.series = AreaSeries(
                chart=self,
                # data_pattern=None,
                # colors=True,
                # lookup_values=True,
                # ids=True,
                # sizes=True,
                # rotations=True,
                # auto_sorting_enabled=True,
                # x_axis=None,
                # y_axis=None,
            )

        self.series_list.append(self.series)

        if title:
            self.set_title(title)
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)

        if y is not None and x is None:
            self.series.add(y=y)
        elif x is not None and y is not None:
            self.series.add(x=x, y=y)
