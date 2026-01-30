import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import app


def test_header_is_present():
    layout = app.app.layout
    header = layout.children[0]

    assert header.children == "Impact of Pink Morsel Price Increase on Sales"


def test_visualisation_is_present():
    layout = app.app.layout

    graph_div = layout.children[-1]
    graph = graph_div.children[0]

    assert graph.id == "sales-line-chart"


def test_region_picker_is_present():
    layout = app.app.layout

    control_div = layout.children[1]
    radio_items = control_div.children[1]

    assert radio_items.id == "region-selector"
