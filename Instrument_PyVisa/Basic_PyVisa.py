import pyvisa


class Basic_PyVisa:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()

    def list_connected_devices(self):
        return self.rm.list_resources()

    def connect_device(self, target_resource_instr):
        try:
            self.rm.open_resource(target_resource_instr)
            return True
        except pyvisa.VisaIOError as error:
            print(error.args)
            print(f'{target_resource_instr} is busy/ not available')





