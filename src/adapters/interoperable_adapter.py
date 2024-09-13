# src/adapters/interoperable_adapter.py

from src.adapters.di_adapter_factory import DIAdapterFactory

class InteroperableDIAdapter:
    def __init__(self, primary_framework: str, secondary_framework: str):
        self.primary_adapter = DIAdapterFactory.get_di_adapter(primary_framework) # first framework that already bound the dependencies
        self.secondary_adapter = DIAdapterFactory.get_di_adapter(secondary_framework) # second framework that needs to access the dependencies
        self._registry = {} # central storage: stores singletons in a shared registry to ensure they are accessed consistently across frameworks

    def bind(self, interface, to, is_singleton=True, name=None):
        """Bind an interface to an implementation in both frameworks and register it in the central registry."""
        key = (interface, name)
        self.primary_adapter.bind(interface, to, is_singleton, name)
        self.secondary_adapter.bind(interface, to, is_singleton, name)
        
        if is_singleton: # singleton instance (cache problem?)
            instance = self.primary_adapter.get(interface, name)
            self._registry[key] = instance

    def get(self, interface, name=None):
        """Retrieve an instance from the central registry or from the respective framework."""
        key = (interface, name) # If the instance is in the registry, it's returned immediately
        if key in self._registry:
            return self._registry[key]
        
        try: # queries non-singleton instance from the either framework
            return self.primary_adapter.get(interface, name)
        except AttributeError:
            return self.secondary_adapter.get(interface, name)

    def connect_frameworks(self, interface, from_secondary=False, name=None, is_singleton=True):
        """Link a dependency from one framework to another by binding it to the other framework's implementation."""
        key = (interface, name)
        
        if from_secondary:
            implementation = self.secondary_adapter.get(interface, name)
            self.primary_adapter.bind(interface, lambda: implementation, is_singleton, name)
        else: # default
            implementation = self.primary_adapter.get(interface, name)
            self.secondary_adapter.bind(interface, lambda: implementation, is_singleton, name)

        # Store it in the registry for consistent access
        if is_singleton:
            self._registry[key] = implementation

    def integrate_dependency(self, interface, secondary_interface, name=None):
        """Integrate a specific dependency across frameworks."""
        primary_dep = self.primary_adapter.get(interface, name)
        secondary_dep = self.secondary_adapter.get(secondary_interface, name)
        
        self._registry[(interface, name)] = primary_dep
        self._registry[(secondary_interface, name)] = secondary_dep
        
        return primary_dep, secondary_dep
