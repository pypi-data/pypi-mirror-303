from pyamasicp.client import Client

SET_POWER_STATE_COMMAND = b'\x18'
GET_POWER_STATE_COMMAND = b'\x19'
SET_VOLUME_COMMAND = b'\x44'
GET_VOLUME_COMMAND = b'\x45'
IR_COMMAND = b'\xDB'
POWER_OFF = b'\x01'
POWER_ON = b'\x02'

IR_POWER = b'\xA0'
IR_MENU = b'\xA1'
IR_INPUT = b'\xA2'
IR_VOL_UP = b'\xA3'
IR_VOL_DOWN = b'\xA4'
IR_MUTE = b'\xA5'
IR_CURSOR_UP = b'\xA6'
IR_CURSOR_DOWN = b'\xA7'
IR_CURSOR_LEFT = b'\xA8'
IR_CURSOR_RIGHT = b'\xA9'
IR_OK = b'\xB1'
IR_RETURN = b'\xB2'
IR_RED = b'\xC1'
IR_GREEN = b'\xC2'
IR_YELLOW = b'\xC3'
IR_BLUE = b'\xC4'
IR_FORMAT = b'\xD1'
IR_INFO = b'\xD2'
IR_BTN_0 = b'\x00'
IR_BTN_1 = b'\x01'
IR_BTN_2 = b'\x02'
IR_BTN_3 = b'\x03'
IR_BTN_4 = b'\x04'
IR_BTN_5 = b'\x05'
IR_BTN_6 = b'\x06'
IR_BTN_7 = b'\x07'
IR_BTN_8 = b'\x08'
IR_BTN_9 = b'\x09'


class Commands:

    def __init__(self, client: Client, id=b'\x01'):
        self._client = client
        self._id = id

    def get_power_state(self):
        match self._client.send(self._id, GET_POWER_STATE_COMMAND):
            case b'\x01':
                return False
            case b'\x02':
                return True
            case _:
                raise CommandException("Unknown power state")

    def set_power_state(self, state: bool):
        self._client.send(self._id, SET_POWER_STATE_COMMAND, POWER_ON if state else POWER_OFF)

    def get_volume(self):
        result = [b for b in self._client.send(self._id, GET_VOLUME_COMMAND)]
        result.reverse()
        return result

    def set_volume(self, output_volume=0, volume=0):
        self._client.send(self._id, SET_VOLUME_COMMAND, bytearray([volume, output_volume]))

    def ir_command(self, code):
        self._client.send(self._id, IR_COMMAND, code)


class CommandException(Exception):
    pass
