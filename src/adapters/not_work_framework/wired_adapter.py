# src/adapters/wired_adapter.py

from wired import ServiceContainer, ServiceRegistry
from .di_container import DIContainerAdapter

class WiredAdapter(DIContainerAdapter):
    """Adapter for the 'wired' library."""

    def __init__(self):
        self._registry = ServiceRegistry()
        self._container = ServiceContainer(self._registry)

    def bind(self, interface, to, is_singleton=True, name=None):
        """Bind an interface to an implementation using the wired library."""
        if is_singleton:
            self._registry.register_singleton(to, provided=interface)
        else:
            self._registry.register_factory(to, provided=interface)

    def get(self, interface, name=None):
        """Retrieve an instance of the specified interface using the wired library."""
        return self._container.get(interface)
