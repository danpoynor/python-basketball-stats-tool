"""Basketball Team Stats Tool Module."""
import os
import sys
import string
import pprint
_balanced_teams = {}


def calculate_avg_height(*args):
    """
    Calculate the average height of all players in a team.

    This function unpacks args (players) into a 'height' list,
    then sums the values and returns the rounded average.
    """
    total_height = sum(player["height"] for player in args)

    # In case during development I edited the data file
    # the total height could be 0.
    try:
        heights = round(total_height / len(args), 2)
        return heights
    except ZeroDivisionError:
        print("\nNo players found in the team.\n")
        return 0


def create_string_from_list_of_lists(list_of_lists):
    """
    Create a string of comma separated values from a list of lists.

    Example: create_string_from_list_of_lists([[1, 2, 3], [4, 5, 6]])
    Returns: "1, 2, 3, 4, 5, 6"
    """
    return ", ".join([", ".join(item) for item in list_of_lists])


def clean_players(data):
    """Clean the data for use in the program.

    Data to be cleaned:
    Height: Should be saved as an integer.
    Experience: Should be a boolean value (True or False).
    Guardians: Should be a List of strings for each player with 'and' removed.

    Returns a List with nested Dictionaries
    """
    cleaned = []

    for item in data:
        fixed = {
            "name": item["name"],
            "guardians": item["guardians"].split(" and "),
            "height": int(item["height"].split(" ")[0]),
            # Using 'tupled ternary technique' to convert experience to boolean
            # https://book.pythontips.com/en/latest/ternary_operators.html
            "experience": (False, True)[item["experience"] == "YES"]}

        cleaned.append(fixed)

    return cleaned


def balance_teams(teams, cleaned_players):
    """Ensure each team has an equal number of players.

    Split players into experienced and inexperienced players.
    Check each list has the same number of players.
    Add equal number of each type of player to each team.
    """
    # Create initial balanced_teams dictionary with just the team name and
    # an empty list for players.
    for team in teams:
        _balanced_teams[team] = []

    # Create a list of experienced and inexperienced players.
    players_trained = [
        player for player in cleaned_players if player["experience"]]
    players_untrained = [
        player for player in cleaned_players if not player["experience"]
    ]

    # Sanity check to ensure each list has an equal number of players
    if not len(players_trained) == len(players_untrained):
        print(
            "\nERROR: Number of players trained and untrained are not equal."
            f"\n Experienced players: ({len(players_trained)})"
            f"\n Inexperienced players: ({len(players_untrained)})"
            "\n Please check the data and try again.\n")
        sys.exit("Program exited successfully.")

    # Loop through the lists of experienced and inexperienced players
    # and add them to each team. Popping them off the list each time
    # it's added to a team reduces the lists till they're both empty.
    while players_trained and players_untrained:
        for team_name in teams:
            _balanced_teams[team_name].append(players_trained.pop())
            _balanced_teams[team_name].append(players_untrained.pop())

    return _balanced_teams


def show_menu_options(options):
    """Show a list of options.

    Args:
        # options (list): List of options to show in menu format.
    """
    menu_dict = dict(zip(string.ascii_uppercase, options))
    print()
    for key, value in menu_dict.items():
        print(f" {key}) {value}")


def menu_teams(msg=None):
    """Show a list of teams and prompt user for input.

    Convert a letter returned as 'selected_option' into an integer to use
    as an index for accessing the selected team in the teams list before
    displaying the team's stats.
    """
    # devtime(_balanced_teams)
    team_keys = tuple(_balanced_teams.keys())
    show_menu_options(team_keys)
    print([msg, ''][msg is None])
    selected_option = input("Enter an option: ")

    # Test if selected_option is an alpha character within range
    # NOTE: The selected_option is converted to an integer using ord() to use
    # as an index indicating which team in the team_index to show stats for.
    # ord() conversion example:
    # If team is 'a', the index will be 0 (97 - 97 = 0)
    # If team is 'b', the index will be 1 (98 - 97 = 1)
    # REF: https://docs.python.org/3/library/functions.html#ord
    # REF: https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin
    # Notice decimal value for 'Latin Small Letter A' is 97.
    if selected_option.isalpha() and (ord(selected_option.lower()) - 97) in range(len(team_keys)):
        show_team_stats(team_keys[ord(selected_option.lower()) - 97])
        input("\nPress ENTER to continue...")
        menu_main()
    else:
        menu_teams(f"\n'{selected_option}' is invalid. Enter a menu option.")


def menu_main(msg=None):
    """Show a list of options and prompt user for input."""
    # Clear screen each time main menu is shown
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BASKETBALL TEAM STATS TOOL")
    print("\n---- MENU----")
    print("\nHere are your choices:")

    # NOTE: I'm packing a Tuple for store _main_menu_options because the order
    # matters. If this were a List or Set, the order would be random since
    # they're mutable.
    show_menu_options(("List all teams", "Quit the program"))
    print([msg, ''][msg is None])
    selected_option = input("Enter an option: ")

    if selected_option.lower() == "a":
        menu_teams()
    elif selected_option.lower() == "b":
        os.system("clear")
        print("\nBye :)\n")
        sys.exit("Program exited successfully.")
    else:
        menu_main(
            f"\n'{selected_option}' is invalid. Enter a menu option.")


def show_team_stats(team_key):
    """Show stats for a team.

    Args:
        team_key (str): Key value of the team in the _balanced_teams dictionary
    """
    team = _balanced_teams[team_key]
    players_names = [player["name"] for player in team]
    players_guardians = [player["guardians"] for player in team]
    players_trained = [player for player in team if player["experience"]]
    players_untrained = [player for player in team if not player["experience"]]

    print(f"\nTeam: {team_key} Stats")
    print("--------------------")
    print(f"Total players: {len(team)}")
    print(f"Total experienced: {len(players_trained)}")
    print(f"Total inexperienced: {len(players_untrained)}")
    print(f"Average height: {calculate_avg_height(*team)}")
    print(f"\nPlayers on Team:\n {', '.join(players_names)}")
    print(
        f"\nGuardians:\n {create_string_from_list_of_lists(players_guardians)}")

    # Show lists of experienced/inexperienced player dictionaries if needed
    # print("\nExperienced Players:")
    # print(*players_trained, sep=',\n')
    # print("\nInexperienced Players:")
    # print(*players_untrained, sep=',\n')


def main(players, teams):
    """Start the application.

    Args:
        PLAYERS (list): List of player objects.
        TEAMS (list): List of team data.
    """
    _balanced_teams = balance_teams(teams, clean_players(players))
    menu_main()


def devtime(data):
    """
    Pretty print data to check for anomalies. For use only during development.

    Example: devtime(_balanced_teams)
    """
    pp = pprint.PrettyPrinter(indent=1, compact=True, width=160)
    print("=" * 79)
    pp.pprint(data)
    print("=" * 79)
