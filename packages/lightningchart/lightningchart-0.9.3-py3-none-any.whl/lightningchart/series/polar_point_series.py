from __future__ import annotations

import lightningchart
from lightningchart.charts import Chart
from lightningchart import Themes
from lightningchart.series import Series2D, SeriesWith2DPoints


class PolarPointSeries(Series2D, SeriesWith2DPoints):
    """Series type for visualizing polar point data."""

    def __init__(
            self,
            chart: Chart,
            theme: Themes = Themes.White,
            name: str = None,
    ):
        Series2D.__init__(self, chart)
        self.instance.send(self.id, 'addPointSeries', {
            'chart': self.chart.id,
            'theme': theme.value,
            'name': name,
        })

    def set_data(self, data: list[dict]):
        """Set the data for the series.

        Args:
            data (list[dict]): A list of dictionaries, each containing:
                - 'angle' (float): The angle in degrees.
                - 'amplitude' (float): The amplitude at that angle.

        Example:
            series.set_data([
                {'angle': 0, 'amplitude': 5},
                {'angle': 90, 'amplitude': 10},
                {'angle': 180, 'amplitude': 7.5},
                {'angle': 270, 'amplitude': 3},
            ])

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setData', {'data': data})
        return self

    def set_name(self, name: str):
        """Sets the name of the series for Legend

        Args:
            name (str): Name of the component.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setName', {'name': name})
        return self
    
    def set_auto_scrolling_enabled(self, enabled: bool = True):
        """Set whether series is taken into account with automatic scrolling and fitting of attached axes.

        Args:
            enabled: Boolean flag.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setAutoScrollingEnabled', {'enabled': enabled})
        return self

    def set_point_alignment(self, x: float, y: float):
        """Set alignment of points. Defaults to center { x: 0, y: 0 }.

        Args:
            x: x-axis alignment in range [-1, 1]
            y: y-axis alignment in range [-1, 1]

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setPointAlignment', {'x': x, 'y': y})
        return self
