TextEditor/
│
├── main.py                         # Entry point of your app
│
├── core/                           # Core functionality
│   ├── editor.py                   # Main text editor logic (insert, delete, undo, etc.)
│   ├── commands.py                 # Logic for command line parsing/handling
│   ├── settings.py                 # Logic to load/save settings
│
├── gui/                            # GUI-specific components
│   ├── window.py                   # Main window setup
│   ├── command_line.py             # Custom Entry + command execution logic
│   ├── colours.py                  # Centralized color definitions
│
├── data/                           # Configuration or persistent data
│   └── settings.json
│
├── resources/                      # Static resources (images, icons)
│   └── assets/
│       └── TextEditorIcon.png
│
├── utils/                          # Utility functions (optional)
│   ├── file_io.py                  # File reading/saving logic
│   ├── fpath_error_handling.py     # Custom Error Support
│   └── colour_format.py            # Correct Colour Formatting
│
├── __pycache__/                    # Auto-generated
├── PROJECT_TREE.md                 # Tree Diagram Of Folders
└── README.md                       # Project info/instructions