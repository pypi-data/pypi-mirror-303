from enum import IntEnum, unique, auto

SWITCH_BYTES_LENGTH = 16
SWITCH_MAX_SIZE = 0xFFFFFFFF
SWITCH_COMMANDS = (1 << SWITCH_BYTES_LENGTH*8) - 1
SCHEDULER_TIMEOUT_MAX = 2147483  # INT_MAX without last three digits
STREAM_CLOSE_MARK = "#&@"

@unique
class SwitchMessages(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return last_values[-1] - count

    NEW_DEMANDS = SWITCH_COMMANDS
    LAST_MESSAGES = auto()

@unique
class ApiType(IntEnum):
    WS = 0
    REST = auto()
    HTML = auto()
