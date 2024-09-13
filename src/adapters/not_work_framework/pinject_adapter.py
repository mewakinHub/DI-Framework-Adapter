# src/adapters/pinject_adapter.py

import pinject
from .di_container import DIContainerAdapter

class PinjectAdapter(DIContainerAdapter):
    """Adapter for the 'pinject' library."""

    def __init__(self):
        self._obj_graph = pinject.new_object_graph()

    def bind(self, interface, to, is_singleton=True, name=None):
        """Bind an interface to an implementation using the pinject library."""
        binding_type = pinject.BINDING_TYPE_SINGLETON if is_singleton else pinject.BINDING_TYPE_NEW_INSTANCE
        self._obj_graph.provide_binding(interface, to, binding_type=binding_type)

    def get(self, interface, name=None):
        """Retrieve an instance of the specified interface using the pinject library."""
        return self._obj_graph.provide(interface)
