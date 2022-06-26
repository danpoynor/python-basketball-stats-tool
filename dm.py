"""Basketball Team Stats Tool Module."""
import os
import sys
import string
_balanced_teams = {}


def calculate_avg_height(*args):
    total_height = sum(player["height"] for player in args)
    return round(total_height / len(args), 2)


def create_string_from_list_of_lists(list_of_lists):
    return ", ".join([", ".join(item) for item in list_of_lists])


def clean_players(data):
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
    menu_dict = dict(zip(string.ascii_uppercase, options))
    print()
    for key, value in menu_dict.items():
        print(f" {key}) {value}")


def menu_teams(msg=None):
    team_keys = tuple(_balanced_teams.keys())
    show_menu_options(team_keys)
    print([msg, ''][msg is None])
    selected_option = input("Enter an option: ")

    # Test if selected_option is an alpha character within range
    if selected_option.isalpha() and (ord(selected_option.lower()) - 97) in range(len(team_keys)):
        show_team_stats(team_keys[ord(selected_option.lower()) - 97])
        input("\nPress ENTER to continue...")
        menu_main()
    else:
        menu_teams(f"\n'{selected_option}' is invalid. Enter a menu option.")


def menu_main(msg=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BASKETBALL TEAM STATS TOOL")
    print("\n---- MENU----")
    print("\nHere are your choices:")

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


def main(players, teams):
    _balanced_teams = balance_teams(teams, clean_players(players))
    menu_main()
