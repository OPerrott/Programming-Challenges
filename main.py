import os


class Run:
    def __init__(SELF):
        SELF.RUNNING = True
        SELF.CURR_DIR = os.path.dirname(os.path.realpath(__file__))
        SELF.TERMINAL()

    def TERMINAL(SELF):
        while SELF.RUNNING:
            SELF.CMD = input(f"{SELF.CURR_DIR}> ")
            SELF.VALIDATE_CMD()

    def VALIDATE_CMD(SELF):
        SPLIT_CMD = SELF.CMD.strip().split()
        if not SPLIT_CMD:
            return

        if SPLIT_CMD[0] == "cd":
            CD(SELF, SPLIT_CMD).VALIDATE_CD()
        elif SPLIT_CMD[0] == "dir":
            DIR(SELF).LIST_DIR()
        elif SPLIT_CMD[0] == "exit":
            SELF.RUNNING = False
        else:
            print(f"Command not recognized: {SPLIT_CMD[0]}")


class CD:
    def __init__(SELF, RUN_INSTANCE, CMD_SPLIT):
        SELF.RUN_INSTANCE = RUN_INSTANCE
        SELF.CMD_SPLIT = CMD_SPLIT

    def VALIDATE_CD(SELF):
        if len(SELF.CMD_SPLIT) == 1:
            SELF.RETURN_CURRENT_DIR()
        else:
            SELF.CHANGE_DIR(SELF.CMD_SPLIT[1])

    def RETURN_CURRENT_DIR(SELF):
        print(f"{SELF.RUN_INSTANCE.CURR_DIR}\n")

    def CHANGE_DIR(SELF, new_dir):
        new_path = os.path.join(SELF.RUN_INSTANCE.CURR_DIR, new_dir)
        if os.path.isdir(new_path):
            SELF.RUN_INSTANCE.CURR_DIR = os.path.abspath(new_path)
        else:
            print(f"No such directory: {new_dir}")


class DIR:
    def __init__(SELF, RUN_INSTANCE):
        SELF.RUN_INSTANCE = RUN_INSTANCE

    def LIST_DIR(SELF):
        try:
            items = os.listdir(SELF.RUN_INSTANCE.CURR_DIR)
            for item in items:
                full_path = os.path.join(SELF.RUN_INSTANCE.CURR_DIR, item)
                if os.path.isdir(full_path):
                    print(f"[DIR]  {item}")
                else:
                    print(f"       {item}")
            print()
        except Exception as error:
            print(f"Error reading directory: {error}")


if __name__ == '__main__':
    os.system("cls" if os.name == "nt" else "clear")
    Run()
