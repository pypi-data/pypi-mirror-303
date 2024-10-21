from textual import on
from textual.containers import Vertical
from textual.message import Message
from textual.timer import Timer
from textual.widget import Widget
from textual.widgets import Input

from tx_widgets import InputInterval, OptionListRightLeft


class SelectWidget(Widget):
    DEFAULT_CSS = """
        #fuzzy_input{
            align-vertical: top;
            height: 1fr;
        }
        #fuzzy_entries{
            align-vertical: top;
            height: 9fr;
        }
    """

    class UpdateHighlighted(Message):
        def __init__(self, options, value):
            self.options = options
            self.value = value
            super().__init__()

        @property
        def control(self):
            return self.options

    class UpdateSelected(Message):
        def __init__(self, options, value):
            self.options = options
            self.value = value
            super().__init__()

        @property
        def control(self):
            return self.options

    def __init__(self, entries, **k):
        super().__init__(**k)
        self.entries = list(entries)
        self.highlighted = None
        self.selected = None

    def select(self, pattern):
        raise NotImplementedError

    def filter_entries(self, pattern=None):
        if pattern:
            return self.select(pattern)
        return self.entries

    def compose(self):
        with Vertical(id='fuzzy_container'):
            self.input = InputInterval(self.update, placeholder='fuzzy', id='fuzzy_input')
            self.options = OptionListRightLeft(*self.filter_entries(), id='fuzzy_entries')
            yield self.input
            yield self.options

    def update(self):
        self.options.clear_options()
        found = self.filter_entries(self.input.value)
        if found:
            self.options.add_options(found)
            self.selected = found[0]
            self.highlighted = found[0]
        else:
            self.selected = ''
            self.highlighted = ''
        self.post_message(self.UpdateHighlighted(self.options, self.highlighted))

    @on(Input.Submitted, '#fuzzy_input')
    def submit_event(self, event):
        event.stop()
        self.post_message(self.UpdateSelected(self, self.selected))

    @on(OptionListRightLeft.OptionHighlighted, '#fuzzy_entries')
    def highlight_event(self, event):
        event.stop()
        self.highlighted = event.option.prompt
        self.post_message(self.UpdateHighlighted(self.options, self.highlighted))

    @on(OptionListRightLeft.OptionSelected, '#fuzzy_entries')
    def select_event(self, event):
        event.stop()
        self.selected = event.option.prompt
        self.post_message(self.UpdateSelected(self.options, self.selected))
