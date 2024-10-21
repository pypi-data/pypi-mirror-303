import zmq
import threading
import logging
from .utils import get_logger

logger = get_logger(__name__)

class RegistryClient:
    """
    Client for the topic registry server.
    """

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:7000")
        logger.info("Connected to Registry server at port 7000.")

    def register_topic(self, topic):
        """
        Register a new topic and get an assigned port.
        """
        self.socket.send_pyobj(('REGISTER', topic))
        port = self.socket.recv_pyobj()
        logger.debug(f"Registered topic '{topic}' with port {port}.")
        return port

    def get_topic_port(self, topic):
        """
        Get the port for an existing topic.
        """
        self.socket.send_pyobj(('GET_PORT', topic))
        port = self.socket.recv_pyobj()
        logger.debug(f"Got port {port} for topic '{topic}'.")
        return port

    def close(self):
        self.socket.close()
        self.context.term()

class RegistryServer(threading.Thread):
    """
    Server for managing topic registrations.
    """

    def __init__(self, start_port=8000):
        threading.Thread.__init__(self)
        self.daemon = True
        self.topics = {}
        self.current_port = start_port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:7000")
        logger.info("Registry server started on port 7000.")

    def run(self):
        while True:
            message = self.socket.recv_pyobj()
            if message[0] == 'REGISTER':
                _, topic = message
                if topic not in self.topics:
                    self.topics[topic] = self.current_port
                    self.current_port += 1
                self.socket.send_pyobj(self.topics[topic])
                logger.debug(f"Registered topic '{topic}' with port {self.topics[topic]}.")
            elif message[0] == 'GET_PORT':
                _, topic = message
                port = self.topics.get(topic, None)
                self.socket.send_pyobj(port)
                logger.debug(f"Provided port {port} for topic '{topic}'.")
