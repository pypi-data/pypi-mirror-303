from textual.binding import Binding
from textual.widgets import OptionList


class OptionListRight(OptionList):
    # Add right key to select.
    BINDINGS = [
        Binding("down", "cursor_down", "Down", show=False),
        Binding("end", "last", "Last", show=False),
        Binding("enter,right", "select", "Select", show=False),
        Binding("home", "first", "First", show=False),
        Binding("pagedown", "page_down", "Page down", show=False),
        Binding("pageup", "page_up", "Page up", show=False),
        Binding("up", "cursor_up", "Up", show=False),
    ]


class OptionListRightLeft(OptionList):
    # Add right key to select and left key to focus previous.
    BINDINGS = [
        Binding("down", "cursor_down", "Down", show=False),
        Binding("end", "last", "Last", show=False),
        Binding("enter,right", "select", "Select", show=False),
        Binding("home", "first", "First", show=False),
        Binding("pagedown", "page_down", "Page down", show=False),
        Binding("pageup", "page_up", "Page up", show=False),
        Binding("up", "cursor_up", "Up", show=False),
        Binding("left", "app.focus_previous", "Focus Previous", show=False),
    ]


