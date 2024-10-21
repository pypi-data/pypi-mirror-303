import zmq
import threading
import pickle
import logging
from .utils import get_logger

logger = get_logger(__name__)

class KeyValueStoreClient:
    """
    A client for the centralized key-value store.
    """

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:6000")
        logger.info("Connected to KeyValueStore server at port 6000.")

    def set(self, key, value):
        """
        Set a key-value pair in the store.
        """
        self.socket.send_pyobj(('SET', key, value))
        response = self.socket.recv_pyobj()
        logger.debug(f"Set key '{key}' with value '{value}'.")
        return response

    def get(self, key):
        """
        Get a value by key from the store.
        """
        self.socket.send_pyobj(('GET', key))
        response = self.socket.recv_pyobj()
        logger.debug(f"Got value '{response}' for key '{key}'.")
        return response

    def close(self):
        self.socket.close()
        self.context.term()

class KeyValueStoreServer(threading.Thread):
    """
    The server for the centralized key-value store.
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.store = {}
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:6000")
        logger.info("KeyValueStore server started on port 6000.")

    def run(self):
        while True:
            message = self.socket.recv_pyobj()
            if message[0] == 'SET':
                _, key, value = message
                self.store[key] = value
                self.socket.send_pyobj(True)
                logger.debug(f"Stored key '{key}' with value '{value}'.")
            elif message[0] == 'GET':
                _, key = message
                value = self.store.get(key, None)
                self.socket.send_pyobj(value)
                logger.debug(f"Retrieved key '{key}' with value '{value}'.")
