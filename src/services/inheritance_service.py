# src/services/inheritance_service.py

from src.services.interfaces import IService

class InheritanceService(IService):
    """Service that inherits from IService for DIP testing."""
    
    def serve(self):
        print(f"InheritanceService with id={id(self)} is serving, testing DIP compliance.")
