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
            error_msg = ""
            return True, error_msg
        except:
            print(f"Set Sequence Definition Error!")
            error_msg = f"Set Sequence Definition Error!"
            return False, error_msg

    def set_DCparam_seq_setting(self, STEP, STEP_TIME, STEP_DCV,
                                STEP_DCRAMP_ONOFF, STEP_DC_RAMP_START, STEP_DC_RAMP_STOP, STEP_DC_OUT_ONOFF,
                                TRIG_OUT, TRIG_IN):
        try:
            self.inst.write(f'PROG:EDIT:STEP:SEL {STEP}')
            self.inst.write(f'PROG:EDIT:STEP:TIME {STEP_TIME}')
            if STEP_DCRAMP_ONOFF == "ON":
                self.inst.write(f'PROG:EDIT:STEP:VOLT {STEP_DC_RAMP_STOP},RAMP')
                self.inst.write(f'PROG:EDIT:STEP:VOLT:RAMP {STEP_DC_RAMP_START}')
            else:
                self.inst.write(f'PROG:EDIT:STEP:VOLT {STEP_DCV},IMM')
            self.inst.write(f'PROG:EDIT:STEP:STAT {STEP_DC_OUT_ONOFF},{TRIG_OUT},{TRIG_IN}')
            error_msg = ""
            return True, error_msg

        except:
            print(f"Set DC parameter sequencing Error!")
            error_msg = f"Set DC parameter sequencing Error!"
            return False, error_msg

    def set_ACparam_seq_setting(self, AC_STAT_ONOFF, AC_FUNC, AC_AMPL, AC_FREQ, AC_PHASE, AC_DUTY,
                                AC_AMPL_SWEEP_ONOFF, AC_AMPL_SWEEP_START, AC_AMPL_SWEEP_STOP,
                                AC_FREQ_SWEEP_ONOFF, AC_FREQ_CHAR, AC_FERQ_START, AC_FREQ_STOP):
        try:
            self.inst.write(f'PROG:EDIT:STEP:AC:STAT {AC_STAT_ONOFF}')                  # SuperImpose on off
            self.inst.write(f'PROG:EDIT:STEP:FUNC {AC_FUNC}')                           # AC Signal Waveform
            self.inst.write(f'PROG:EDIT:STEP:PHAS {AC_PHASE},ON')                       # AC Signal Phase angle
            self.inst.write(f'PROG:EDIT:STEP:SQU:DCYC {AC_DUTY}')                       # AC Duty Cycle

            if AC_AMPL_SWEEP_ONOFF == "ON":
                self.inst.write(f'PROG:EDIT:STEP:VOLT:AC {AC_AMPL_SWEEP_STOP},SWE')     # AC Sweep Stop Amp
                self.inst.write(f'PROG:EDIT:STEP:VOLT:AC:SWE {AC_AMPL_SWEEP_START}')    # AC Sweep Start Amp
            else:
                self.inst.write(f'PROG:EDIT:STEP:VOLT:AC {AC_AMPL}, IMM')               # AC Sweep Amp

            if AC_FREQ_SWEEP_ONOFF == "ON":
                self.inst.write(f'PROG:EDIT:STEP:FREQ {AC_FREQ_STOP},SWE')                  # AC Freq Sweep Stop Freq
                self.inst.write(f'PROG:EDIT:STEP:FREQ:SWE {AC_FREQ_CHAR},{AC_FERQ_START}')  # AC Freq Sweep Char and Start Freq
            else:
                self.inst.write(f'PROG:EDIT:STEP:FREQ {AC_FREQ},IMM')                   # AC Signal Amp when IMM (Stop if SWE)

            error_msg = ""

            return True, error_msg

        except:
            print(f"Set AC parameter sequencing Error!")
            error_msg = f"Set AC parameter sequencing Error!"
            return False, error_msg

    def run_select_seq(self, SEQ_NUMBER):
        try:
            self.inst.write(f'PROG:NAME {SEQ_NUMBER}')
            self.inst.write(f'PROG:EXEC:STAT RUN')
            error_msg = ""
            return True, error_msg

        except:
            print(f"Run Sequence {SEQ_NUMBER} Error")
            error_msg = f"Run Sequence {SEQ_NUMBER} Error"
            return False, error_msg

    def seq_status_query(self):
        try:
            self.inst.write(f'PROG:EXEC?')
            status = self.inst.read()
            return True, status

        except:
            error_msg = f"Query for status FAIL"
            return False, error_msg


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

    def set_sequence_output(self, seq_definition_setting, sequence_setting):

        # First - Set Store sequence Definition
        status_set_def, error_msg_def = self.kikusui.set_store_seq_definition(seq_definition_setting[1],
                                                               seq_definition_setting[5],
                                                               seq_definition_setting[0],
                                                               seq_definition_setting[2],
                                                               seq_definition_setting[3],
                                                               seq_definition_setting[4])

        if status_set_def:

            status_set_dcparam = False
            status_set_acparam = False
            error_msg = ""

            # Second Set DC Param Sequence
            for step in range(len(sequence_setting)):
                status_set_dcparam, error_msg_dcparam = self.kikusui.set_DCparam_seq_setting(STEP=sequence_setting[step][0],
                                                                                             STEP_TIME=sequence_setting[step][1],
                                                                                             STEP_DCV=sequence_setting[step][2],
                                                                                             STEP_DCRAMP_ONOFF=sequence_setting[step][3],
                                                                                             STEP_DC_RAMP_START=sequence_setting[step][4],
                                                                                             STEP_DC_RAMP_STOP=sequence_setting[step][5],
                                                                                             STEP_DC_OUT_ONOFF=sequence_setting[step][6],
                                                                                             TRIG_OUT=sequence_setting[step][7],
                                                                                             TRIG_IN=sequence_setting[step][8])

                if not status_set_dcparam:
                    error_msg = error_msg_dcparam
                    break

                status_set_acparam, error_msg_acparam = self.kikusui.set_ACparam_seq_setting(AC_STAT_ONOFF=sequence_setting[step][9],
                                                                                             AC_FUNC=sequence_setting[step][10],
                                                                                             AC_AMPL=sequence_setting[step][11],
                                                                                             AC_FREQ=sequence_setting[step][12],
                                                                                             AC_PHASE=sequence_setting[step][13],
                                                                                             AC_DUTY=sequence_setting[step][14],
                                                                                             AC_AMPL_SWEEP_ONOFF=sequence_setting[step][15],
                                                                                             AC_AMPL_SWEEP_START=sequence_setting[step][16],
                                                                                             AC_AMPL_SWEEP_STOP=sequence_setting[step][17],
                                                                                             AC_FREQ_SWEEP_ONOFF=sequence_setting[step][18],
                                                                                             AC_FREQ_CHAR=sequence_setting[step][19],
                                                                                             AC_FERQ_START=sequence_setting[step][20],
                                                                                             AC_FREQ_STOP=sequence_setting[step][21])
                if not status_set_acparam:
                    error_msg = error_msg_acparam
                    break

            status_set = status_set_dcparam and status_set_acparam

        else:
            status_set = status_set_def
            error_msg = error_msg_def

        return status_set, error_msg

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

    def run_sequence_output(self, sequence_number):

        status_run_seq, error_msg_run = self.kikusui.run_select_seq(sequence_number)
        return status_run_seq, error_msg_run

    def run_sequence_query(self):
        read_status, query_stat = self.kikusui.seq_status_query()
        return read_status, query_stat


if __name__ == "__main__":
    rm = Kikusui_features()
    rm.connect_equipment('USB0::0x0B3E::0x1012::XF001773::0::INSTR')
    rm.clear_error()
    rm.disconnect_equipment()

    # rm.set_unipolar_cv_output("CV", "BIP", 5, 10, 1)
    # rm.on_off_equipment(1)
    # time.sleep(1)
    # print(rm.read_output_supply())

