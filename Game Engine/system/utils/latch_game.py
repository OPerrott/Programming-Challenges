import os
from importlib.util import spec_from_file_location, module_from_spec

class Latch:
    def __init__(self, window):
        self.window = window

        if self.check_drives():
            main_path = "D:\\main\\main.py"
            if os.path.exists(main_path):
                try:
                    # Dynamically import main.py
                    spec = spec_from_file_location("main_module", main_path)
                    main_module = module_from_spec(spec)
                    spec.loader.exec_module(main_module)

                    # Now run main_module.Main(window)
                    main_module.Main(window)

                    self.window.LOADED_GAME = True
                except Exception as e:
                    print(f"Failed to run main.py: {e}")
            else:
                print(f"{main_path} does not exist.")
        else:
            print("D drive not found.")

    def check_drives(self):
        return os.path.exists("D:\\")
