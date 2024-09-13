# src/adapters/di_container.py

from abc import ABC, abstractmethod

class DIContainerAdapter(ABC):
    """Abstract base class for DI container adapters."""
    
    @abstractmethod
    def bind(self, interface, to, is_singleton=True, name=None):
        """Bind an interface to a specific implementation."""
        raise NotImplementedError("This method must be overridden by subclasses.")
        # pass
    
    @abstractmethod
    def get(self, interface, name=None):
        """Get an instance of the specified interface."""
        raise NotImplementedError("This method must be overridden by subclasses.")
        # pass
