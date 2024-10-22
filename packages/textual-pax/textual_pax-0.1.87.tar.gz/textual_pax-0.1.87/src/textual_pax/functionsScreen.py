import pandas as pd
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Button, Header, Footer 
from textual import  on, work
from .DFTable import DataFrameTable
from .revertpaxmodule import apiPaxFunctions, PushConfigs, resetTerminals
from .ti_labels_iccid import create_pdf
from textual.containers import Container, VerticalScroll
from .confmscn import Confirm_Screen
from .singleTerminal import parseList
from .SingleTermDetailsScreen import TerminalDetailsScreen


class FunctionsScreen(Screen):

    BINDINGS = [("escape", "app.pop_screen", "BACK")]
    CSS_PATH = "css_lib/group_gunctions.tcss"

    def __init__(self, df:pd.DataFrame) -> None:
        self.df = df
        self.button_list = [
            {'name': 'Reset Group', 'id': 'reset', 'classes':'gtask-buttons'},
            {'name':'Activate Group','id':'activate','classes':'gtask-buttons'},
            {'name':'Deactivate','id':'deactivate','classes':'gtask-buttons'},
            {'name':'Delete Group', 'id':'delete', 'classes':'gtask-buttons'},
            {'name':'Refresh Terminal Detials','id':'details','classes':'gtask-buttons'},
            {'name':'Create Ticket Labels', 'id':'labels', 'classes':'gtask-buttons'}
        ]
        self.op = apiPaxFunctions()
        self.configop = PushConfigs()
        self.operations = {
            "activate": self.op.activateTerminals,
            "details": self.op.startPaxGroup,
            "deactivate": self.op.disableTerminals, 
            "delete": self.op.deleteTerminals,
            "reset": resetTerminals,
            "labels": create_pdf,
            "payanywhere": self.configop.paPushByReseller,
            "broadpos":self.configop.pushBroadPosEPX,
            "other": self.configop.pushBroadPos_nonEPX
        }
        self.functionDict = {}
        super().__init__()
    
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id = "top-pane"):
                yield DataFrameTable()
            with VerticalScroll(id = "bottom-left"):
                yield Static("Available Tasks", classes="titleheader")
                for button in self.button_list:
                    yield Button(button['name'], id=button['id'], classes=button['classes']) # type: ignore
            with VerticalScroll(id= "bottom-right"):
                yield Static("Configuration Tasks", classes="titleheader")
                yield Button("Config for PayAnywhere", id="payanywhere", classes="buttons")
                yield Button("Config for BroadPOS - EPX", id="broadpos",classes="buttons")
                yield Button("Config for BroadPOS - Not EPX", id ="other", classes="buttons")
        yield Footer()
    async def on_mount(self):   
        """if self.df == None:
            self.mdf = pd.read_pickle("/Users/scottjamnik/python-to-google-sheets/E600M04.29.2024.14.051.pkl")
        else: self.mdf = pd.DataFrame(self.df)"""

        self.table = self.query_one(DataFrameTable)
        self.table.add_df(self.df)
        self.app.notify(str(self.df))

    @on(Button.Pressed)
    @work
    async def do_stuff(self, event: Button.Pressed):
        operation = self.operations.get(event.button.id)  # type: ignore
        if await self.app.push_screen_wait(Confirm_Screen("Please confirm terminal network connection and open PaxStore client on device.")):
            result = await operation(idList = self.df['id'], serialNoList = self.df['serialNo'], df = self.df)  # type: ignore
            self.notify(str(result))
            refresh = await self.op.startPaxGroup(self.df['serialNo'])
            self.ndf = pd.DataFrame(refresh).drop_duplicates(subset=["serialNo"])
            self.table.update_df(self.ndf)
            self.df = self.ndf
    
    @work
    @on(DataFrameTable.CellSelected)
    async def note_cell(self, event:DataFrameTable.CellSelected):
        if event.value in self.df['serialNo'].values:
            self.app.notify(str(event.value))
            if await self.app.push_screen_wait(Confirm_Screen(message=f"View {event.value} Terminal Page?")):
                dList = [event.value]
                termDetails = await parseList(dList)
                self.app.notify(str(termDetails))            
                self.app.push_screen(TerminalDetailsScreen(termDetails))   