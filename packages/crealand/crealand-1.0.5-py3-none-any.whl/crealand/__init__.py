__version__ = '0.1.0'

from .apis import (
    # ai, 
    # control, 
    # detect, 
    event, 
    # interactive, 
    # media, 
    # object, 
    # sensor
)

from .utils.logger_setup import (
    enable_logger, 
    disable_logger, 
    setup_logger
)

def __initialize():
    try:
        import threading
        from .core.websocket.websocket_client import ws_connect, get_ws_client, init_callback

        logger = setup_logger()
        threading.Thread(target=ws_connect, args=()).start()
        while True:
            ws_client = get_ws_client()
            if ws_client and ws_client.session_id:
                break
        init_callback()
    except Exception as e:
        logger.error(f'An error occurred: {e}')

__initialize()

