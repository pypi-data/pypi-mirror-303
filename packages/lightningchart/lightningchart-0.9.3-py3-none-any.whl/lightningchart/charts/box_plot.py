from __future__ import annotations

from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYAxis
from lightningchart.charts.chart_xy import ChartXY
from lightningchart.instance import Instance
from lightningchart.series.box_series import BoxSeries

try:
    import numpy as np
except ImportError:
    np = None

try:
    import pandas as pd
except ImportError:
    pd = None


class BoxPlot(ChartXY):
    """Chart for visualizing data groups through quartiles."""

    def __init__(
            self,
            data,
            theme: Themes = Themes.White,
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            license: str = None,
            license_information: str = None,
    ):
        """Create a box plot.

        Args:
            data: Data input for the chart.
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

        self.series = BoxSeries(self)
        self.series_list.append(self.series)
        self.x_index = 0
        self.add(data)
        if title:
            self.set_title(title)
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)
        self.instance.send(self.id, 'clearTickStrategy', {'axis': self.default_x_axis.id})

    def add(self, data: list[list[int | float]]):
        """Add data to the chart.

        Args:
            data (list[list[int | float]]): List of Lists containing y-values.

        Returns:
            The instance of the class for fluent interface.
        """
        if np is None:
            raise ImportError("NumPy is not installed. Please install it to use this functionality.")
        if pd is None:
            raise ImportError("Pandas is not installed. Please install it to use this functionality.")

        if isinstance(data, pd.DataFrame):  # Pandas dataframe
            for column, values in data.items():
                sorted = np.sort(values)
                self.series.add(
                    start=self.x_index,
                    end=self.x_index + 1,
                    median=float(np.median(sorted)),
                    lower_quartile=float(np.percentile(sorted, 25)),
                    upper_quartile=float(np.percentile(sorted, 75)),
                    lower_extreme=float(sorted[0]),
                    upper_extreme=float(sorted[-1])
                )
                self.instance.send(self.id, 'customTick', {
                    'axis': self.default_x_axis.id,
                    'position': self.x_index + 0.5,
                    'content': column
                })
                self.x_index += 2
            return self
        elif isinstance(data, dict):  # Dictionary
            for key, value in data.items():
                sorted = np.sort(value)
                self.series.add(
                    start=self.x_index,
                    end=self.x_index + 1,
                    median=float(np.median(sorted)),
                    lower_quartile=float(np.percentile(sorted, 25)),
                    upper_quartile=float(np.percentile(sorted, 75)),
                    lower_extreme=float(sorted[0]),
                    upper_extreme=float(sorted[-1])
                )
                self.instance.send(self.id, 'customTick', {
                    'axis': self.default_x_axis.id,
                    'position': self.x_index + 0.5,
                    'content': key
                })
                self.x_index += 2
            return self
        elif not isinstance(data, list):  # List
            data = [data]
        label_index = 1
        for i in data:
            sorted = np.sort(i)
            self.series.add(
                start=self.x_index,
                end=self.x_index + 1,
                median=float(np.median(sorted)),
                lower_quartile=float(np.percentile(sorted, 25)),
                upper_quartile=float(np.percentile(sorted, 75)),
                lower_extreme=float(sorted[0]),
                upper_extreme=float(sorted[-1])
            )
            #self.instance.send(self.id, 'customTick', {
            #    'axis': self.default_x_axis.id,
            #    'position': self.x_index + 0.5,
            #    'content': str(label_index)
            #})
            self.x_index += 2
            label_index += 1

        return self
