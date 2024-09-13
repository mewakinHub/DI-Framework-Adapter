# How the DI Adapter Pattern Works

## Overview
The DI Adapter pattern is designed to handle multiple Dependency Injection (DI) frameworks within a single application. This allows the application to remain flexible, modular, and easy to maintain, regardless of which DI framework is being used. 

**Docs:**
- [adapter_pattern](docs/adapter_pattern.md)
- [singleton](docs/singleton.md)
- [implementation](docs/implementation.md)

- การสร้าง Adapter Pattern แบบทั่วไปเพื่อให้รองรับทุก DI framework อาจไม่จำเป็นและใช้เวลาโดยเปล่าประโยชน์
- ในทางกลับกัน ควรมุ่งเน้นที่การสร้าง Adapter ที่ทำหน้าที่เชื่อมโยงระหว่างสองหรือหลาย DI frameworks เพื่อให้สามารถทำงานร่วมกันได้ในโปรเจ็กต์ที่มีอยู่แล้ว
- สิ่งนี้จะช่วยให้คุณสามารถใช้ฟีเจอร์เฉพาะของแต่ละ DI framework ในขณะที่ยังคงความสามารถในการทำงานร่วมกันได้ระหว่าง framework ต่างๆ

 The InjectorAdapter was updated to handle named bindings correctly since injector doesn't natively support the name argument in the same way dependency-injector does.

1. Singleton instances are shared across both frameworks.
2. Prototype instances are independently created in each framework (cloned as needed).

## Key Components of the DI Adapter Pattern

1. **Common Interface (`DIContainerAdapter`) (Target Interface)**: 
   - This interface defines the contract for dependency management operations (`bind` and `get`). All adapters for different DI frameworks will implement this interface.

2. **Framework-Specific Adapters (Adaptee)**:
   - **InjectorAdapter**: Adapter for the `injector` DI framework.
   - **DependencyInjectorAdapter**: Adapter for the `dependency-injector` DI framework.
   - **PinjectAdapter**: Adapter for the `pinject` DI framework.
   - **WiredAdapter**: Adapter for the `wired` DI framework.
   - Each adapter provides a framework-specific implementation for the `bind` and `get` methods.

3. **Dynamic Adapter Selection (Adapter)**:
   - The application dynamically selects the DI adapter based on the configuration file. This allows it to work with any of the supported DI frameworks without changing the core logic.

4. **Client:** The code that uses the target interface.

### Sources
- [Pinject GitHub Repository](https://github.com/google/pinject)
- [Wired Documentation](https://wired.readthedocs.io/en/stable/)
- [Injector Documentation](https://injector.readthedocs.io/en/latest/)
- [Python Dependency Injector Documentation](https://python-dependency-injector.ets-labs.org/)

### Set-up

#### Step 1: Create the Environment from the YAML File

Run the following command to create the environment with both Conda and pip packages:

```bash
conda env create -f environment.yml
```

This command will:

1. Create a new environment named `DI-Adapter`.
2. Install all Conda packages listed under `dependencies`.
3. Install the pip packages using the pip tool within the Conda environment.

#### Step 2: Activate and Use the Environment

Activate the environment with:

```bash
conda activate DI-Adapter
```

After activation, all packages (both Conda-managed and pip-managed) will be available, and you can verify this by running:

```bash
conda list  # This will show all packages, including pip-installed ones
```

#### Step 3: Updating the Environment

If you need to add more packages later, you can update your environment with:

```bash
conda env update --file environment.yml --prune
```

The `--prune` flag removes dependencies that are no longer required from the environment.