from re import compile
from subprocess import call

from pygments import lexers
from pygments.util import ClassNotFound
from rich.syntax import Syntax
from rich.traceback import Traceback
from textual import on
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Static
from tx_widgets import OptionListRight


class FilesScreen(Screen):
    CSS = '''
        #files{
            width: 5fr;
        }
        #preview{
            width: 7fr;
        }
    '''
    BINDINGS = [
        ("escape, left", "exit", "Exit"),
    ]

    def compose(self):
        with Horizontal():
            self.files = OptionListRight(id='files')
            self.files.width = 5
            yield self.files
            preview = Static(id="preview", expand=True)
            preview.width = 7
            yield preview

    def on_screen_resume(self, event):
        self.root, self.paths = self.app.files_get()
        self.files.clear_options()
        self.files.add_options(self.paths)
        self.files.focus()
        self.files.action_first()
        # app.config should be a pybrary.Config
        self.theme = self.app.config.syntax_theme or 'lightbulb'

    def on_key(self, event):
        key = event.key
        files = self.files
        preview = self.query_one('#preview', Static)
        if key == "minus" and files.width > 3:
            files.width -= 1
            preview.width += 1
        if key == "plus" and preview.width > 3:
            preview.width -= 1
            files.width += 1
        files.styles.width = f'{files.width}fr'
        preview.styles.width = f'{preview.width}fr'

    @on(OptionListRight.OptionHighlighted, '#files')
    def highlight(self, event):
        event.stop()
        preview = self.query_one("#preview", Static)
        height = self.size.height
        path = event.option.prompt
        path = f'{self.root}/{path}'
        rex = compile(self.app.files_search).search
        try:
            content = open(path).read()
            lines = content.split('\n')
            for idx, line in enumerate(lines):
                if rex(line): break
            first = idx -10 if idx > 10 else 0
            last = first + height
            selection = '\n'.join(lines[:last])
        except Exception as x:
            selection = f'{x}'
            file_type = None
        try:
            lexer = lexers.guess_lexer_for_filename(path, content)
            file_type = lexer.name
        except ClassNotFound:
            file_type = None
        try:
            syntax = Syntax(
                selection,
                file_type,
                line_range = (first, None),
                highlight_lines = (idx+1, ),
                line_numbers = True,
                word_wrap = False,
                indent_guides = False,
                theme = self.theme,
            )
            preview.update(syntax)
            self.query_one("#preview").scroll_home(animate=False)
        except Exception as x:
            preview.update(Traceback(theme=self.theme, width=None))
            self.sub_title = "ERROR"

    @on(OptionListRight.OptionSelected, '#files')
    def select(self, event):
        event.stop()
        if selected := event.option.prompt:
            path = f'{self.root}/{selected}'
            with self.app.suspend():
                call(self.app.files_open.format(path=path).split())

    def action_exit(self):
        self.app.pop_screen()

