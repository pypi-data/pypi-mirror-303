"""Module providing a function printing python version."""

import signal
import sys
import time

from plutonkit.command.action.help import Help
from plutonkit.config.command import ACTIONS
from plutonkit.config.message import INTRODUCTION

# noqa: Our signal handler


def signal_handler():
    print("\nInvalid control +key or press control+z to exit")
    print("\nPlease try to select appropriate key selection")


def exit_handler():
    print("\nExiting....")
    sys.exit(0)


def autoload():

    signal.signal(signal.SIGINT, signal_handler)

    # noqa: Register the exit handler with `SIGTSTP` (Ctrl + Z)
    signal.signal(signal.SIGTSTP, exit_handler)

    print(f"{INTRODUCTION}\n")
    try:
        while 1:
            ACTIONS["help"] = Help(sys.argv)
            ACTIONS[str(sys.argv[1])].execute()
            time.sleep(30)

    except Exception:
        print("Invalid argument, please type `help` to see available command")


def load_command():

    signal.signal(signal.SIGINT, signal_handler)

    # noqa: Register the exit handler with `SIGTSTP` (Ctrl + Z)
    signal.signal(signal.SIGTSTP, exit_handler)

    print(f"{INTRODUCTION}\n")
    try:
        while 1:
            ACTIONS["cmd"].modify_argv_index(1).execute()
            time.sleep(30)
    except Exception:
        print("Invalid command request")
