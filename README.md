# Handling Multiple DI Frameworks within Hexagonal Architecture

## 1st Assignment: (โจทย์ POC)

- get code from ML workshop and convert into python script
- implement multiple Dependencies Injections(pattern) by using python library/framework such as Dependencies injector(tools/lib/opensource), build-in python, etc.
    
    DI framework: https://python-dependency-injector.ets-labs.org/
    
- convert multiple DI lib. by using Adaptor pattern (this step is core task)
- convert multiple DI lib. by using strategy pattern? (select which framework gonna use, how to implement along with port and adaptor???)
    - the way developers in team using DI maybe not the same?? how to create best defined strategy?

Finish & monitor

- ทำได้แล้วให้สร้าง Backlogs azure ต่อ (อันนี้อาจจะยังไม่ต้อง เพราะยังไม่ได้ Azure Workshop)

---

Project:

- creating based project implementing DI
- 3 approaches of handling multiple DI frameworks - Adapter Pattern, Strategy Pattern, and Hexagonal Architecture
    - compare both code and insight such as maintenance, learning curve
    - 3 branches on Git
    - for Adapter Pattern, using Dependency injector for main tool
        - python generate_structure.py structure_adapter_pattern.md
    - for Strategy Pattern,
        - python generate_structure.py structure_strategy_pattern.md
    - for Hexagonal Architecture,
        - python generate_structure.py structure_hexagonal_architecture.md

In the Python ecosystem, certain DI frameworks and tools are more popular and commonly used than others. Here’s an overview of their use cases and prevalence:

1. **Dependency Injector**
    - **Popularity**: High
    - **Use Cases**: Large-scale applications requiring robust dependency management. It's known for its flexibility and comprehensive features.
    - **Insights**: Widely adopted in enterprise-level applications due to its extensive capabilities in managing complex dependencies.
2. **Pydantic**
    - **Popularity**: High
    - **Use Cases**: Data validation, settings management, and type enforcement. It's often used in API development, data processing, and configuration management.
    - **Insights**: While not a traditional DI framework, Pydantic is heavily used in conjunction with DI frameworks for data validation purposes.
3. **Flask-Injector**
    - **Popularity**: Moderate
    - **Use Cases**: Web applications built with Flask. It integrates seamlessly with Flask, making it easier to manage dependencies within Flask applications.
    - **Insights**: Preferred by Flask developers who need DI capabilities but want to stay within the Flask ecosystem.
4. **Django’s Built-in DI Tools**
    - **Popularity**: High (within the Django community)
    - **Use Cases**: Web applications built with Django. It leverages Django’s built-in mechanisms to manage dependencies, though not as advanced as dedicated DI frameworks.
    - **Insights**: Often used by Django developers who prefer to stick with Django’s native features rather than introducing external DI frameworks.
5. **Python’s Built-in Tools**
    - **Popularity**: High (for small to medium projects)
    - **Use Cases**: Simple applications or scripts where full-fledged DI frameworks are overkill. Standard Python features are used to achieve basic DI.
    - **Insights**: Commonly used in smaller projects or for quick prototypes where introducing a full DI framework would be unnecessary overhead.
