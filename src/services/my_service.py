# src/services/my_service.py

# from src.services.interfaces import IService
from src.services.dao import DAO
from src.services.logger import Logger
from src.services.model_service import ModelService

# class MyService(IService):
class MyService():
    """A concrete implementation of the IService interface."""

    def __init__(self, dao: DAO, logger: Logger, model_service: ModelService):
        # Dependencies are injected here
        self.dao = dao
        self.logger = logger
        self.model_service = model_service
        # print(f"MyService instance id={id(self)} with DAO id={id(self.dao)}, Logger id={id(self.logger)}, ModelService id={id(self.model_service)}")

    def serve(self):
        # Use the injected dependencies
        self.logger.log("MyService is serving using DAO and ModelService.")
        self.dao.connect()
        self.model_service.generate_session()
        print(f"MyService instance id={id(self)} with DAO id={id(self.dao)}, Logger id={id(self.logger)}, ModelService id={id(self.model_service)}")
