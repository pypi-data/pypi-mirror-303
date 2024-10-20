import struct
from enum import Enum


class HeaderFlagCodes(Enum):
    RESPONSE = 0x0000
    NOTIFICATION = 0x0001
    INVENTORY_READ_NOTIFICATION = 0x0002


class CommandCode(Enum):
    PING = 1
    RESET = 3
    GET_MODE = 4
    CLEAR_ID_BUFFER = 5
    GET_ID_BUFFER = 6
    GET_ID_BUFFER_META = 7
    GET_READER_INFO = 9
    GET_DEVICE_CAPABILITIES = 0xB
    RESTART = 0x14
    GET_MODULE_SETUP = 0x22
    SIMPLE_INVENTORY = 0x31
    INVENTORY_STREAM = 0x39
    NOTIFICATION_INVENTORY = 0x82


class StatusCode(Enum):
    SUCCESS = 0
    INVALID_COMMAND = 1
    INVALID_LENGTH = 2
    PARAMETER_OUT_OF_RANGE = 3
    INVALID_PARAMETER = 5
    CRC_ERROR = 11
    APPLICATION_NOT_PRESENT = 14
