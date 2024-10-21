from textual import on
from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Label

from tx_widgets.select_widgets import (
    select_exact,
    select_contain,
    select_insensitive,
    select_start,
    select_end,
    select_rex,
    select_fuzzy,
    select_multi,
    selectors,
    SelectWidget,
    SelectExact,
    SelectContain,
    SelectInsensitive,
    SelectStart,
    SelectEnd,
    SelectRex,
    SelectFuzzy,
    SelectMulti,
)


words = [
    'Banane',
    'Trompette',
    'Kiwi',
    'Raquette',
    'Bougie',
    'Pasteque',
]


class WidgetTest(App):
    CSS = '''
        Select {
            width: 1fr;
        }
    '''
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]
    def compose(self):
        with Horizontal():
            yield SelectMulti(words)
            with Vertical():
                yield Label('', id='highlighted')
                yield Static('', id='selected')

    @on(SelectWidget.UpdateHighlighted)
    def highlight(self, event):
        event.stop()
        self.query_one('#highlighted').update(event.value)

    @on(SelectWidget.UpdateSelected)
    def select(self, event):
        event.stop()
        self.query_one('#selected').update(event.value)


def app_test():
    WidgetTest().run()


def test_exact():
    assert select_exact(words, 'kiwi') == []
    assert select_exact(words, 'Kiwi') == ['Kiwi']


def test_contain():
    assert select_contain(words, 'eppe') == []
    assert select_contain(words, 'ette') == ['Trompette', 'Raquette']


def test_insensitive():
    assert select_contain(words, 'tromp') == []
    assert select_insensitive(words, 'tromp') == ['Trompette']


def test_start():
    assert select_start(words, 'tromp') == []
    assert select_start(words, 'Tromp') == ['Trompette']


def test_end():
    assert select_end(words, 'eppe') == []
    assert select_end(words, 'ette') == ['Trompette', 'Raquette']


def test_rex():
    assert select_rex(words, 'ette') == ['Trompette', 'Raquette']
    assert select_rex(words, r'[^e]$') == ['Kiwi']
    assert select_rex(words, r'a.*t.*e') == ['Raquette', 'Pasteque']


def test_fuzzy():
    assert select_fuzzy(words, 'ate') == ['Pasteque', 'Raquette']


def test_multi():
    patterns = r'''
        tromp
        Tromp
        eppe
        ette
        ate
        [^e]$
        a.*t.*e
    '''.split()
    for pattern in patterns:
        for method, selector in selectors.items():
            assert select_multi(words, f'{method}:{pattern}') == selector(words, pattern)


if __name__=='__main__': app_test()
