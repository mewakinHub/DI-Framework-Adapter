# src/adapters/injector_adapter.py

from injector import Injector, Module, singleton, Binder
from .di_container import DIContainerAdapter

class InjectorAdapter(DIContainerAdapter):
    """Adapter for the 'injector' library."""

    def __init__(self):
        self._injector = Injector()

    def bind(self, interface, to, is_singleton=True, name=None):
        """Bind an interface to an implementation using the injector library."""
        class DynamicModule(Module):
            def configure(self, binder: Binder):
                if name:
                    binder.bind(f"{interface.__name__}_{name}", to=to, scope=singleton if is_singleton else None)
                else:
                    binder.bind(interface, to=to, scope=singleton if is_singleton else None)

        self._injector.binder.install(DynamicModule())

    def get(self, interface, name=None):
        """Retrieve an instance of the specified interface using the injector library."""
        if name:
            return self._injector.get(f"{interface.__name__}_{name}")
        return self._injector.get(interface)
