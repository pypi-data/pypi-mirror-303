from PySide6.QtCharts import QChartView

from _support.basetests import BaseGuiTest
from guilib.multitabs.widget import MultiTabs
from guilib.searchsheet.widget import SearchSheet


class TestMultiTabs(BaseGuiTest):
    def test_ui(self) -> None:
        multi_tabs = MultiTabs()
        multi_tabs.add_double_box(SearchSheet(), QChartView(), 'first')
        multi_tabs.add_double_box(SearchSheet(), QChartView(), 'second')
        multi_tabs.add_double_box(SearchSheet(), QChartView(), '3rd')
        self.widgets.append(multi_tabs)
