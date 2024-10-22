from textual.screen import Screen
from textual.widgets import Static, Input, Header, Footer
from textual import events, on, work
from textual.app import ComposeResult
import pandas as pd
from .confmscn import Confirm_Screen
from .revertpaxmodule import apiPaxFunctions, findGroup
from .functionsScreen import FunctionsScreen
from. tui_exceptions import TerminalNotFoundError

class Scan_qr(Screen):
    """QR SCANNER"""
    BINDINGS = [("escape", "app.pop_screen", "BACK")]

    def __init__(self):
        self.serialNoList = []
        self.copySerialNoList = self.serialNoList
        super().__init__()
    

    def compose(self) -> ComposeResult:
        yield Static("PlEASE SCAN QR CODE TO BEGIN", classes="question" )
        yield Input(placeholder=">>>>")
        yield Footer()
    @on(Input.Submitted)
    @work
    async def fix_qr(self) -> None:
        self.l = self.query_one(Input).value
        self.disabled = True
        self.serialNoList = eval(self.l)  # Assuming the QR code contains a list of serial numbers
        sndf = pd.DataFrame({"serialNo":self.serialNoList})
        if await self.app.push_screen_wait(Confirm_Screen(f"Are these terminals you wish to activate\n{self.serialNoList}?")):
            self.notify("SEARCHING>>>")
            try:
                self.group = await findGroup(self.serialNoList)
                self.app.push_screen(FunctionsScreen(pd.DataFrame(self.group)))
            except TerminalNotFoundError as e:
                # Display error message and prompt for registration
                not_found_terminals = [e.serial_no]
                self.copySerialNoList.remove(e.serial_no)
                try:
                    self.group = await findGroup(self.copySerialNoList)
                except TerminalNotFoundError as e:
                    not_found_terminals.append(e.serial_no)
                    self.app.notify(str(len(not_found_terminals)))
                    if len(not_found_terminals) == 1:
                        error_message = f"Terminal not found: {not_found_terminals[0]}\nRegister now?"
                    else:
                        error_message = f"Terminals not found: {', '.join(not_found_terminals)}\nRegister now?"   
                    if await self.app.push_screen_wait(Confirm_Screen(error_message)):
                        func = apiPaxFunctions()
                        add = await func.createTerminals(serialNoList=not_found_terminals)
                        self.app.notify(f"{not_found_terminals} added successfully") 
                        self.group = await findGroup(sndf['serialNo'])
                        df = pd.DataFrame(self.group)
                        self.app.push_screen(FunctionsScreen(df))
