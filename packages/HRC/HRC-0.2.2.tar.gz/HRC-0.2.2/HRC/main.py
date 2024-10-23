import serial
import struct
import serial.tools.list_ports

class HRC_Finger:
    speed = 30
    torque = 0.125

    def __init__(self, id:int, speed:float, torque:int, ser : serial.Serial):
        self.id = id
        self.speed = speed
        self.torque = torque
        self.ser = ser

    def set_desired_speed(self, speed:float):
        self.speed = speed

    def set_desired_torque(self, torque:float):
        self.torque = torque

    def rotate(self, theta:float, speed:float = speed, torque:float = torque) -> None:
        msg = bytearray()

        torque = int(torque*16000)

        if(self.id == 1):
            msg.append(0xA1)
        elif(self.id == 2):
            msg.append(0xA2)
        elif(self.id == 3):
            msg.append(0xA3)
        elif(self.id == 4):
            msg.append(0xA4)

        msg1 = bytearray(struct.pack("<f", theta))
        for b in msg1:
            msg.append(b)

        msg.append(0xFF)

        msg1 = bytearray(struct.pack("<f", speed))
        for b in msg1:
            msg.append(b)

        msg.append(0xFF)

        msg1 = bytearray(struct.pack("<i", torque))
        for b in msg1:
            msg.append(b)

        msg.append(0xAB)

        try:        
            self.ser.write((msg))
        except Exception as e:
            print(f'Error while trying to send motor command: {e}')


class HRC_Hand:
    def __init__(self):

        self.ser = None
        ports = serial.tools.list_ports.comports()

        for port, desc, _ in sorted(ports):
                if "CH340" in desc:
                    try:
                        self.ser = serial.Serial(str(port), 9600)
                    except Exception as e:
                        print(f'error trying to open port: {e}')

        self.finger_1 = HRC_Finger(id=1, speed=50, torque=0.125, ser=self.ser)
        self.finger_2 = HRC_Finger(id=2, speed=50, torque=0.125, ser=self.ser)
        self.thumb_flexion = HRC_Finger(id=3, speed=50, torque=0.125, ser=self.ser)
        self.thumb_rotation = HRC_Finger(id=4, speed=50, torque=0.125, ser=self.ser)
