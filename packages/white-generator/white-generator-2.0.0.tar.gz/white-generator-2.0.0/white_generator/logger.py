import logging

import termcolor
import termcolor._types

_LOG_FORMAT = (
    termcolor.colored('%(asctime)s', 'grey')
    + ' [%(levelname)s] %(message)s'
)
_LOG_LEVEL_COLORS: dict[str, termcolor._types.Color] = {
    '[INFO]': 'green',
    '[WARNING]': 'yellow',
    '[ERROR]': 'red',
}

class _Formatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        for level, color in _LOG_LEVEL_COLORS.items():
            message = message.replace(level, termcolor.colored(level, color))

        return message

def get_logger() -> logging.Logger:
    return logging.getLogger(__package__)

def init_logger() -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(_Formatter(_LOG_FORMAT))

    get_logger().addHandler(handler)
    get_logger().setLevel(logging.INFO)
