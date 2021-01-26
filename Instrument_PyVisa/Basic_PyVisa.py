import pyvisa


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

        except pyvisa.VisaIOError as error:
            print(error)
            return False
            # return True


if __name__ == "__main__":
    rm = Basic_PyVisa()
    rm.connect_device('USB0::0x0B3E::0x1012::XF001773::0::INSTR')



