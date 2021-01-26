import pyvisa
from Instrument_PyVisa.Basic_PyVisa import Basic_PyVisa


# Only Kikusui PBZ20-20 specified PyVISA command should be placed here.
class Kikusui_PyVisa(Basic_PyVisa):
    def __init__(self):
        super().__init__()

    def set_polarity(self, polarity="UNIP"):
        try:
            self.inst.write(f"FUNC:POL {polarity}")
        except:
            print(f"Unable to set Polarity --> {polarity}")

    def set_mode(self, string_mode="CV"):
        try:
            self.inst.write(f"FUNC:MODE {string_mode}")
            print(f"Mode set to {string_mode}")
        except:
            print(f"Unable to set Mode --> {string_mode}")

    def set_output_voltage(self, output_voltage=0):
        try:
            self.inst.write(f"VOLT {output_voltage}")
        except:
            print(f"Unable to set VOUT --> {output_voltage}")

    def set_voltage_limit(self, output_voltage_limit=1):
        try:
            self.inst.write(f"VOLT:LIM:UPP {output_voltage_limit}")
            self.inst.write(f"VOLT:LIM:LOW -{output_voltage_limit}")
        except:
            print(f"Unable to set VOUT Limit --> {output_voltage_limit}")

    def set_current_limit(self, output_current_limit=1):
        try:
            self.inst.write(f"CURR:LIM:UPP {output_current_limit}")
            self.inst.write(f"CURR:LIM:LOW -{output_current_limit}")
        except:
            print(f"Unable to set Current Limit --> {output_current_limit}")

    def turn_on_output(self, on_off=0):
        try:
            self.inst.write(f"OUTP {on_off}")
        except:
            print(f"Unable to set OUTP --> {on_off}")


if __name__ == "__main__":
    rm = Kikusui_PyVisa()
    rm.connect_device('USB0::0x0B3E::0x1012::XF001773::0::INSTR')
    rm.set_mode("CV")
    rm.set_polarity("BIP")
    rm.set_output_voltage(5)
    rm.set_voltage_limit(10)
    rm.set_current_limit(1)
    rm.turn_on_output(1)