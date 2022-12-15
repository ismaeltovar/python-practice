"""Useful Console functions"""
import os
from platform import system

def clear():
    """Clear the console."""
    if system() == "Windows":
        os.system("cls")
    elif system() == "Linux":
        os.system("clear")


def enter_pmt():
    """Prompt user to Enter in order to continue."""
    print('')
    print("Press ENTER to continue:", end='')
    input()
