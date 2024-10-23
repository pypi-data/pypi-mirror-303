import os
import sys
import getpass
import mutagen
from mutagen.wave import WAVE
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from time import sleep as wait
from .faded_altcolor import colored_text, leaked_text, reset
import msvcrt

# Class to manage notification suppression
class NotificationManager:
    """A class-based approach to suppress and restore notifications."""
    
    def __init__(self):
        self._original_stdout = sys.stdout

    def hide(self):
        """Suppress notifications by redirecting stdout to null."""
        sys.stdout = open(os.devnull, 'w')

    def restore(self):
        """Restore stdout to its original state."""
        sys.stdout.close()
        sys.stdout = self._original_stdout

# Clear console
def clear():
    """Clears the console of any text. Works on Windows, Linux, macOS, etc."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Cross-platform password input
def get_password(prompt="Enter your password: "):
    """Cross-platform password input hiding."""
    return getpass.getpass(prompt)

# Hide typed input with customizable hide character
def hide_input(prompt="", hide_char="*"):
    """Hide input with the specified hide_char (default '*'). Works cross-platform."""
    print(prompt, end='', flush=True)
    response = ''
    while True:
        if os.name == 'nt':
            char = msvcrt.getch().decode('utf-8')
        else:
            # For non-Windows systems, you would need to handle getch differently
            # This is a placeholder to represent an alternative method for Unix-based systems
            char = sys.stdin.read(1)
            
        if char == '\r':  # Enter key pressed
            print()
            break
        elif char == '\x08':  # Backspace key pressed
            if len(response) > 0:
                response = response[:-1]
                print('\b \b', end='', flush=True)  # Erase last character
        else:
            response += char
            print(hide_char, end='', flush=True)  # Print hide_char instead of the typed character
    return response

# Get audio length with support for multiple formats
def get_audio_length(file_path):
    """Retrieve the length of an audio file (supports WAV, MP3, FLAC)."""
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.wav':
            audio = WAVE(file_path)
        elif ext == '.mp3':
            audio = MP3(file_path)
        elif ext == '.flac':
            audio = FLAC(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
        return audio.info.length
    except mutagen.MutagenError as e:
        print(f"Error retrieving audio length: {e}")
        return None

# Custom exit with delay and colored message
def exit_app(msg="Thanks for using the application!", delay=2):
    """Exit the application with a customizable message and delay (in seconds)."""
    wait(delay)
    print(colored_text("GREEN", msg))
    wait(delay)
    sys.exit()

# Notify the user that they are using FancyUtil
print(colored_text("BLUE", "\n\nThanks for using FancyUtil! Consider using our other products at 'https://tairerullc.vercel.app'\n\n"))
