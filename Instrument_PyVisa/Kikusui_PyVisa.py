import pyvisa
from Instrument_PyVisa.Basic_PyVisa import Basic_PyVisa


# Only Kikusui PBZ20-20 specified PyVISA command should be placed here.
class Kikusui_PyVisa(Basic_PyVisa):
    def __init__(self):
        super().__init__()
        pass

    def measure_voltage(self):
        pass
