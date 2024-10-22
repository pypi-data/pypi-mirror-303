from textual.widgets import MarkdownViewer, Button, Footer, Header, Static
from textual.app import  ComposeResult
from textual.screen import Screen
from textual.widgets import Footer
from textual.containers import Container, VerticalScroll, Horizontal, Grid
from textual import  on, work
import pandas as pd
from .revertpaxmodule import apiPaxFunctions, PushConfigs, updateTerminals 
from .ti_labels_iccid import create_pdf
from .confmscn import Confirm_Screen
from .singleTerminal import parseList




def update_table(appdata):
        headers = "| ".join(appdata[0].keys()) + " \n| --------------- | --------------- | --------------- | --------------- | --------------- |"
        rows = "\n|".join(["|".join(str(value) for value in item.values()) + "|" for item in appdata])
        content = f"## Installed Applications\n\n|{headers} \n|{rows}"
        return content

def format_terminal_details(termDetails:dict, appdata:list):

    text = ""
    text += "## Basic Info\n\n"
    for key, value in termDetails.items():
        if key == "serialNo":
            text += f"**Serial No:** {value}\n"
    for key, value in termDetails.items(): 
            if key !="serialNo":
                text += f"* {key}: {value}\n"
    text += update_table(appdata) 
    return text

class TerminalDetailsScreen(Screen):
    
    BINDINGS = [("escape", "app.pop_screen", "BACK")]
    CSS_PATH = "css_lib/singleTermDetails.tcss"
    
    def __init__(self,details:tuple):

        self.termdetails = details[0]
        self.df = pd.DataFrame(details[0])
        self.appdata = details[1]
        self.markdown = format_terminal_details(*self.termdetails,self.appdata)
        self.button_list = [
            {'name':'Reset Terminal', 'id': 'reset', 'classes':'gtask-buttons'},
            {'name':'Activate Terminal','id':'activate','classes':'gtask-buttons'},
            {'name':'Deactivate','id':'deactivate','classes':'gtask-buttons'},
            {'name':'Delete', 'id':'delete', 'classes':'gtask-buttons'},
            {'name':'Refresh Terminal Detials','id':'details','classes':'gtask-buttons'},
            {'name':'Create Label', 'id':'labels', 'classes':'gtask-buttons'}
        ]
        self.op = apiPaxFunctions()
        self.configop = PushConfigs()
        self.operations = {
            "activate": self.op.activateTerminals,
            "details": self.op.startPaxGroup,
            "deactivate": self.op.disableTerminals, 
            "move": None,
            "delete": self.op.deleteTerminals,
            "reset": updateTerminals,
            "labels": create_pdf,
            "payanywhere": self.configop.pushPAConfig,
            "broadpos":self.configop.pushBroadPosEPX,
            "other": self.configop.pushBroadPos_nonEPX
        }
        self.functionDict = {}
        super().__init__()

    def compose(self)-> ComposeResult:
        yield Header(name='PaxTools')
        with Container(id="app-grid"):
            with VerticalScroll(id = "top-pane"):
                yield MarkdownViewer(markdown=self.markdown,show_table_of_contents= True, id="mkdn") 
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

    @on(Button.Pressed)
    @work
        
    async def do_stuff(self, event: Button.Pressed):
        operation = self.operations.get(event.button.id)  # type: ignore
        if await self.app.push_screen_wait(Confirm_Screen("Please confirm terminal network connection and open PaxStore client on device.")):
            result = await operation(idList = self.df['id'], serialNoList = self.df['serialNo'], df = self.df)  # type: ignore
            self.notify(str(result))
            if event.button.id == "details":
                resp = await parseList(self.df['serialNo'])
                updateTermDetails = resp[0]
                updateAPKinfo = resp[1]
                self.markdown=format_terminal_details(*updateTermDetails,updateAPKinfo)  