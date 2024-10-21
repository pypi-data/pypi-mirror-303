from textual.binding import Binding
from textual.widgets import Input


class InputInterval(Input):
    BINDINGS = [
        Binding("down", "app.focus_next", "Focus Next", show=False),
        # Super Bindings
        Binding("left", "cursor_left", "Move cursor left", show=False),
        Binding("ctrl+left", "cursor_left_word", "Move cursor left a word", show=False),
        Binding("right", "cursor_right", "Move cursor right", show=False),
        Binding("ctrl+right", "cursor_right_word", "Move cursor right a word", show=False),
        Binding("backspace", "delete_left", "Delete character left", show=False),
        Binding("home,ctrl+a", "home", "Go to start", show=False),
        Binding("end,ctrl+e", "end", "Go to end", show=False),
        Binding("delete,ctrl+d", "delete_right", "Delete character right", show=False),
        Binding("enter", "submit", "Submit", show=False),
        Binding("ctrl+w", "delete_left_word", "Delete left to start of word", show=False),
        Binding("ctrl+u", "delete_left_all", "Delete all to the left", show=False),
        Binding("ctrl+f", "delete_right_word", "Delete right to start of word", show=False),
        Binding("ctrl+k", "delete_right_all", "Delete all to the right", show=False),
    ]

    def __init__(self, callback, interval=1, **kw):
        super().__init__(**kw)
        self.callback = callback
        self.last_value = ''
        self.timer = self.set_interval(interval, self.check)

    def check(self):
        if self.value != self.last_value:
            self.last_value = self.value
            self.callback()
