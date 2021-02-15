import pyvisa
from Instrument_PyVisa.Basic_PyVisa import Basic_PyVisa
import time


# Only Kikusui PBZ20-20 specified PyVISA command should be placed here.
class Kikusui_PyVisa(Basic_PyVisa):
    def __init__(self):
        super().__init__()

    def set_polarity(self, polarity="UNIP"):
        try:
            self.inst.write(f"FUNC:POL {polarity}")
            return True
        except:
            print(f"Unable to set Polarity --> {polarity}")
            return False

    def set_mode(self, string_mode="CV"):
        try:
            self.inst.write(f"FUNC:MODE {string_mode}")
            print(f"Mode set to {string_mode}")
            return True
        except:
            print(f"Unable to set Mode --> {string_mode}")
            return False

    def set_output_voltage(self, output_voltage=0):
        try:
            self.inst.write(f"VOLT {output_voltage}")
            return True
        except:
            print(f"Unable to set VOUT --> {output_voltage}")
            return False

    def set_voltage_limit(self, output_voltage_limit=21):
        try:
            self.inst.write(f"VOLT:LIM:UPP {output_voltage_limit}")
            self.inst.write(f"VOLT:LIM:LOW -{output_voltage_limit}")
            return True
        except:
            print(f"Unable to set VOUT Limit --> {output_voltage_limit}")
            return False

    def set_current_limit(self, output_current_limit=1):
        try:
            self.inst.write(f"CURR:LIM:UPP {output_current_limit}")
            self.inst.write(f"CURR:LIM:LOW -{output_current_limit}")
            return True
        except:
            print(f"Unable to set Current Limit --> {output_current_limit}")
            return False

    def turn_on_output(self, on_off=0):
        try:
            self.inst.write(f"OUTP {on_off}")
            return True
        except:
            print(f"Unable to set OUTP --> {on_off}")
            return False

    def read_output_voltage(self):
        try:
            read_vout = self.inst.query_ascii_values("MEAS:VOLT?")
        except:
            read_vout = 999
            # print(f"Unable to set read output voltage")
        return read_vout

    def read_output_current(self):
        try:
            read_iout = self.inst.query_ascii_values("MEAS:CURR?")
        except:
            read_iout = 999
            # print(f"Unable to set read output voltage")
        return read_iout

    def clear_error(self):
        self.inst.write("*CLS")

    def set_store_seq_definition(self, SEQ_NUMBER, SEQ_STEPS, SEQ_NAME, SEQ_POLARITY, SEQ_MODE, SEQ_LOOP):
        try:
            self.inst.write(f'PROG:NAME {SEQ_NUMBER}')
            self.inst.write(f'PROG:EDIT:DEL')
            self.inst.write(f'PROG:EDIT:ADD {SEQ_STEPS}')
            self.inst.write(f'PROG:EDIT:TITL "{SEQ_NAME}"')
            self.inst.write(f'PROG:EDIT:FUNC:POL {SEQ_POLARITY}')
            self.inst.write(f'PROG:EDIT:FUNC:MODE {SEQ_MODE}')
            self.inst.write(f'PROG:EDIT:FUNC:LOOP {SEQ_LOOP}')
            return True
        except:
            print(f"Set Sequence Definition Error!")
            return False


class Kikusui_features:
    def __init__(self):
        self.kikusui = Kikusui_PyVisa()

    def connect_equipment(self, instrument_address):
        print(instrument_address)
        self.kikusui.connect_device(instrument_address)
        self.kikusui.turn_on_output(0)

    def disconnect_equipment(self):
        self.kikusui.disconnect_device()

    def set_cv_output(self, mode, polar, out_vol, out_vol_lim, out_cur_lim):
        status1 = self.kikusui.set_mode(mode)
        status2 = self.kikusui.set_polarity(polar)
        status3 = self.kikusui.set_output_voltage(out_vol)
        status4 = self.kikusui.set_voltage_limit(out_vol_lim)
        status5 = self.kikusui.set_current_limit(out_cur_lim)
        final_status = status1 and status2 and status3 and status4 and status5
        return final_status

    def set_sequence_output(self, seq_definition_setting):
        status_set_def = self.kikusui.set_store_seq_definition(seq_definition_setting[0],
                                                               seq_definition_setting[1],
                                                               seq_definition_setting[2],
                                                               seq_definition_setting[3],
                                                               seq_definition_setting[4],
                                                               seq_definition_setting[5])
        return status_set_def

    def update_output_voltage(self, out_vol):
        self.kikusui.set_output_voltage(out_vol)

    def on_off_equipment(self, on_off=0):
        return self.kikusui.turn_on_output(on_off)

    def read_output_supply(self):
        read_iout = self.kikusui.read_output_current()
        read_vout = self.kikusui.read_output_voltage()
        return read_vout, read_iout

    def clear_error(self):
        self.kikusui.clear_error()


if __name__ == "__main__":
    rm = Kikusui_features()
    rm.connect_equipment('USB0::0x0B3E::0x1012::XF001773::0::INSTR')
    rm.clear_error()
    rm.disconnect_equipment()

    # rm.set_unipolar_cv_output("CV", "BIP", 5, 10, 1)
    # rm.on_off_equipment(1)
    # time.sleep(1)
    # print(rm.read_output_supply())

