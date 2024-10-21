"""
A collection of predefined functions to set the text colour and style in the terminal.
"""

def black(message: str):
    """
    Set the text colour to black.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text colour set to black.
    
    """
    return f"\033[30m{message}\033[0m"

def bright_magenta(message: str):
    """
    Set the text colour to bright magenta.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text colour set to bright magenta.
    
    """
    return f"\033[95m{message}\033[0m"

def bright_blue(message: str):
    """
    Set the text colour to bright blue.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text colour set to bright blue.
    
    """
    return f"\033[94m{message}\033[0m"

def bright_green(message: str):
    """
    Set the text colour to bright green.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text colour set to bright green.
    
    """
    return f"\033[92m{message}\033[0m"

def bright_yellow(message: str):
    """
    Set the text colour to bright yellow.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text colour set to bright yellow.
    
    """
    return f"\033[93m{message}\033[0m"

def bright_red(message: str):
    """
    Set the text colour to bright red.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text colour set to bright red.
    
    """
    return f"\033[91m{message}\033[0m"

def red(message: str):
    """
    Set the text colour to red.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text colour set to red.
    
    """
    return f"\033[31m{message}\033[0m"

def italic(message: str):
    """
    Set the text style to italic.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text style set to italic.
    
    """
    return f"\033[3m{message}\033[0m"

def underline(message: str):
    """
    Set the text style to underline.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text style set to underline.
    
    """
    return f"\033[4m{message}\033[0m"

def bold(message: str):
    """
    Set the text style to bold.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text style set to bold.
    
    """
    return f"\033[1m{message}\033[0m"

def dimmed(message: str):
    """
    Set the text style to dimmed.
    
    Args:
        message (str): The message to be displayed.

    Returns:
        str: The message with the text style set to dimmed.
    
    """
    return f"\033[2m{message}\033[0m"
