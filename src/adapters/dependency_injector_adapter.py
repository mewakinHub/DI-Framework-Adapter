# src/adapters/dependency_injector_adapter.py

from dependency_injector import containers, providers
from .di_container import DIContainerAdapter

class DependencyInjectorAdapter(DIContainerAdapter):
    """Adapter for the 'dependency-injector' library."""

    def __init__(self):
        self._container = containers.DynamicContainer()

    def bind(self, interface, to, is_singleton=True, name=None):
        """Bind an interface to an implementation using the dependency-injector library."""
        provider = providers.Singleton(to) if is_singleton else providers.Factory(to)
        # if name:
        #     setattr(self._container, f"{interface.__name__}_{name}", provider)
        # else:
        #     setattr(self._container, interface.__name__, provider)
        attribute_name = f"{interface.__name__}_{name}" if name else interface.__name__
        setattr(self._container, attribute_name, provider)
        print(f"[dependency_injector] Bound {attribute_name} to {to} (singleton={is_singleton})")

    def get(self, interface, name=None):
        """Retrieve an instance of the specified interface using the dependency-injector library."""
        provider_name = f"{interface.__name__}_{name}" if name else interface.__name__
        provider = getattr(self._container, provider_name, None)
        
        if not provider:
            raise AttributeError(f"'{self._container.__class__.__name__}' object has no attribute '{provider_name}'. "
                             "Check if the service was bound correctly.")
        return provider()
        # try:
        #     provider = getattr(self._container, provider_name)
        #     return provider()
        # except AttributeError:
        #     raise AttributeError(f"'{self._container.__class__.__name__}' object has no attribute '{provider_name}'. "
        #                          f"Check if the service was bound correctly.")
