from pathlib import Path
from typing import Iterable
import time
from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Static, Label, Button, LoadingIndicator
from textual.screen import Screen, ModalScreen
from textual.containers import Container, Horizontal, VerticalScroll, Grid
from textual import events, on, work
from textual.reactive import reactive
import pandas as pd
from DFTable import DataFrameTable
from textual.message import Message
import os
import datetime

def read_xl(file):
    """Imports Excel spreadsheet"""

    Erequire_cols = [0]
    df = pd.read_excel(file, skiprows=[0], usecols=Erequire_cols,index_col=None,dtype=object)
    serial_list = df['Serial No'].astype("str").values
    tid_list = get_term_ids_v2(list(serial_list)) # type: ignore
    tid_list.to_excel("new_file2.xlsx")

    return tid_list

class PathLabel(Label):
    path: reactive[str] = reactive("None")

    def render(self) -> str:
        return f"Selected path: {self.path}"

class GroupLabel(Label):
    group: reactive [str] = reactive("None")

    def render(self) -> str:
        return f"Selected group: {self.group}"

class FilePicker(DirectoryTree):
    
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if not path.name.startswith(".")] 

class GroupButton(Button):
    
    """Button For PaxGroups"""

    class Selected(Message):

        def __init__(self,group:str) -> None:
            self.group = group
            super().__init__()

    def __init__(self,group:str) -> None:
        self.group = group
        super().__init__()
    
    def on_mount(self) -> None:
        self.styles.margin = (1, 2)
        self.styles.content_align = ("center", "middle")

    def on_button_pressed(self) -> None:
        self.post_message(self.Selected(self.group))
    
    
    
    def render(self) -> str:
        return str(self.group)



class Confirm_Screen(ModalScreen[bool]):
    CSS_PATH = "src/textual_pax/css_lib/cofirm_screen.tcss"

    def __init__(self, message:str):
        self.message = message
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Grid(
            Static(self.message, id="question"),
            Button("Cancel", id="cancel", variant="error"),
            Button("OK", id="ok", variant="success")
            ,id="confirmscreen"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ok":
            self.dismiss(True)
        else:
            self.dismiss(False)

class GroupSelection(Screen):

    def __init__(self, question) -> None:
        self.question = question
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(self.question)
        yield Button("Group 1", id="Group_1")
        yield Button("Group 2", id="Group_2")
        yield Button("Group 3", id="Group_3")
        yield Button("Group 4", id="Group_4")
        yield Button("Group 5", id="Group_5")
        yield Button("Group 6", id="Group_6")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(str(event.button.id))

     

class PaxGroup(Screen):

    def __init__(self,file: str) -> None:
        self.file = file
        super().__init__()

    def compose(self) -> ComposeResult:
        yield DataFrameTable()
        yield Static("CREATE PAX GROUP?")
        yield Button("No", id="no", variant="error")
        yield Button("Yes", id="yes", variant="success")
   
    def on_mount(self):
        """Imports Excel spreadsheet"""
        Erequire_cols = [0]
        df = pd.read_excel(self.file, skiprows=[0], usecols=Erequire_cols,index_col=None,dtype=object)
        serial_list = df['Serial No'].astype("str").values
        self.tid_list = get_term_ids_v2(list(serial_list)) # type: ignore
        self.model_list = self.tid_list["label"]
        table = self.query_one(DataFrameTable)
        table.add_df(self.tid_list)
        
        self.loading = False
        self.tid_list.to_excel("again.xlsx")

        
    
    def handle_confirm(self, cancel:bool):
        """Callback for ConfirmScreen"""
        if cancel:
            self.dismiss()

    def accept_answer(self, group:str): 
        """Callback for GroupSelection screen"""
        self.notify(group)
    
        try:
            Current_Date = str(datetime.datetime.today().strftime('%m.%d.%Y.%H.%M'))
            path = f"Iface_Pax_Groups/{group}"
            os.makedirs(path)
            os.chdir(path)
            file_name = str(self.model_list[0]+Current_Date+group.removeprefix("Group_")+".pkl")
            
            self.tid_list.to_pickle(file_name)
            
        except OSError:
            self.app.push_screen(Confirm_Screen(message=f"{group} FILE EXISTS\nOverwirite Existing Group?"),callback=self.handle_confirm)


    @on(Button.Pressed, "#yes")
    #@work
    def choose_group_id(self, group:str):
        self.app.push_screen(GroupSelection("Please Assign Group ID"),self.accept_answer)

class Selector_Widget_Screen(Screen):

    def compose(self) -> ComposeResult:
        
        
        yield Static("PLEASE SELECT FILE TO IMPORT")
        yield FilePicker(str(os.curdir))
        yield PathLabel()
        

    @on(FilePicker.FileSelected)
    @work
    async def show_path(self, event: DirectoryTree.FileSelected) -> None:
        self.notify(str(event.path))
        if await self.app.push_screen_wait(Confirm_Screen(message="IS THIS THE FILE TO UPLOAD?")): #type: ignore
            self.app.query_one(PathLabel).path = str(event.path)
            self.app.push_screen(PaxGroup(str(event.path)))
        else: self.app.query_one(PathLabel).path = str(None)
    
    def action_confirm_file(self):
        """confirm file"""
        def use_file(use: bool):
            if use:
                self.app.pop_screen()

class Selector(App):
    
    def on_mount(self) -> None:
        self.push_screen(Selector_Widget_Screen())

if __name__ == "__main__":
    app = Selector()
    app.run()


