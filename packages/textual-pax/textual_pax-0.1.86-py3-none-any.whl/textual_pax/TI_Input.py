
from textual.app import ComposeResult, App
from textual.widgets import Static, Button, Input, Header, Footer
from textual.screen import Screen, ModalScreen
from textual.containers import Grid
from .confmscn import Confirm_Screen
from textual import  on, work
from .revertpaxmodule import *
from .scan_serials import Scan_serials
from .functionsScreen import FunctionsScreen

class Select_QR_or_Barcode(ModalScreen[bool]):
    BINDINGS = [("escape", "app.pop_screen", "BACK")]
    CSS_PATH = "css_lib/cofirm_screen.tcss"

    def compose(self) -> ComposeResult:
        yield Grid(
            Static("Please select input method:", id= "question"),
            Button("SCAN QR CODE", name="QR", id="qr"),
            Button("SCAN BARCODE", name='BC', id='BC'),
            id="confirmscreen"
        )
        
    
    @on(Button.Pressed, "#qr")
    def push_qr_screen(self) -> None:
        self.app.push_screen(Scan_qr())

    @on(Button.Pressed, "#BC")
    def push_bcScreen(self) -> None:
        self.app.push_screen(Scan_serials())

class Scan_qr(Screen):
    """QR SCANNER"""
    BINDINGS = [("escape", "app.pop_screen", "BACK")]

    def compose(self) -> ComposeResult:
        yield Static("PlEASE SCAN QR CODE TO BEGIN", classes="question" )
        yield Input(placeholder=">>>>")
        yield Footer()
    
    @on(Input.Submitted)
    @work
    async def fix_qr(self) -> None:
        self.l = self.query_one(Input).value
        self.disabled = True
        self.serialList = eval(self.l)
        if await self.app.push_screen_wait(Confirm_Screen(f"Are these terminals you wish to activate\n{self.serialList}?")):
            self.notify("Activating>>>")

            apifun = apiPaxFunctions() 
            self.thing = await apifun.startPaxGroup(self.serialList)
            thing2 = await apifun.activateTerminals(apifun.idList)
            self.notify(str(thing2))
            self.app.push_screen(FunctionsScreen(self.thing))


class Input_app(App):

    def on_mount(self) -> None:
         self.push_screen(Select_QR_or_Barcode())
         

