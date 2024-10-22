class TerminalNotFoundError(Exception):
    """Exception raised when a terminal is not found in PaxStore."""
    def __init__(self, serial_no):
        super().__init__(f"Terminal SN {serial_no} not found in PaxStore.")
        self.serial_no = serial_no