# src/services/model_service.py

import uuid

class ModelService:
    """Service for generating a unique session."""

    def __init__(self):
        self.session_id = None

    def generate_session(self):
        """Generate a new session ID."""
        self.session_id = uuid.uuid4()
        print(f"ModelService generated new session ID: {self.session_id}")
