# src/services/interfaces.py

from abc import ABC, abstractmethod

class IService(ABC):
    """Interface for a service."""
    
    @abstractmethod
    def serve(self):
        raise NotImplementedError("This method must be overridden.")
        # pass
