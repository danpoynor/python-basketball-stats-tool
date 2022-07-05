# Python Basketball Stats Tool

Demo console-based basketball team statistics app that divides a group of players into teams and presents statistics about each team.

Features

- Uses various Python data types to store and manipulate data into organized team structures.
- Cleans data from `constants.py` without changing the original data.
   - Converts string data into integers or floats.
   - Converts string data into Boolean values.
   - Converts string data into lists of strings.
- Organizes player data evenly into teams ensuring each team has the same number of experienced and inexperienced players.
- Provides Dunder Main usage examples in `app.py` entry point and `dm.py` module.
- Presents data in a nice readable format using extra spaces and line breaks ('\n') to break up lines.
- User is re-prompted with the main menu until they decide to "Quit the program".

## Run the app

```bash
python3 app.py
```

NOTE: Python 3.10 was used to develop and test this app.

---

## Run Unit Tests

Some basic unit tests are included to test the `dm.py` module.

<details>
  <summary>Expand/Collapse</summary>
To run the tests, use something like:


```bash
python3 -m unittest -v dm.py
```

and you should see some test result output like this:

```bash
test_balance_teams (dm.Tests) ... ok
test_calculate_avg_height (dm.Tests) ... ok
test_cleaned_players (dm.Tests) ... ok
test_create_string_from_list_of_lists (dm.Tests) ... ok
test_show_menu_options (dm.ToDoTests) ... skipped "TODO: When there's more time, test this"
test_show_team_stats (dm.ToDoTests) ... skipped "TODO: When there's more time, test this"

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK (skipped=2)
```

Note: If you run `dm.py` directly, with something like:

```bash
python3 dm.py
```

You should see test result output like this:

```bash
....ss
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK (skipped=2)
```

The `....ss` indicates four tests ran and two were skipped.

</details>

---

## Screenshot Showing Example Program States

<details>
  <summary>Expand/Collapse</summary>
  
<img width="499" alt="Screen Shot 2022-07-05 at 11 06 45 AM" src="https://user-images.githubusercontent.com/764270/177370712-ce5c170e-6bd6-49e5-886f-2a4d2dad86d4.png">

</details>
