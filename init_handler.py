"""
socket_file_transfer/init_handler.py
Main script for initiated env.
"""
import os


class InitEnv:
    def __init__(self):
        pass

    @staticmethod
    def init_env():
        for dirs in ["send", "receive"]:
            try:
                os.mkdir(dirs)
                with open(f"{dirs}/test.txt", "w") as f:
                    f.write("This is a placeholder test document !")
            except FileExistsError:
                pass
