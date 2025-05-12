from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

commands = {
    "download"  :   "class:download",
    "help"      :   "class:help",
    "view"      :   "class:view",
    "list"      :   "class:list",
    "ls"        :   "class:ls",
    
    "end"       :   "class:end",
    "stop"      :   "class:stop",
    
    "cls"       :   "class:cls",
    "clear"     :   "class:clear"
}
completer = WordCompleter(commands, ignore_case=True)

while True:
    user_input = prompt(">>> ", completer=completer)
    print(f"You entered: {user_input}")
