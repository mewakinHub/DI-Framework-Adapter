my_project/
├── domain/
│   ├── models/
│   └── services/
├── application/
│   ├── use_cases/
│   └── dtos/
├── infrastructure/
│   ├── di/
│   │   ├── __init__.py
│   │   ├── main_container.py
│   │   └── adapters/
│   │       ├── __init__.py
│   │       ├── dependency_injector_adapter.py
│   │       ├── pydantic_adapter.py
│   │       └── built_in_adapter.py
│   ├── repositories/
│   └── services/
├── presentation/
│   ├── api/
│   └── cli/
├── tests/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   ├── presentation/
│   └── __init__.py
└── main.py
