import os

def find_all_folders_with_py_files(base_folder):
    folders = {}
    for root, dirs, files in os.walk(base_folder):
        py_files = [f for f in files if f.endswith(".py") and f != "main.py"]
        if py_files:
            relative_root = os.path.relpath(root, start=base_folder)
            folders[relative_root] = py_files
    return folders

def run_python_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    exec(code, {"__name__": "__main__"})

def main():
    base_folder = "."

    while True:
        folders = find_all_folders_with_py_files(base_folder)

        print("\nAvailable folders with Python files:")
        for folder in folders:
            print(f" - {folder}")
        print("Type 'q' to quit.")

        folder_choice = input("\nEnter the folder name: ").strip()

        if folder_choice.lower() == "q":
            print("Exiting...")
            break

        if folder_choice not in folders:
            print("Folder not found or contains no Python files.")
            continue

        print(f"\nAvailable Python files in '{folder_choice}':")
        for file in folders[folder_choice]:
            print(f" - {file}")

        file_choice = input("\nEnter the Python file name to run: ").strip()

        if file_choice not in folders[folder_choice]:
            print("File not found in that folder.")
            continue

        filepath = os.path.join(base_folder, folder_choice, file_choice)
        print(f"\n--- Running {filepath} ---\n")
        try:
            run_python_file(filepath)
        except Exception as e:
            print(f"Error while running {filepath}:\n{e}")
        print("\n--- Done ---")

if __name__ == "__main__":
    main()
