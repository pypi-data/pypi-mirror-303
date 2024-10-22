from textual.screen import ModalScreen
from textual.app import  ComposeResult

from textual.widgets import Static, Input, Header,Footer
from textual import on, work
import pandas as pd
from .revertpaxmodule import apiPaxFunctions, findGroup  # Assuming this is in the same directory
from .confmscn import Confirm_Screen  # Assuming this is in the same directory
from .functionsScreen import FunctionsScreen
from .serialNoValidator import SerialNoValidator
from .tui_exceptions import TerminalNotFoundError

class Scan_serials(ModalScreen):

    """SERIAL NUMBER INPUT"""
    BINDINGS = [("escape", "app.pop_screen", "Go Back"),("0000", "", "Complete Entry"),("BKSPC", "", "Del item")]


    def __init__(self):
        self.serialNoList = []
        self.copySerialNoList = self.serialNoList
        self.validator = SerialNoValidator()  # Create an instance of the validator
        super().__init__()
    
    def compose(self) -> ComposeResult:
        
        yield Header(name='PaxTools')
        yield Static("SCAN OR TYPE SERIAL NUMBER. KEY IN 0000 TO COMPLETE. KEY IN BKSPC TO REMOVE PREVIOUS ENTRY:")
        yield Input(placeholder="S/N",validators=[self.validator])
        yield Footer()
    
    @on(Input.Submitted)
    @work
    async def update_serial_list(self):
        user_input = self.query_one(Input)
        serialNo = user_input.value
        self.serialNoList.append(serialNo)
        self.mount(Static(serialNo))
        if user_input.value == "BKSPC":
            self.serialNoList.pop()
            self.serialNoList.pop()
        if ":" in user_input.value:
            self.serialNoList.pop()
            self.app.bell()
        if user_input.value == "0000":
            self.disabled = True
            self.app.bell()
            self.serialNoList.pop()
            sndf = pd.DataFrame({"serialNo":self.serialNoList})
            if await self.app.push_screen_wait(Confirm_Screen(f"Are these terminals you wish to activate\n{self.serialNoList}?")):
                self.app.notify("SEARCHING...")
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
        user_input.clear()