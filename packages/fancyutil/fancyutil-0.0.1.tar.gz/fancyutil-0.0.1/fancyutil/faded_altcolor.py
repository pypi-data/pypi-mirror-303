from colorama import Style, Fore, Back

def reset():
    """Stolen from altcolor (do not worry, we made altcolor.)"""
    return Style.RESET_ALL

def Color(r, g, b):
    """Stolen from altcolor (do not worry, we made altcolor.)"""
    # Returns RGB ANSI escape code
    return f"\033[38;2;{r};{g};{b}m"

def colored_text(color, text, style="Fore"):
    """Stolen from altcolor (do not worry, we made altcolor.)"""
    style = style.capitalize()
    
    if style == "Fore":
        styles = {
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,
            "WHITE": Fore.WHITE,
            "LIGHTBLACK": Fore.LIGHTBLACK_EX,
            "LIGHTRED": Fore.LIGHTRED_EX,
            "LIGHTGREEN": Fore.LIGHTGREEN_EX,
            "LIGHTYELLOW": Fore.LIGHTYELLOW_EX,
            "LIGHTBLUE": Fore.LIGHTBLUE_EX,
            "LIGHTMAGENTA": Fore.LIGHTMAGENTA_EX,
            "LIGHTCYAN": Fore.LIGHTCYAN_EX,
            "LIGHTWHITE": Fore.LIGHTWHITE_EX,
        }
    elif style == "Back":
        styles = {
            "BLACK": Back.BLACK,
            "RED": Back.RED,
            "GREEN": Back.GREEN,
            "YELLOW": Back.YELLOW,
            "BLUE": Back.BLUE,
            "MAGENTA": Back.MAGENTA,
            "CYAN": Back.CYAN,
            "WHITE": Back.WHITE,
            "LIGHTBLACK": Back.LIGHTBLACK_EX,
            "LIGHTRED": Back.LIGHTRED_EX,
            "LIGHTGREEN": Back.LIGHTGREEN_EX,
            "LIGHTYELLOW": Back.LIGHTYELLOW_EX,
            "LIGHTBLUE": Back.LIGHTBLUE_EX,
            "LIGHTMAGENTA": Back.LIGHTMAGENTA_EX,
            "LIGHTCYAN": Back.LIGHTCYAN_EX,
            "LIGHTWHITE": Back.LIGHTWHITE_EX,
        }
    else:
        print(Fore.RED + "INVALID STYLE!" + Style.RESET_ALL)
        return

    # Check if the color is in the predefined styles
    if isinstance(color, str) and color.upper() in styles:
        return styles[color.upper()] + text + Style.RESET_ALL
    # Check if the color is in RGB format
    elif isinstance(color, tuple) and len(color) == 3:
        return Color(color[0], color[1], color[2]) + text + Style.RESET_ALL
    else:
        print(Fore.RED + "INVALID COLOR!" + Style.RESET_ALL)
        return

def leaked_text(color, text, style="Fore"):
    """Stolen from altcolor (do not worry, we made altcolor.)"""
    style = style.capitalize()
    
    if style == "Fore":
        styles = {
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,
            "WHITE": Fore.WHITE,
            "LIGHTBLACK": Fore.LIGHTBLACK_EX,
            "LIGHTRED": Fore.LIGHTRED_EX,
            "LIGHTGREEN": Fore.LIGHTGREEN_EX,
            "LIGHTYELLOW": Fore.LIGHTYELLOW_EX,
            "LIGHTBLUE": Fore.LIGHTBLUE_EX,
            "LIGHTMAGENTA": Fore.LIGHTMAGENTA_EX,
            "LIGHTCYAN": Fore.LIGHTCYAN_EX,
            "LIGHTWHITE": Fore.LIGHTWHITE_EX,
        }
    elif style == "Back":
        styles = {
            "BLACK": Back.BLACK,
            "RED": Back.RED,
            "GREEN": Back.GREEN,
            "YELLOW": Back.YELLOW,
            "BLUE": Back.BLUE,
            "MAGENTA": Back.MAGENTA,
            "CYAN": Back.CYAN,
            "WHITE": Back.WHITE,
            "LIGHTBLACK": Back.LIGHTBLACK_EX,
            "LIGHTRED": Back.LIGHTRED_EX,
            "LIGHTGREEN": Back.LIGHTGREEN_EX,
            "LIGHTYELLOW": Back.LIGHTYELLOW_EX,
            "LIGHTBLUE": Back.LIGHTBLUE_EX,
            "LIGHTMAGENTA": Back.LIGHTMAGENTA_EX,
            "LIGHTCYAN": Back.LIGHTCYAN_EX,
            "LIGHTWHITE": Back.LIGHTWHITE_EX,
        }
    else:
        print(Fore.RED + "INVALID STYLE!" + Style.RESET_ALL)
        return

    # Check if the color is in the predefined styles
    if isinstance(color, str) and color.upper() in styles:
        return styles[color.upper()] + text
    # Check if the color is in RGB format
    elif isinstance(color, tuple) and len(color) == 3:
        return Color(color[0], color[1], color[2]) + text
    else:
        print(Fore.RED + "INVALID COLOR!" + Style.RESET_ALL)
        return