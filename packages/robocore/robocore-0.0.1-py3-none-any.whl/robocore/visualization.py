import threading
import logging
import rerun
from .utils import get_logger

logger = get_logger(__name__)

class Visualizer(threading.Thread):
    """
    Visualizes data from topics using rerun-sdk.
    """

    def __init__(self, topics):
        threading.Thread.__init__(self)
        self.daemon = True
        self.topics = topics
        logger.info(f"Visualizer initialized for topics: {self.topics}.")

    def run(self):
        # Placeholder for visualization logic
        rerun.init("Robocore Visualization")
        for topic in self.topics:
            # Visualization code using rerun-sdk
            logger.debug(f"Visualizing topic '{topic}'.")
