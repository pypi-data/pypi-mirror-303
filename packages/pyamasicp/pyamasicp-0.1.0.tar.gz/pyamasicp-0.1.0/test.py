import logging

from pyamasicp import client
from pyamasicp.commands import Commands, IR_VOL_UP, IR_VOL_DOWN, IR_OK
import getmac

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

HOST = 'iiyama.home'

logger.debug("MAC: %a" % getmac.get_mac_address(ip=HOST, hostname=HOST))

c = Commands(client.Client(HOST,mac="DC:62:94:25:02:B3"))
# c.set_power_state(True)

c.set_volume(22)
# c.ir_command(IR_OK)
logger.info("%s" % (c.get_volume()))

c.get_power_state()


# c.send(b'\x01', b'\x18', b'\x01')

# send(b'\x01', b'\xA2', b'\x01')
# send(b'\x01', b'\xAC', b'\x00\x18\x01\x00')

# send(b'\x01', b'\x44', b'\100\20')
