import tkinter as tk
import subprocess
import threading

class CodeEditor(tk.Text):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg="#2B2B2B",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            bd=0,
            highlightthickness=0,
            font=("Consolas", 12)
        )
        self.pack(fill=tk.BOTH, expand=True)

class CommandInput(tk.Text):
    def __init__(self, parent, editor=None, quit_callback=None):
        super().__init__(
            parent,
            height=1,
            bg="#2B2B2B",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            bd=0,
            highlightthickness=0,
            font=("Consolas", 12)
        )
        self.editor = editor
        self.quit_callback = quit_callback
        self.visible = False
        self.bind("<Return>", self.execute_command)

    def toggle(self, prefill=None):
        if self.visible:
            self.pack_forget()
            self.visible = False
        else:
            self.pack(fill=tk.X)
            self.focus_set()
            self.visible = True
            self.delete("1.0", tk.END)
            if prefill:
                self.insert("1.0", prefill)

    def execute_command(self, event=None):
        command = self.get("1.0", tk.END).strip()
        if command:
            Command(command=command, editor=self.editor, quit_callback=self.quit_callback)
        self.delete("1.0", tk.END)
        return "break"

class TerminalWindow:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None or not cls._instance.window.winfo_exists():
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, 'initialized') and self.initialized:
            return

        self.window = tk.Toplevel()
        self.window.title("Terminal Output")
        self.window.geometry("600x400")
        self.window.configure(bg="#1E1E1E")

        self.text = tk.Text(
            self.window,
            bg="#000000",
            fg="#19B419",
            insertbackground="#00FF00",
            font=("Consolas", 12),
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.text.pack(fill=tk.BOTH, expand=True)

        self.initialized = True

    def run_command(self, command):
        def target():
            self.append_text(f"\n$ {command}\n")
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                text=True
            )
            for line in iter(process.stdout.readline, ''):
                self.append_text(line)
            process.stdout.close()
            process.wait()
            self.append_text("[Process finished]\n")
        threading.Thread(target=target, daemon=True).start()

    def append_text(self, text):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, text)
        self.text.see(tk.END)
        self.text.config(state=tk.DISABLED)

class Command:
    def __init__(self, command, editor=None, quit_callback=None):
        self.editor = editor
        self.quit_callback = quit_callback

        if command.startswith(":"):
            self.handle_editor_command(command)
        else:
            term_win = TerminalWindow()
            term_win.run_command(command)

    def handle_editor_command(self, command):
        parts = command[1:].split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        if cmd == "w":
            filename = arg if arg else "output.txt"
            self.save_file(filename)
        elif cmd == "q":
            if self.quit_callback:
                self.quit_callback()
        else:
            print(f"[Unknown command: {command}]")

    def save_file(self, filename):
        if not self.editor:
            return
        content = self.editor.get("1.0", tk.END)
        try:
            with open(filename, "w") as f:
                f.write(content)
            print(f"[File saved to {filename}]")
        except Exception as e:
            print(f"[Failed to save file: {e}]")

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.configure(background='#2B2B2B')

        self.in_command_mode = False

        self.setup_frames()
        self.setup_widgets()
        self.setup_keybindings()

        self.window.mainloop()

    def setup_frames(self):
        self.code_frame = tk.Frame(self.window, bg="#2B2B2B")
        self.command_frame = tk.Frame(self.window, bg="#2B2B2B")

        self.code_frame.pack(fill=tk.BOTH, expand=True)
        self.command_frame.pack(fill=tk.X)

    def setup_widgets(self):
        self.editor = CodeEditor(self.code_frame)
        self.command_input = CommandInput(
            self.command_frame,
            editor=self.editor,
            quit_callback=self.window.destroy
        )

    def setup_keybindings(self):
        self.window.bind("<Escape>", self.enter_command_mode)
        self.window.bind(":", self.check_colon)

    def enter_command_mode(self, event=None):
        self.in_command_mode = True

    def check_colon(self, event=None):
        if self.in_command_mode:
            self.command_input.toggle(prefill=":")
        self.in_command_mode = False

if __name__ == '__main__':
    App()
