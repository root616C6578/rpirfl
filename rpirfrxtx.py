from rpi_rf import RFDevice
import time
class RFReceiver:
    @staticmethod
    def receive(pin):
        rfdevice = RFDevice(pin)
        rfdevice.enable_rx()
        timestamp = None
        rx_code_list = []
        protocol_list = []
        pulse_length_list = []
        try:
            while True:
                if rfdevice.rx_code_timestamp != timestamp:
                    timestamp = rfdevice.rx_code_timestamp
                    code = rfdevice.rx_code
                    protocol = rfdevice.rx_proto
                    pulse_length = rfdevice.rx_pulselength
                    rx_code_list = [int(x) for x in str(code)]
                    protocol_list = [int(x) for x in str(protocol)]
                    pulse_length_list = [int(x) for x in str(pulse_length)]
                    time.sleep(0.01) 
        except KeyboardInterrupt:     
            rfdevice.cleanup()
            return rx_code_list, protocol_list, pulse_length_list

class RFTransmitter:
    @staticmethod
    def transmit(pin, code, protocol, pulselength, repeat=10):
        rfdevice = RFDevice(pin)
        rfdevice.enable_tx()
        rfdevice.tx_repeat = repeat
        rfdevice.tx_code(code, protocol, pulselength)
        rfdevice.cleanup()

