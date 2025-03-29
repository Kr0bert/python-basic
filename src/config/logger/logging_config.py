import atexit
import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger("mylogger")


def setup_logging():
    script_dir = pathlib.Path(__file__).resolve()
    config_file = script_dir.parent / "logs_config.json"
    print(f"Loading logging configuration from {config_file}")
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)
    # setup_queue_handler()


def setup_queue_handler():
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
