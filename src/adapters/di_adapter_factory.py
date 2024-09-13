# src/adapters/di_adapter_factory.py

from .injector_adapter import InjectorAdapter
from .dependency_injector_adapter import DependencyInjectorAdapter
# from .pinject_adapter import PinjectAdapter
# from .wired_adapter import WiredAdapter

class DIAdapterFactory:
    """Factory class to create DI adapters based on the selected framework."""
    
    @staticmethod
    def get_di_adapter(framework_name: str):
        if framework_name == 'injector':
            return InjectorAdapter()
        elif framework_name == 'dependency_injector':
            return DependencyInjectorAdapter()
        # elif framework_name == 'pinject':
        #     return PinjectAdapter()
        # elif framework_name == 'wired':
        #     return WiredAdapter()
        else:
            raise ValueError(f"Unsupported DI framework: {framework_name}")
