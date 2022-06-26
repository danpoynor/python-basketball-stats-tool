"""
Basketball Stats Tool
---------------------
"""

import copy
import dm
from constants import PLAYERS
from constants import TEAMS


def main():
    """This is the main entry point of the program."""
    try:
        dm.main(copy.deepcopy(PLAYERS), TEAMS)
    except ModuleNotFoundError:
        print("Data module constants.py missing")


if __name__ == "__main__":
    main()
