import os
import sys

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path):
    with open(path, 'w') as f:
        f.write("# Placeholder\n")

def create_project_structure(base_path):
    # Project root
    create_directory(base_path)

    # Config
    create_directory(os.path.join(base_path, "config"))
    create_directory(os.path.join(base_path, "config", "settings"))
    create_file(os.path.join(base_path, "config", "__init__.py"))
    create_file(os.path.join(base_path, "config", "settings", "__init__.py"))
    create_file(os.path.join(base_path, "config", "settings", "base.py"))
    create_file(os.path.join(base_path, "config", "settings", "development.py"))
    create_file(os.path.join(base_path, "config", "settings", "production.py"))
    create_file(os.path.join(base_path, "config", "urls.py"))
    create_file(os.path.join(base_path, "config", "wsgi.py"))
    create_file(os.path.join(base_path, "config", "asgi.py"))

    # Core
    create_directory(os.path.join(base_path, "core"))
    create_file(os.path.join(base_path, "core", "__init__.py"))

    # Core - Domain
    for domain in ["user", "order"]:
        domain_path = os.path.join(base_path, "core", "domain", domain)
        create_directory(domain_path)
        create_file(os.path.join(domain_path, "__init__.py"))
        create_file(os.path.join(domain_path, "entities.py"))
        create_file(os.path.join(domain_path, "value_objects.py"))
        create_file(os.path.join(domain_path, "aggregates.py"))
        create_file(os.path.join(domain_path, "events.py"))

    # Core - Application
    create_directory(os.path.join(base_path, "core", "application"))
    create_file(os.path.join(base_path, "core", "application", "__init__.py"))
    create_directory(os.path.join(base_path, "core", "application", "interfaces"))
    create_file(os.path.join(base_path, "core", "application", "interfaces", "__init__.py"))
    create_file(os.path.join(base_path, "core", "application", "interfaces", "repositories.py"))
    create_file(os.path.join(base_path, "core", "application", "interfaces", "services.py"))

    for domain in ["user", "order"]:
        domain_path = os.path.join(base_path, "core", "application", domain)
        create_directory(domain_path)
        create_file(os.path.join(domain_path, "__init__.py"))
        create_file(os.path.join(domain_path, "dtos.py"))
        create_file(os.path.join(domain_path, "use_cases.py"))
        create_file(os.path.join(domain_path, "services.py"))

    # Core - Infrastructure
    create_directory(os.path.join(base_path, "core", "infrastructure"))
    create_file(os.path.join(base_path, "core", "infrastructure", "__init__.py"))
    create_directory(os.path.join(base_path, "core", "infrastructure", "db"))
    create_file(os.path.join(base_path, "core", "infrastructure", "db", "__init__.py"))
    create_directory(os.path.join(base_path, "core", "infrastructure", "db", "models"))
    create_file(os.path.join(base_path, "core", "infrastructure", "db", "models", "__init__.py"))
    create_file(os.path.join(base_path, "core", "infrastructure", "db", "models", "user_models.py"))
    create_file(os.path.join(base_path, "core", "infrastructure", "db", "models", "order_models.py"))
    create_directory(os.path.join(base_path, "core", "infrastructure", "db", "repositories"))
    create_file(os.path.join(base_path, "core", "infrastructure", "db", "repositories", "__init__.py"))
    create_file(os.path.join(base_path, "core", "infrastructure", "db", "repositories", "user_repository.py"))
    create_file(os.path.join(base_path, "core", "infrastructure", "db", "repositories", "order_repository.py"))
    create_directory(os.path.join(base_path, "core", "infrastructure", "services"))
    create_file(os.path.join(base_path, "core", "infrastructure", "services", "__init__.py"))
    create_file(os.path.join(base_path, "core", "infrastructure", "services", "external_service.py"))

    # API
    create_directory(os.path.join(base_path, "api"))
    create_file(os.path.join(base_path, "api", "__init__.py"))
    create_directory(os.path.join(base_path, "api", "v1"))
    create_file(os.path.join(base_path, "api", "v1", "__init__.py"))
    create_directory(os.path.join(base_path, "api", "v1", "serializers"))
    create_file(os.path.join(base_path, "api", "v1", "serializers", "__init__.py"))
    create_file(os.path.join(base_path, "api", "v1", "serializers", "user_serializers.py"))
    create_file(os.path.join(base_path, "api", "v1", "serializers", "order_serializers.py"))
    create_directory(os.path.join(base_path, "api", "v1", "views"))
    create_file(os.path.join(base_path, "api", "v1", "views", "__init__.py"))
    create_file(os.path.join(base_path, "api", "v1", "views", "user_views.py"))
    create_file(os.path.join(base_path, "api", "v1", "views", "order_views.py"))
    create_file(os.path.join(base_path, "api", "v1", "urls.py"))
    create_file(os.path.join(base_path, "api", "v1", "schemas.py"))
    create_directory(os.path.join(base_path, "api", "middlewares"))
    create_file(os.path.join(base_path, "api", "middlewares", "__init__.py"))
    create_file(os.path.join(base_path, "api", "middlewares", "auth_middleware.py"))
    create_directory(os.path.join(base_path, "api", "validators"))
    create_file(os.path.join(base_path, "api", "validators", "__init__.py"))
    create_file(os.path.join(base_path, "api", "validators", "user_validators.py"))
    create_file(os.path.join(base_path, "api", "validators", "order_validators.py"))
    create_directory(os.path.join(base_path, "api", "docs"))
    create_file(os.path.join(base_path, "api", "docs", "__init__.py"))
    create_file(os.path.join(base_path, "api", "docs", "openapi.py"))
    create_file(os.path.join(base_path, "api", "docs", "schema.yml"))

    # Cross-cutting concerns
    create_directory(os.path.join(base_path, "cross_cutting"))
    create_file(os.path.join(base_path, "cross_cutting", "__init__.py"))
    for concern in ["logging", "auth", "caching", "messaging", "monitoring", "error_handling", "validation"]:
        concern_path = os.path.join(base_path, "cross_cutting", concern)
        create_directory(concern_path)
        create_file(os.path.join(concern_path, "__init__.py"))
        create_file(os.path.join(concern_path, f"{concern}.py"))

    # Tests
    create_directory(os.path.join(base_path, "tests"))
    create_file(os.path.join(base_path, "tests", "__init__.py"))
    for test_type in ["unit", "integration", "e2e"]:
        test_path = os.path.join(base_path, "tests", test_type)
        create_directory(test_path)
        create_file(os.path.join(test_path, "__init__.py"))

    # Requirements
    create_directory(os.path.join(base_path, "requirements"))
    create_file(os.path.join(base_path, "requirements", "base.txt"))
    create_file(os.path.join(base_path, "requirements", "development.txt"))
    create_file(os.path.join(base_path, "requirements", "production.txt"))

    # Root level files
    create_file(os.path.join(base_path, "manage.py"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_project_structure.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    base_path = os.path.join(os.getcwd(), project_name)
    create_project_structure(base_path)
    print(f"Project structure created at: {base_path}")