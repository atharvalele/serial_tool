import serial
import serial.tools.list_ports

def serial_list_ports():
    ports = serial.tools.list_ports.comports()

    return ports

class SerialHandler:
    def __init__(self):
        pass

    def connect(self, port: str, baudrate: int, flow_ctl: bool, sw_flow_ctl: bool, parity: str) -> bool:
        try:
            self.connection = serial.Serial(
                port=port,
                baudrate=baudrate,
                timeout=0.1,
                rtscts=flow_ctl,
                xonxoff=sw_flow_ctl,
                parity=parity
            )

            return True
        except (serial.SerialException, ValueError):
            return False
