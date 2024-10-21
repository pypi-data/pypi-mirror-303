from __future__ import annotations

from lightningchart import conf, Themes
from lightningchart.charts import ChartWithSeries, ChartWithXYAxis
from lightningchart.charts.chart_xy import ChartXY
from lightningchart.instance import Instance
from lightningchart.series.area_series import AreaSeries, AreaSeriesBipolar
from lightningchart.series.area_range_series import AreaRangeSeries

try:
    import pandas as pd
except ImportError:
    pd = None


class StackedAreaChart(ChartXY):
    """The stacked charts are a popular visual aid used for categorizing
    and comparing the parts of a whole using different colors to distinguish the categories.
    """

    def __init__(
            self,
            data=None,
            theme: Themes = Themes.White,
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            license: str = None,
            license_information: str = None,
    ):
        """Create a stacked area chart.

        Args:
            data: List of lists containing y values.
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

        if title:
            self.set_title(title)
        if xlabel:
            self.get_default_x_axis().set_title(xlabel)
        if ylabel:
            self.get_default_y_axis().set_title(ylabel)
        if data is not None:
            self.add(data)

    def add(self, data: list[list[int | float]]):
        """Add data to the chart.

        Args:
            data (list[list[int | float]]): List of lists containing y values.

        Returns:
            The instance of the class for fluent interface.
        """
        for i in range(len(data)):
            if i == 0:
                new_series = AreaSeriesBipolar(self).add(y=data[i])
                self.series_list.append(new_series)
            else:
                area_range_data = []
                for j in range(len(data[i])):
                    area_range_data.append({
                        'position': j,
                        'high': data[i][j],
                        'low': data[i - 1][j]
                    })
                new_series = AreaRangeSeries(self).add_dict_data(area_range_data)
                self.series_list.append(new_series)


        if pd is None:
            raise ImportError("Pandas is not installed. Please install it to use this functionality.")

        if isinstance(data, pd.DataFrame):  # Pandas dataframe
            i = 0
            for column, values in data.items():
                if i == 0:
                    new_series = AreaSeriesBipolar(self).add(y=values).set_name(column)
                    self.series_list.append(new_series)
                    below = values
                else:
                    area_range_data = []
                    for j in range(len(values)):
                        area_range_data.append({
                            'position': j,
                            'high': float(values[j]),
                            'low': float(below[j])
                        })
                    new_series = AreaRangeSeries(self).add_dict_data(area_range_data).set_name(column)
                    self.series_list.append(new_series)
                    below = values
                i += 1
            return self
        elif isinstance(data, dict):  # Dictionary
            i = 0
            for key, value in data.items():
                if i == 0:
                    new_series = AreaSeriesBipolar(self).add(y=value).set_name(key)
                    self.series_list.append(new_series)
                    below = value
                else:
                    area_range_data = []
                    for j in range(len(value)):
                        area_range_data.append({
                            'position': j,
                            'high': value[j],
                            'low': below[j]
                        })
                    new_series = AreaRangeSeries(self).add_dict_data(area_range_data).set_name(key)
                    self.series_list.append(new_series)
                    below = value
                i += 1
            return self
        elif not isinstance(data, list):  # List
            data = [data]
        for i in range(len(data)):
            if i == 0:
                new_series = AreaSeriesBipolar(self).add(y=data[i])
                self.series_list.append(new_series)
            else:
                area_range_data = []
                for j in range(len(data[i])):
                    area_range_data.append({
                        'position': j,
                        'high': data[i][j],
                        'low': data[i - 1][j]
                    })
                new_series = AreaRangeSeries(self).add_dict_data(area_range_data)
                self.series_list.append(new_series)
