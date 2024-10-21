import logging
import queue
import struct
import time
from threading import Thread
from typing import Callable, List

from . import Packet
from .command.get_device_capabilities import parse_get_device_capabilities_response
from .command.get_id_buffer import parse_get_id_buffer_response
from .command.get_id_buffer_meta import parse_get_id_buffer_meta_response, NurTagDataMeta
from .command.get_mode import parse_get_mode_response
from .command import HeaderFlagCodes, StatusCode
from .command.inventory import parse_inventory_response
from .command.inventory_stream import parse_inventory_stream_notification, InventoryStreamNotification
from .command.module_setup import parse_module_setup_response
from .command.get_reader_info import parse_get_reader_info_response
from .. import CommandCode

logger = logging.getLogger(__name__)


class RxHandler:

    def __init__(self):
        self.buffer = bytearray()
        self.response_queue = queue.Queue()
        self.notification_queue = queue.Queue()
        self.notification_callback = None
        self._callback_thread = Thread(target=self._callback_thread_fxn, daemon=True, name='CallbackThread')
        self._callback_thread.start()

    def set_notification_callback(self, callback: Callable[[InventoryStreamNotification,
                                                            List[NurTagDataMeta]], None]) -> None:
        self.notification_callback = callback

    def _callback_thread_fxn(self) -> None:
        while True:
            if not self.notification_queue.empty():
                [notification, tags] = self.notification_queue.get()
                if self.notification_callback:
                    self.notification_callback(notification, tags)
            time.sleep(0.001)

    def append_data(self, data):
        if data is not None:
            self.buffer += data
            self._try_parse_data()

    def _try_parse_data(self):
        try:
            # Discard data until PREAMBLE
            start = self.buffer.find(bytearray([Packet.START_BYTE]))
            if start > 0:
                logger.warning('Syching PREAMBLE.')
                self.buffer = self.buffer[start:]

            # Check if Header available
            while len(self.buffer) > 5:
                # Checksum validation
                checksum_rx = self.buffer[5]
                checksum_calc = Packet.checksum(self.buffer[0:5])
                if checksum_calc != checksum_rx:
                    logger.warning('Checksum mismatch')
                    # Remove START_BYTE
                    del self.buffer[0]
                else:
                    payload_len = struct.unpack('<H', self.buffer[1:3])[0]
                    header_flags = struct.unpack('<H', self.buffer[3:5])[0]
                    # Check if Full packet available
                    if len(self.buffer) > 5 + payload_len:
                        # Check CRC
                        crc_rx = struct.unpack('<H', self.buffer[7 + payload_len - 3: 7 + payload_len])[0]
                        crc_calc = Packet.crc16(self.buffer[6:7 + payload_len - 3])
                        if crc_calc != crc_rx:
                            logger.warning('CRC mismatch')
                        else:
                            # Extract data
                            command = CommandCode(self.buffer[6])
                            payload = self.buffer[7:7 + payload_len - 3]

                            status = StatusCode(payload[0])
                            if status != StatusCode.SUCCESS:
                                logger.error(status)
                                return
                            payload = payload[1:]

                            # Process message
                            if header_flags == HeaderFlagCodes.RESPONSE.value:
                                self._process_response(command, payload)
                            elif header_flags & HeaderFlagCodes.NOTIFICATION.value:
                                self._process_notification(command, payload)

                        # Remove processed data
                        del self.buffer[0:8 + payload_len]
                    else:
                        # Missing payload data
                        break
        except Exception as e:
            logger.error(e)

    def _process_response(self, command: CommandCode, payload: bytearray):
        if command is CommandCode.PING:
            self.response_queue.put(True)
            return
        if command is CommandCode.RESET:
            self.response_queue.put(True)
            return
        if command is CommandCode.RESTART:
            self.response_queue.put(True)
            return
        if command is CommandCode.GET_MODE:
            self.response_queue.put(parse_get_mode_response(payload))
            return
        if command is CommandCode.GET_READER_INFO:
            self.response_queue.put(parse_get_reader_info_response(payload))
            return
        if command is CommandCode.GET_DEVICE_CAPABILITIES:
            self.response_queue.put(parse_get_device_capabilities_response(payload))
            return
        if command is CommandCode.GET_MODULE_SETUP:
            self.response_queue.put(parse_module_setup_response(payload))
            return
        if command is CommandCode.SIMPLE_INVENTORY:
            self.response_queue.put(parse_inventory_response(payload))
            return
        if command is CommandCode.GET_ID_BUFFER:
            self.response_queue.put(parse_get_id_buffer_response(payload))
            return
        if command is CommandCode.GET_ID_BUFFER_META:
            self.response_queue.put(parse_get_id_buffer_meta_response(payload))
            return
        if command is CommandCode.CLEAR_ID_BUFFER:
            self.response_queue.put(True)
            return
        if command is CommandCode.INVENTORY_STREAM:
            self.response_queue.put(True)
            return

    def _process_notification(self, command: CommandCode, payload: bytearray):
        if command is CommandCode.NOTIFICATION_INVENTORY:
            self.notification_queue.put(parse_inventory_stream_notification(payload))
            return

    def get_response(self, timeout=1):
        start = time.monotonic()
        while self.response_queue.empty():
            time.sleep(0.001)
            if time.monotonic() - start > timeout:
                raise TimeoutError
        return self.response_queue.get()
