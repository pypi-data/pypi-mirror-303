from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Placeholder, Input, Label, TextArea, Header,Footer, MarkdownViewer
from textual.screen import Screen, ModalScreen
from textual.containers import Container, Horizontal, VerticalScroll, Grid
from confmscn import Confirm_Screen
from textual import events, on, work
import pandas as pd
from revertpaxmodule import *
from DFTable import DataFrameTable


serialNo = "082214439"

EXAMPLE_MARKDOWN = f"""\
# {serialNo}

This is an example of Textual's `MarkdownViewer` widget.


## Features

Markdown syntax and extensions are supported.

- Typography *emphasis*, **strong**, `inline code` etc.
- Headers
- Lists (bullet and ordered)
- Syntax highlighted code blocks
- Tables!

## Tables

Tables are displayed in a DataTable widget.

| Name            | Type   | Default | Description                        |
| --------------- | ------ | ------- | ---------------------------------- |
| `show_header`   | `bool` | `True`  | Show the table header              |
| `fixed_rows`    | `int`  | `0`     | Number of fixed rows               |
| `fixed_columns` | `int`  | `0`     | Number of fixed columns            |
| `zebra_stripes` | `bool` | `False` | Display alternating colors on rows |
| `header_height` | `int`  | `1`     | Height of header row               |
| `show_cursor`   | `bool` | `True`  | Show a cell cursor                 |


## Code Blocks

Code blocks are syntax highlighted, with guidelines.

```python
class ListViewExample(App):
    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
        )
        yield Footer()
```
"""


class MarkdownExampleApp(App):
    def compose(self) -> ComposeResult:
        yield MarkdownViewer(EXAMPLE_MARKDOWN, show_table_of_contents=True)


if __name__ == "__main__":
    app = MarkdownExampleApp()
    app.run()

