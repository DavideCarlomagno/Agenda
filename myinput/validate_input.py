from datetime import datetime, date

def int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    Prompts the user for an integer input, optionally constrained by a minimum and/or maximum value.

    Args:
        prompt (str): The message to display to the user.
        min_val (int, optional): Minimum acceptable value. Defaults to None.
        max_val (int, optional): Maximum acceptable value. Defaults to None.

    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        try:
            user_input = int(input(prompt)) #prendo l'input e tento di convertirlo in int --> se fallisce: ValueError

            if min_val is not None and user_input < min_val: 
                print(f"Value must be at least {min_val}. Try again.")
                continue

            if max_val is not None and user_input > max_val:
                print(f"Value must be at most {max_val}. Try Again.")
                continue

            return user_input
        
        except ValueError:
            print("It was not an int. Try again.")

def float_input(prompt: str, min_val: float = None, max_val: float = None) -> float:
    """
    Prompts the user for a float input, optionally constrained by a minimum and/or maximum value.

    Args:
        prompt (str): The message to display to the user.
        min_val (float, optional): Minimum acceptable value. Defaults to None.
        max_val (float, optional): Maximum acceptable value. Defaults to None.

    Returns:
        float: A valid float entered by the user.
    """
    while True:
        try:
            user_input = float(input(prompt)) #prendo l'input e tento di convertirlo in float --> se fallisce: ValueError

            if min_val is not None and user_input < min_val: 
                print(f"Value must be at least {min_val}. Try again.")
                continue

            if max_val is not None and user_input > max_val:
                print(f"Value must be at most {max_val}. Try Again.")
                continue

            return user_input
        
        except ValueError:
            print("It was not a float. Try again.")

def choice_input(prompt: str, choices: list[str], case_sensitive: bool = False) -> str:
    """
    Prompt the user to choose from a list of predefined options.

    Args:
        prompt (str): The message displayed to the user.
        choices (list[str]): A list of valid input options.
        case_sensitive (bool, optional): If True, enforces case-sensitive matching. Defaults to False.

    Returns:
        str: A valid choice selected by the user.
    """
    
    pass

def bool_input(prompt: str) -> bool:
    """
    Prompt the user for a boolean response (yes/no, true/false).

    Accepts inputs like "yes", "no", "y", "n", "true", "false" (case-insensitive).

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        bool: True for affirmative responses, False for negative responses.
    """
    while True:
        user_input = input(prompt).strip().lower()

        if user_input in ["yes", "y", "true"]:
            return True
        elif user_input in ["no", "n", "false"]:
            return False
        else:
            print("Input must be: \n 'y', 'yes' or 'true' for True value, \n 'n', 'no', 'false' for False value.")

def str_input(prompt: str, min_len: int = None, max_len: int = None, regex: str = None) -> str:
    """
    Prompt the user for a string input, with optional constraints.

    Args:
        prompt (str): The message displayed to the user.
        min_len (int, optional): Minimum length required. Defaults to None.
        max_len (int, optional): Maximum length allowed. Defaults to None.
        regex (str, optional): A regular expression that the input must match. Defaults to None.

    Returns:
        str: A validated string input from the user.
    """
    
    pass

def optional_input(prompt: str, base_validator: callable) -> any:
    """
    Prompt the user for optional input, allowing them to skip by pressing Enter.

    If input is provided, it is validated using the given validator function.

    Args:
        prompt (str): The message displayed to the user.
        base_validator (Callable): A function that validates the input.

    Returns:
        Any: None if skipped, or the validated result of the input.
    """
    
    pass

def date_input(prompt: str, onlyFuture: bool = False) -> datetime:
    """
    Prompts the user for a date, optionally conditioned to be a future day.

    Args:
        prompt (str): The message to display to the user.
        alsoGoneDays (bool, optional): If set True, forces the user to give a future or present day. Defaults to False.

    Returns:
        datetime: A valid date entered by the user.
    """

    while True:
        print("Accepted format: YYYY-MM-DD.")
        user_input = input(prompt).strip()
        try:
            user_input = datetime.strptime(user_input, "%Y-%m-%d").date()

            if onlyFuture and user_input < date.today():
                print("You must type a future or present date. Try again.")
                continue
        
            return user_input

        except ValueError:
            print("not a Valid date, try again.")