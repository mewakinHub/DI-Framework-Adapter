# main.py -> for Github Copilot tp recognize the path

from src.adapters.interoperable_adapter import InteroperableDIAdapter
from src.adapters.di_adapter_factory import DIAdapterFactory
from src.services.my_service import MyService
from src.services.dao import DAO
from src.services.logger import Logger
from src.services.mock_dao import MockDAO
from src.services.model_service import ModelService
from src.services.aggregation_service import AggregationService
from src.services.inheritance_service import InheritanceService
from src.services.interfaces import IService

def test_multiple_implementations(framework_name):
    di_adapter = DIAdapterFactory.get_di_adapter(framework_name)

    # Bind dependencies
    di_adapter.bind(DAO, DAO, is_singleton=True)
    di_adapter.bind(MockDAO, MockDAO, is_singleton=True)
    di_adapter.bind(Logger, Logger, is_singleton=True)
    di_adapter.bind(ModelService, ModelService, is_singleton=False)
    
    # First implementation: MyService with real DAO (non-singleton)
    def create_my_service_real():
        dao = di_adapter.get(DAO)
        logger = di_adapter.get(Logger)
        model_service = di_adapter.get(ModelService)
        service_instance = MyService(dao=dao, logger=logger, model_service=model_service)
        print(f"[{framework_name}] Created MyService (real DAO) instance with id={id(service_instance)}")
        return service_instance

    # Second implementation: MyService with MockDAO (with name)
    def create_my_service_mock():
        dao = di_adapter.get(MockDAO)
        logger = di_adapter.get(Logger)
        model_service = di_adapter.get(ModelService)
        service_instance = MyService(dao=dao, logger=logger, model_service=model_service)
        print(f"[{framework_name}] Created MyService (MockDAO) instance with id={id(service_instance)}")
        return service_instance
    
    # Bind services without a name for the first implementation
    di_adapter.bind(IService, create_my_service_real, is_singleton=False)
    
    # Bind services with a name for the second implementation
    di_adapter.bind(IService, create_my_service_mock, is_singleton=True, name="MyServiceMock")
    
    # Test non-singleton behavior
    service_real_1 = di_adapter.get(IService)
    service_real_2 = di_adapter.get(IService)
    print(f"[{framework_name}] MyService (real DAO) instance 1 id={id(service_real_1)}, instance 2 id={id(service_real_2)}")
    
    # Test singleton behavior
    service_mock_1 = di_adapter.get(IService, name="MyServiceMock")
    service_mock_2 = di_adapter.get(IService, name="MyServiceMock")
    print(f"[{framework_name}] MyService (MockDAO) instance 1 id={id(service_mock_1)}, instance 2 id={id(service_mock_2)}")

    # Aggregate services using AggregationService, injecting directly from DI
    print(f"\n[{framework_name}] Testing AggregationService:")
    aggregation_service_real = AggregationService(
        service1=di_adapter.get(IService),
        service2=di_adapter.get(IService)
    )
    aggregation_service_real.aggregate()
    
    # Aggregate services using AggregationService, injecting directly from DI
    print(f"\n[{framework_name}] Testing AggregationService:")
    aggregation_service_mock = AggregationService(
        service1=di_adapter.get(IService, name="MyServiceMock"),
        service2=di_adapter.get(IService, name="MyServiceMock")
    )
    aggregation_service_mock.aggregate()

    # Test InheritanceService for DIP compliance without DI
    print(f"\n[{framework_name}] Testing InheritanceService for DIP compliance:")
    inheritance_service = InheritanceService()
    inheritance_service.serve()
    
    # Additional assertions to validate the behavior
    assert isinstance(service_real_1.dao, DAO), "Expected DAO instance"
    assert isinstance(service_mock_1.dao, MockDAO), "Expected MockDAO instance"
    assert isinstance(service_real_1.logger, Logger), "Expected Logger instance"
    assert isinstance(service_real_1.model_service, ModelService), "Expected ModelService instance"

    print(f"\n[{framework_name}] All tests passed for {framework_name}.\n")

def setup_di_and_test(primary_framework, secondary_framework):
    adapter = InteroperableDIAdapter(primary_framework, secondary_framework)
    primary_di_adapter = DIAdapterFactory.get_di_adapter(primary_framework)
    secondary_di_adapter = DIAdapterFactory.get_di_adapter(secondary_framework)

    # Bind dependencies in the primary framework
    primary_di_adapter.bind(DAO, DAO, is_singleton=True)
    primary_di_adapter.bind(ModelService, ModelService, is_singleton=False)

    # Integrate dependencies across frameworks (Singleton instance sharing)
    adapter.connect_frameworks(DAO, from_secondary=False, name=None, is_singleton=True)
    
    # Prototype instances should be created fresh in each framework
    adapter.connect_frameworks(ModelService, from_secondary=False, name=None, is_singleton=False)

    # Use integrate_dependency to ensure both frameworks recognize the same instance
    adapter.integrate_dependency(DAO, DAO, name=None)
    adapter.integrate_dependency(ModelService, ModelService, name=None)

    # Test Singleton consistency using shared registry
    registry_DAO_instance_1 = adapter.get(DAO)
    registry_DAO_instance_2 = adapter.get(DAO)
    print(f"[{primary_framework} & {secondary_framework}] DAO instance 1 ID: {id(registry_DAO_instance_1)}, instance 2 ID: {id(registry_DAO_instance_2)}")

    # Test ModelService with prototype behavior
    model_service_instance_1 = adapter.get(ModelService)
    model_service_instance_2 = adapter.get(ModelService)
    print(f"[{primary_framework} & {secondary_framework}] ModelService instance 1 ID: {id(model_service_instance_1)}, instance 2 ID: {id(model_service_instance_2)}")
    model_service_instance_1.generate_session()
    model_service_instance_2.generate_session()
    
    # Test Singleton consistency across frameworks
    # DAO_instance_1 = secondary_di_adapter.get(DAO)
    # DAO_instance_2 = secondary_di_adapter.get(DAO)
    # print(f"[{primary_framework} & {secondary_framework}] DAO instance 1 ID: {id(DAO_instance_1)}, instance 2 ID: {id(DAO_instance_2)}")
    
    # Test ModelService with prototype behavior across frameworks
    # model_service_instance_1 = secondary_di_adapter.get(ModelService)
    # model_service_instance_2 = secondary_di_adapter.get(ModelService)
    # print(f"[{primary_framework} & {secondary_framework}] ModelService instance 1 ID: {id(model_service_instance_1)}, instance 2 ID: {id(model_service_instance_2)}")
    # model_service_instance_1.generate_session()
    # model_service_instance_2.generate_session()

if __name__ == "__main__":
    # frameworks = ['injector', 'dependency_injector', 'pinject', 'wired']
    frameworks = ['dependency_injector', 'injector']
    for framework in frameworks:
        print(f"\n========== DIAdapterFactory Testing(swap framework): Running tests for {framework} (each life cycle for singleton) ==========")
        test_multiple_implementations(framework)

    for primary, secondary in [('injector', 'dependency_injector'), ('dependency_injector', 'injector')]:
        print(f"\n========== InteroperableDIAdapter Testing: Running tests for {primary} with {secondary} ==========")
        setup_di_and_test(primary, secondary)
