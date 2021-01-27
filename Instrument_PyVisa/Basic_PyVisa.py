import pyvisa
import time

# All the basic PyVISA command should be placed here.
class Basic_PyVisa:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()

    def list_connected_devices(self):
        return self.rm.list_resources()

    def connect_device(self, target_resource_instr):
        try:
            self.inst = self.rm.open_resource(target_resource_instr)
            print(f'Connected -->  {self.inst.query("*IDN?")}')
            return True

        # except pyvisa.VisaIOError as error:
        except:
            # print(error)
            print("Error 002: \n"
                  "- Incorrect equipment used/ no connection detection.\n"
                  "- Please make sure the equipment is properly connected")
            return False

    def disconnect_device(self):
        try:
            self.inst.close()
            print("Session close")
        except:
            print("Error 003: Unable to close the session")

    def display_session(self):
        return self.inst.session


if __name__ == "__main__":
    rm = Basic_PyVisa()
    rm.connect_device('USB0::0x0B3E::0x1012::XF001773::0::INSTR')
    rm.disconnect_device()




