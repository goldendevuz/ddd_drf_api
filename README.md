# Django REST Framework DDD Project Template

This project template provides a structured foundation for building scalable and maintainable Django REST Framework (DRF) applications using Domain-Driven Design (DDD) principles and Clean Architecture.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Architecture Overview](#architecture-overview)
3. [Detailed Project Structure](#detailed-project-structure)
4. [Getting Started](#getting-started)
5. [Development Guidelines](#development-guidelines)
6. [Project-wide Configuations](#project-wide-configurations)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)

## Project Structure

```
myproject/
├── manage.py
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── domain/
│   ├── application/
│   └── infrastructure/
├── api/
│   ├── v1/
│   ├── middlewares/
│   ├── validators/
│   └── docs/
├── cross_cutting/
├── tests/
└── requirements/
```

## Architecture Overview

This template follows a layered architecture based on DDD and Clean Architecture principles:

1. **Domain Layer** (`core/domain/`): Contains the core business logic, entities, value objects, and domain events.

2. **Application Layer** (`core/application/`): Houses use cases, application services, and interfaces for repositories and services.

3. **Infrastructure Layer** (`core/infrastructure/`): Implements interfaces defined in the application layer, including repositories and external services.

4. **API Layer** (`api/`): Handles HTTP requests/responses using Django REST Framework.

5. **Cross-Cutting Concerns** (`cross_cutting/`): Manages aspects like logging, authentication, and caching that span multiple layers.


## Detailed Project Structure
Below is the detailed structure of the project, followed by explanations of each major component:

```
myproject/
├── .gitignore
├── .editorconfig
├── .pre-commit-config.yaml
├── pyproject.toml
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   ├── entities.py
│   │   │   ├── value_objects.py
│   │   │   ├── aggregates.py
│   │   │   └── events.py
│   │   └── order/
│   │       ├── __init__.py
│   │       ├── entities.py
│   │       ├── value_objects.py
│   │       ├── aggregates.py
│   │       └── events.py
│   ├── application/
│   │   ├── __init__.py
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   ├── repositories.py
│   │   │   └── services.py
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   ├── dtos.py
│   │   │   ├── use_cases.py
│   │   │   └── services.py
│   │   └── order/
│   │       ├── __init__.py
│   │       ├── dtos.py
│   │       ├── use_cases.py
│   │       └── services.py
│   └── infrastructure/
│       ├── __init__.py
│       ├── db/
│       │   ├── __init__.py
│       │   ├── models/
│       │   │   ├── __init__.py
│       │   │   ├── user_models.py
│       │   │   └── order_models.py
│       │   └── repositories/
│       │       ├── __init__.py
│       │       ├── user_repository.py
│       │       └── order_repository.py
│       └── services/
│           ├── __init__.py
│           └── external_service.py
├── api/
│   ├── __init__.py
│   ├── v1/
│   │   ├── __init__.py
│   │   ├── serializers/
│   │   │   ├── __init__.py
│   │   │   ├── user_serializers.py
│   │   │   └── order_serializers.py
│   │   ├── views/
│   │   │   ├── __init__.py
│   │   │   ├── user_views.py
│   │   │   └── order_views.py
│   │   ├── urls.py
│   │   └── schemas.py
│   ├── middlewares/
│   │   ├── __init__.py
│   │   └── auth_middleware.py
│   ├── validators/
│   │   ├── __init__.py
│   │   ├── user_validators.py
│   │   └── order_validators.py
│   └── docs/
│       ├── __init__.py
│       ├── openapi.py
│       └── schema.yml
├── cross_cutting/
│   ├── __init__.py
│   ├── logging/
│   │   ├── __init__.py
│   │   └── logger.py
│   ├── auth/
│   │   ├── __init__.py
│   │   └── authentication.py
│   ├── caching/
│   │   ├── __init__.py
│   │   └── cache_manager.py
│   ├── messaging/
│   │   ├── __init__.py
│   │   └── event_bus.py
│   ├── monitoring/
│   │   ├── __init__.py
│   │   └── metrics.py
│   ├── error_handling/
│   │   ├── __init__.py
│   │   └── exceptions.py
│   └── validation/
│       ├── __init__.py
│       └── validator.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   ├── integration/
│   └── e2e/
└── requirements/
    ├── base.txt
    ├── development.txt
    └── production.txt
```

### Structure Breakdown

1. **config/**
   - Contains project-wide configuration files.
   - `settings/`: Separate settings for different environments.
   - `urls.py`: Main URL routing configuration.
   - `wsgi.py` and `asgi.py`: Entry points for WSGI and ASGI servers.

2. **core/**
   - The heart of the application, implementing DDD and Clean Architecture.
   
   a. **domain/**
      - Contains the core business logic and rules.
      - Separated into bounded contexts (e.g., user, order).
      - Each context includes:
        - `entities.py`: Core business objects.
        - `value_objects.py`: Immutable objects describing characteristics.
        - `aggregates.py`: Clusters of domain objects treated as a single unit.
        - `events.py`: Domain events for important business occurrences.
   
   b. **application/**
      - Houses use cases and application-specific logic.
      - `interfaces/`: Defines repository and service interfaces.
      - Each bounded context (e.g., user, order) includes:
        - `dtos.py`: Data Transfer Objects for input/output.
        - `use_cases.py`: Implementation of specific use cases.
        - `services.py`: Application services orchestrating domain logic.
   
   c. **infrastructure/**
      - Implements interfaces defined in the application layer.
      - `db/`: Database-related implementations.
        - `models/`: Django ORM models.
        - `repositories/`: Concrete implementations of repository interfaces.
      - `services/`: External service integrations.

3. **api/**
   - Handles HTTP requests/responses using Django REST Framework.
   - `v1/`: First version of the API.
     - `serializers/`: DRF serializers for data validation and conversion.
     - `views/`: DRF views (ViewSets, APIViews).
     - `urls.py`: URL routing for this API version.
   - `middlewares/`: Custom middleware (e.g., for authentication).
   - `validators/`: Custom validators for complex validation logic.
   - `docs/`: API documentation (OpenAPI/Swagger).

4. **cross_cutting/**
   - Manages aspects that span multiple layers of the application.
   - Includes modules for logging, authentication, caching, messaging, monitoring, error handling, and validation.

5. **tests/**
   - Structured test directory for different types of tests.
   - `unit/`: Tests for individual components in isolation.
   - `integration/`: Tests for interactions between components.
   - `e2e/`: End-to-end tests simulating user scenarios.

6. **requirements/**
   - Dependency management for different environments.

7. **Project-wide Configuration Files**
   - `.gitignore`: Specifies intentionally untracked files to ignore.
   - `.editorconfig`: Defines and maintains consistent coding styles between different editors and IDEs.
   - `.pre-commit-config.yaml`: Configuration for pre-commit hooks to ensure code quality before commits.
   - `pyproject.toml`: Configuration file for Python tools like Black, isort, and others.
   - `README.md`: Project documentation and overview (this file).

This structure enforces a clear separation of concerns, adhering to DDD principles and Clean Architecture. It promotes modularity, testability, and scalability of the application.



## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/onlythompson/drf-ddd-template.git
   cd drf-ddd-template
   ```

2. Create your project structure using the provided script:
   ```
   python create_project_structure.py your_project_name
   ```
   This script will create a new directory with your project name and set up the entire project structure as defined in this template.

3. Navigate to your new project directory:
   ```
   cd your_project_name
   ```

4. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

5. Install dependencies:
   ```
   pip install -r requirements/development.txt
   ```

6. Apply migrations:
   ```
   python manage.py migrate
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```
8. Set up pre-commit hooks:
   ```
   pre-commit install
   ```

9. Review and adjust the project-wide configuration files (`.gitignore`, `.editorconfig`, `pyproject.toml`) as needed for your specific project requirements.

### About the Project Structure Script

The `create_project_structure.py` script is a crucial part of this template. It automates the process of setting up your project structure, ensuring that all necessary directories and placeholder files are created according to the DDD and Clean Architecture principles we're following.

Key features of the script:
- Creates all directories and subdirectories as per our architecture.
- Generates placeholder Python files for all the modules we've defined.
- Customizable: You can easily modify it to add or remove directories/files as your project evolves.

To view or modify the script, open `create_project_structure.py` in your text editor.

## Development Guidelines

1. **Domain Layer**: 
   - Define entities, value objects, and aggregates in `core/domain/`.
   - Keep this layer free from framework-specific code.

2. **Application Layer**:
   - Implement use cases in `core/application/*/use_cases.py`.
   - Define interfaces for repositories and services in `core/application/interfaces/`.

3. **Infrastructure Layer**:
   - Implement repositories in `core/infrastructure/db/repositories/`.
   - Place external service integrations in `core/infrastructure/services/`.

4. **API Layer**:
   - Define serializers in `api/v1/serializers/`.
   - Implement views in `api/v1/views/`.
   - Use `api/v1/urls.py` for routing.

5. **Cross-Cutting Concerns**:
   - Implement logging, caching, etc., in their respective directories under `cross_cutting/`.

## Project-wide Configurations

This project includes several configuration files to ensure code quality, maintain consistency, and improve the development workflow. Below is an overview of each configuration file and how to use it effectively.

### .gitignore

The `.gitignore` file specifies intentionally untracked files that Git should ignore. Our configuration includes rules for:

- Python artifacts (`.pyc`, `__pycache__`, etc.)
- Django specific files (local settings, database files, media files)
- Virtual environment directories
- IDE and editor files
- OS generated files
- Testing artifacts
- Dependency directories

To use: This file works automatically with Git once it's in your project root.

### .editorconfig

The `.editorconfig` file helps maintain consistent coding styles across various editors and IDEs. It includes settings for:

- Character encoding
- Indentation styles and sizes for different file types
- Line endings
- Trimming trailing whitespace

To use: Many editors support EditorConfig out of the box. For others, you may need to install a plugin. Once set up, it works automatically.

### .pre-commit-config.yaml

This file configures pre-commit hooks to automate code quality checks before each commit. It includes hooks for:

- Code formatting (Black, isort)
- Linting (Flake8)
- Type checking (MyPy)
- Django-specific checks
- General file checks (trailing whitespace, large files, etc.)

To use:
1. Install pre-commit: `pip install pre-commit`
2. Set up the git hook scripts: `pre-commit install`
3. (Optional) Run against all files: `pre-commit run --all-files`

Now, pre-commit will run automatically on `git commit`.

### pyproject.toml

The `pyproject.toml` file is a centralized configuration file for various Python tools. Our configuration includes settings for:

- Black (code formatter)
- isort (import sorter)
- MyPy (static type checker)
- Pytest (testing framework)
- Coverage (code coverage tool)
- Poetry (dependency management)

To use: Most tools will automatically detect and use the configurations in this file. For Poetry, you'll need to use Poetry commands for dependency management.

## Using These Configurations

1. Ensure all configuration files (`.gitignore`, `.editorconfig`, `.pre-commit-config.yaml`, `pyproject.toml`) are in your project root.

2. Install necessary tools:
   ```
   pip install pre-commit black isort flake8 mypy django-stubs pytest pytest-django coverage django-coverage-plugin
   ```

3. Set up pre-commit hooks:
   ```
   pre-commit install
   ```

4. (Optional) If using Poetry for dependency management:
   ```
   poetry install
   ```

These configurations provide a solid foundation for maintaining code quality and consistency. However, feel free to adjust them to better suit your project's specific needs.

## Testing

- Unit tests: `python manage.py test tests.unit`
- Integration tests: `python manage.py test tests.integration`
- E2E tests: `python manage.py test tests.e2e`

## Deployment

1. Update `config/settings/production.py` with production-specific settings.
2. Use `requirements/production.txt` for production dependencies.
3. Set appropriate environment variables for sensitive information.
4. Follow Django's deployment checklist: https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests for your changes.
4. Ensure all tests pass and the code adheres to the project's style guide.
5. Submit a pull request with a clear description of your changes.

---

This template is designed to provide a solid starting point for your DRF project using DDD principles. Feel free to adapt it to your specific needs as your project evolves.

For more detailed information on DDD and Clean Architecture, refer to:
- [Domain-Driven Design](https://domainlanguage.com/ddd/) by Eric Evans
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) by Robert C. Martin

Happy coding!