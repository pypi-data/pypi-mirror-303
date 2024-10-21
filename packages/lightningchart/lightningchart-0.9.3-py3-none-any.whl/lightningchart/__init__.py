"""
**LightningChart Python.**

**Available charts**:
    * ChartXY
    * Chart3D
    * BarChart
    * PolarChart
    * SpiderChart
    * PieChart
    * GaugeChart
    * FunnelChart
    * PyramidChart
    * MapChart
    * TreeMapChart
    * LineChart
    * LineChart3D
    * ScatterChart
    * ScatterChart3D
    * Heatmap
    * Surface3D
    * AreaChart
    * StackedAreaChart
    * BoxPlot
    * Box3D
    * Dashboard
"""

from lightningchart.conf import LICENSE_KEY
from lightningchart.utils import *
from lightningchart.charts.chart_xy import ChartXY
from lightningchart.charts.chart_3d import Chart3D
from lightningchart.charts.dashboard import Dashboard
from lightningchart.charts.bar_chart import BarChart
from lightningchart.charts.spider_chart import SpiderChart
from lightningchart.charts.pie_chart import PieChart
from lightningchart.charts.gauge_chart import GaugeChart
from lightningchart.charts.funnel_chart import FunnelChart
from lightningchart.charts.pyramid_chart import PyramidChart
from lightningchart.charts.map_chart import MapChart

from lightningchart.charts.line_chart import LineChart
from lightningchart.charts.line_chart_3d import LineChart3D
from lightningchart.charts.scatter_chart import ScatterChart
from lightningchart.charts.scatter_chart_3d import ScatterChart3D
from lightningchart.charts.heat_map import Heatmap
from lightningchart.charts.surface_3d import Surface3D
from lightningchart.charts.area_chart import AreaChart
from lightningchart.charts.stacked_area_chart import StackedAreaChart
from lightningchart.charts.box_plot import BoxPlot
from lightningchart.charts.box_3d import Box3D
from lightningchart.charts.treemap_chart import TreeMapChart
from lightningchart.charts.polar_chart import PolarChart


def set_license(license_key: str, license_information: dict[str, str] = None):
    conf.LICENSE_KEY = license_key
    if license_information:
        conf.LICENSE_INFORMATION = license_information
