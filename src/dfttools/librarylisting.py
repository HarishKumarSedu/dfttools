import pkg_resources
import inspect
import importlib
import json

def get_python_suggestions():
    # List all installed libraries
    installed_packages = [pkg.key for pkg in pkg_resources.working_set]

    # Unified list for all suggestions
    suggestions = []

    for package in installed_packages:
        try:
            module = importlib.import_module(package)
            
            # Add library name as a suggestion
            suggestions.append(package)
            # Get functions with their definitions (signatures and docstrings)
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                func_signature = inspect.signature(obj)
                func_doc = inspect.getdoc(obj)
                suggestions.append(f"{name}{func_signature}")
                suggestions.append(f"{name}")
            
            # Get keywords (includes attributes, classes, etc.)
            for keyword in dir(module):
                suggestions.append(f"{keyword}")
            
        except Exception:
            # Skip libraries that cannot be imported
            continue
    suggestions = list(set(suggestions))
    # Write suggestions to a file
    with open('suggestions.json', 'w') as file:
        json.dump(suggestions, file)

if __name__ == "__main__":
    get_python_suggestions()



