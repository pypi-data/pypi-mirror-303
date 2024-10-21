from .kvstore import KeyValueStoreServer
from .registry import RegistryServer

def start_servers():
    """
    Start the key-value store and registry servers automatically.
    """
    kv_server = KeyValueStoreServer()
    kv_server.start()
    registry_server = RegistryServer()
    registry_server.start()
