# Singleton and Instance Scoping in DI Frameworks

This document provides an overview of the default and available scopes for managing dependency lifecycles across four different Dependency Injection (DI) frameworks: `pinject`, `wired`, `injector`, and `dependency-injector`.

## Overview

In Dependency Injection, scoping determines whether the same instance of a class is reused (singleton) or if a new instance is created each time it is requested (transient or factory). This document outlines the default behavior and available scopes for each framework.

## Framework Scopes

| Framework              | Default Scope    | Other Scopes Available                        | Description |
|------------------------|------------------|-----------------------------------------------|-------------|
| **`pinject`**          | Singleton        | Prototype, Custom Scopes                      | Reuses the same instance by default unless explicitly configured otherwise. |
| **`wired`**            | Singleton        | Factory (Transient), Custom Scopes            | Services are registered as singletons by default. Factory scope allows for new instance creation with each request. |
| **`injector`**         | Transient        | Singleton, Custom Scopes                      | Creates a new instance each time by default. Singleton scope reuses the same instance. |
| **`dependency-injector`** | None (Explicit) | Singleton, Factory (Transient), ThreadLocalSingleton, CoroutineScoped, Custom Providers | Requires explicit definition of scope; does not default to singleton or factory. |

## Detailed Descriptions

### 1. `pinject`
- **Default Scope:** Singleton.
- **Other Scopes:**
  - **Prototype:** Each request results in a new instance.
  - **Custom Scopes:** Can define custom scope behaviors using decorators.

### 2. `wired`
- **Default Scope:** Singleton.
- **Other Scopes:**
  - **Factory (Transient):** Each request results in a new instance.
  - **Custom Scopes:** Custom lifecycle management through registry.

### 3. `injector`
- **Default Scope:** Transient.
- **Other Scopes:**
  - **Singleton:** Reuses the same instance.
  - **Custom Scopes:** Allows for custom scope creation, useful in specific contexts like web applications.

### 4. `dependency-injector`
- **Default Scope:** None (Need to Explicitly defined).
- **Other Scopes:**
  - **Singleton:** Reuses the same instance.
  - **Factory (Transient):** Creates a new instance with each request.
  - **ThreadLocalSingleton:** Singleton per thread.
  - **CoroutineScoped:** Singleton per asyncio task.
  - **Custom Providers:** Can define complex custom scopes and providers.

## Summary

Understanding the default and available scoping options in DI frameworks is crucial for designing efficient and maintainable applications. By leveraging the appropriate scope, developers can ensure that their applications perform as expected and manage resources efficiently.

### Sources
- [Pinject GitHub Repository](https://github.com/google/pinject)
- [Wired Documentation](https://wired.readthedocs.io/en/stable/)
- [Injector Documentation](https://injector.readthedocs.io/en/latest/)
- [Python Dependency Injector Documentation](https://python-dependency-injector.ets-labs.org/)
