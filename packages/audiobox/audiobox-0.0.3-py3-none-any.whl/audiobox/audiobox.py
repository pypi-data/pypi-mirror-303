# Import statements
import os
import sys
import shutil
from threading import Thread
from time import sleep as wait
import pygame
from altcolor import colored_text

# Redirect stdout to suppress pygame messages
old_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')

pygame.mixer.init()

sys.stdout.close()
sys.stdout = old_stdout

# Global variables
music_on = False
music_file = None
current_dir = os.path.dirname(__file__)

# Credits
def show_credits():
    """Display credits and license information."""
    print(colored_text("BLUE", "\n\nThanks for using AudioBox! Check out our other products at 'https://tairerullc.vercel.app'"))
    print(colored_text("MAGENTA", "\n\nNote:\nThe music, not the sfx, is by Sadie Jean. The song is called 'Locksmith' and is available via Spotify."
                         "\nPlease note this song is copyrighted material, and we use it only as an example. "
                         "We are not endorsed by them, nor are they endorsed by us.\n\n"))

show_credits()

# Functions
def generate_example_files():
    """Generates two example audio clips for use."""
    example_sfx = os.path.join(current_dir, "example_sfx.wav")
    example_music = os.path.join(current_dir, "example_music.mp3")

    # Set the location of clones
    cloned_sfx = "example_sfx.wav"
    cloned_music = "example_music.mp3"

    # Copy the example files
    try:
        shutil.copyfile(example_sfx, cloned_sfx)
        shutil.copyfile(example_music, cloned_music)
    except FileNotFoundError as e:
        print(f"Error: {e}. Example files not found.")

def sfx(filename, times=1):
    """Plays a sound effect."""
    def play_sound_effect():
        filepath = find_audio_file(filename)
        try:
            sound_effect = pygame.mixer.Sound(filepath)
            pygame.mixer.music.set_volume(0.5)
            sound_effect.play(times - 1)
            wait(1)  # Allow time for the sound to play
            pygame.mixer.music.set_volume(1)  # Reset volume
        except pygame.error as e:
            print(f"Error playing sound effect: {e}")

    # Play sound effects in a separate thread to prevent blocking
    sound_thread = Thread(target=play_sound_effect)
    sound_thread.start()

def play_music(filename, stop_other=False):
    """Plays music in the background, stopping other music if specified."""
    global music_file

    if not music_on:
        return

    filepath = find_audio_file(filename)

    if pygame.mixer.music.get_busy() and music_file == filepath:
        return  # Music already playing, no need to restart

    def play_and_wait():
        try:
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            # Wait for the song to finish (if music is still on)
            while pygame.mixer.music.get_busy():
                wait(1)  # Check every second
            if music_on:
                music_file = filepath
        except pygame.error as e:
            print(f"Error loading or playing music file: {e}")

    if stop_other:
        pygame.mixer.music.stop()

    # Play music in a separate thread to prevent blocking
    music_thread = Thread(target=play_and_wait)
    music_thread.start()

def find_audio_file(filename):
    """Helper function to locate a .wav or .mp3 file."""
    if os.path.isfile(f"{filename}.wav"):
        return f"{filename}.wav"
    elif os.path.isfile(f"{filename}.mp3"):
        return f"{filename}.mp3"
    else:
        raise FileNotFoundError(f"File {filename}.wav or {filename}.mp3 not found.")
