from __future__ import annotations

import lightningchart
from lightningchart.charts import Chart
from lightningchart.ui.axis import Axis
from lightningchart.series import Series2D, SeriesWithAddDataPoints, SeriesWithAddDataXY, SeriesWith2DLines, \
    SeriesWithDataCleaning, Series, BetaXYFeatures


class AreaSeries(
    Series2D,
    SeriesWithAddDataPoints,
    SeriesWithAddDataXY,
    SeriesWith2DLines,
    SeriesWithDataCleaning,
    BetaXYFeatures
):
    """Series for visualizing 2D areas."""

    def __init__(
            self,
            chart: Chart,
            data_pattern: str = None,
            colors: bool = False,
            lookup_values: bool = False,
            ids: bool = False,
            sizes: bool = False,
            rotations: bool = False,
            auto_sorting_enabled: bool = False,
            x_axis: Axis = None,
            y_axis: Axis = None,
    ):
        Series.__init__(self, chart)
        self.instance.send(self.id, 'areaSeries', {
            'chart': self.chart.id,
            'dataPattern': data_pattern,
            'colors': colors,
            'lookupValues': lookup_values,
            'ids': ids,
            'sizes': sizes,
            'rotations': rotations,
            'autoSortingEnabled': auto_sorting_enabled,
            'xAxis': x_axis,
            'yAxis': y_axis,
        })

    def set_fill_color(self, color: lightningchart.Color):
        """Set a fill color of the area.

        Args:
            color (Color): Color of the area.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setAreaFillStyle', {'color': color.get_hex()})
        return self


class AreaSeriesPositive(
    Series2D,
    SeriesWithAddDataPoints,
    SeriesWithAddDataXY,
    SeriesWith2DLines,
    SeriesWithDataCleaning
):
    """Series for visualizing a collection of progressive Points by filling the area between the points Y-values and a
    static baseline value. This type of AreaSeries only shows data that is above the baseline.
    """

    def __init__(
            self,
            chart: Chart,
            area_type: str = 'positive',
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send(self.id, 'areaSeriesOld', {
            'type': area_type,
            'chart': self.chart.id,
            'xAxis': x_axis,
            'yAxis': y_axis
        })

    def set_fill_color(self, color: lightningchart.Color):
        """Set a fill color of the area.

        Args:
            color (Color): Color of the area.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setSolidFillStyle', {'color': color.get_hex()})
        return self


class AreaSeriesNegative(
    Series2D,
    SeriesWithAddDataPoints,
    SeriesWithAddDataXY,
    SeriesWith2DLines,
    SeriesWithDataCleaning
):
    """Series for visualizing a collection of progressive Points by filling the area between the points Y-values and a
    static baseline value. This type of AreaSeries only shows data that is below the baseline.
    """

    def __init__(
            self,
            chart: Chart,
            area_type: str = 'negative',
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send(self.id, 'areaSeriesOld', {
            'type': area_type,
            'chart': self.chart.id,
            'xAxis': x_axis,
            'yAxis': y_axis
        })

    def set_fill_color(self, color: lightningchart.Color):
        """Set a fill color of the area.

        Args:
            color (Color): Color of the area.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setSolidFillStyle', {'color': color.get_hex()})
        return self


class AreaSeriesBipolar(
    Series2D,
    SeriesWithAddDataPoints,
    SeriesWithAddDataXY,
    SeriesWithDataCleaning
):
    """Series for visualizing a collection of progressive Points by filling the area between the points Y-values and a
    static baseline value.

    This type of AreaSeries shows data on both sides of the baseline, and it has individual styles for each side:
    positive and negative. Each side is also composed of the areas fill and border.
    """

    def __init__(
            self,
            chart: Chart,
            area_type: str = 'bipolar',
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send(self.id, 'areaSeriesOld', {
            'type': area_type,
            'chart': self.chart.id,
            'xAxis': x_axis,
            'yAxis': y_axis
        })

    def set_negative_fill_color(self, color: lightningchart.Color):
        """Set negative area style of Series.

        Args:
            color (Color): Color of the negative area.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setNegativeFillStyle', {'color': color.get_hex()})
        return self

    def set_negative_stroke(self, thickness: int | float, color: lightningchart.Color):
        """Set negative stroke style of Series.

        Args:
            thickness (int | float): Thickness of the stroke.
            color (Color): Color of the stroke.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setNegativeStrokeStyle', {'thickness': thickness, 'color': color.get_hex()})
        return self

    def set_positive_fill_color(self, color: lightningchart.Color):
        """Set positive area style of Series.

        Args:
            color (Color): Color of the positive area.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setPositiveFillStyle', {'color': color.get_hex()})
        return self

    def set_positive_stroke(self, thickness: int | float, color: lightningchart.Color):
        """Set positive stroke style of Series.

        Args:
            thickness (int | float): Thickness of the stroke.
            color (Color): Color of the stroke.

        Returns:
            The instance of the class for fluent interface.
        """
        self.instance.send(self.id, 'setPositiveStrokeStyle', {'thickness': thickness, 'color': color.get_hex()})
        return self
