# src/services/aggregation_service.py

from src.services.interfaces import IService

class AggregationService:
    """Service to aggregate results from multiple IService implementations."""

    def __init__(self, service1: IService, service2: IService):
        self.service1 = service1
        self.service2 = service2

    def aggregate(self):
        print("AggregationService: Aggregating results from two services...")
        self.service1.serve()
        self.service2.serve()
