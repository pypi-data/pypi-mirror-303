import logging
import time
from typing import List

from src.nurapy import NurAPY, ModuleSetupFlags, ModuleSetup
from src.nurapy.protocol.command.get_id_buffer_meta import NurTagDataMeta
from src.nurapy.protocol.command.inventory_stream import InventoryStreamNotification
from src.nurapy.protocol.command.module_setup import ModuleSetupLinkFreq, ModuleSetupRxDec

logging.basicConfig(level=logging.DEBUG)

reader = NurAPY('COM8')
if not reader.ping():
    logging.error('Could not connect to NUR APY')
    exit()
reader.get_mode()
reader_info = reader.get_reader_info()
device_caps = reader.get_device_capabilities()
setup = reader.get_module_setup(setup_flags=[
    ModuleSetupFlags.LINKFREQ,
    ModuleSetupFlags.RXDEC,
    ModuleSetupFlags.TXLEVEL,
    ModuleSetupFlags.ANTMASKEX,
    ModuleSetupFlags.SELECTEDANT,
    ModuleSetupFlags.ALL
])

new_setup = ModuleSetup()
new_setup.link_freq = ModuleSetupLinkFreq.BLF_256
new_setup.rx_decoding = ModuleSetupRxDec.MILLER_4
new_setup.tx_level = 0
new_setup.antenna_mask = 1
new_setup.selected_antenna = 0
setup = reader.set_module_setup(setup_flags=[
    ModuleSetupFlags.LINKFREQ,
    ModuleSetupFlags.RXDEC,
    ModuleSetupFlags.TXLEVEL,
    ModuleSetupFlags.ANTMASK,
    ModuleSetupFlags.SELECTEDANT
], module_setup=new_setup)

inventory_response = reader.simple_inventory()
if inventory_response.tags_in_memory:
    tags = reader.get_id_buffer_with_metadata(clear=True)
    logging.info(tags)


def my_notification_callback(inventory_stream_notification: InventoryStreamNotification,
                             tags: List[NurTagDataMeta]):
    if inventory_stream_notification.stopped:
        logging.info('Restarting inventory stream')
        reader.start_inventory_stream()
    for tag in tags:
        logging.info(tag)
    reader.clear_id_buffer()


reader.set_notification_callback(my_notification_callback)
reader.start_inventory_stream()
time.sleep(2)
reader.stop_inventory_stream()
