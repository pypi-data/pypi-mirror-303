import zmq
import threading
import time
import pickle
import logging
from .registry import RegistryClient
from .utils import get_logger

logger = get_logger(__name__)

class Publisher:
    """
    A class for publishing messages to a topic.
    """

    def __init__(self, topic):
        self.topic = topic
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.registry = RegistryClient()
        self.port = self.registry.register_topic(topic)
        self.socket.bind(f"tcp://*:{self.port}")
        logger.info(f"Publisher bound to port {self.port} for topic '{self.topic}'.")

    def publish(self, message):
        """
        Publish a message to the topic.
        """
        data = pickle.dumps(message)
        self.socket.send_multipart([self.topic.encode(), data])
        logger.debug(f"Published message on topic '{self.topic}'.")

    def close(self):
        self.socket.close()
        self.context.term()

class Subscriber:
    """
    A class for subscribing to messages from a topic.
    """

    def __init__(self, topic, retry_interval=0.1, timeout=10):
        self.topic = topic
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.registry = RegistryClient()
        self.port = self.registry.get_topic_port(topic)
        start_time = time.time()
        while self.port is None:
            self.port = self.registry.get_topic_port(topic)
            if self.port is None:
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    raise TimeoutError(f"Timeout: Could not find port for topic '{topic}' within {timeout} seconds.")
                time.sleep(retry_interval)
        self.socket.connect(f"tcp://localhost:{self.port}")
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.topic)
        logger.info(f"Subscriber connected to port {self.port} for topic '{self.topic}'.")

    def receive(self):
        """
        Receive a message from the topic.
        """
        topic, data = self.socket.recv_multipart()
        message = pickle.loads(data)
        logger.debug(f"Received message on topic '{self.topic}'.")
        return message

    def close(self):
        self.socket.close()
        self.context.term()
