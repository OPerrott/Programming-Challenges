# main.py

import os
import sys
import importlib
from problems.registry import PROBLEM_REGISTRY

def auto_import_problems():
    problems_dir = "problems"
    for filename in os.listdir(problems_dir):
        if filename.endswith(".py") and filename not in ("__init__.py", "registry.py"):
            module_name = f"problems.{filename[:-3]}"
            importlib.import_module(module_name)

def run_problem(class_name):
    # Live reload the module where the class is defined
    for module_name, module in sys.modules.items():
        if module_name.startswith("problems.") and hasattr(module, class_name):
            importlib.reload(module)
            break  # reload only once

    # Get latest class from the registry
    cls = PROBLEM_REGISTRY.get(class_name)
    if cls is None:
        print(f"No class named '{class_name}' found.")
        return

    instance = cls()
    instance.run()

class Main:
    def __init__(self):
        self.curr = None
        self.running = True

        while self.running:
            self.command = input("% ").strip()
            self.validate_command()

    def validate_command(self):
        if self.command == "change file":
            self.curr = input(f"{self.curr} -> ").strip()

        elif self.command == "curr":
            print(self.curr)

        elif self.command == "run":
            if not self.curr:
                print("No file selected. Use 'change file' first.")
            else:
                run_problem(self.curr)

        elif self.command == "end":
            self.running = False

        elif self.command == "cls":
            os.system("cls" if os.name == "nt" else "clear")

        elif self.command == "list":
            print("Available problems:")
            for name in PROBLEM_REGISTRY:
                print("-", name)

        else:
            print(f"Unknown command: '{self.command}'")

if __name__ == '__main__':
    os.system("cls" if os.name == "nt" else "clear")
    auto_import_problems()
    Main()
