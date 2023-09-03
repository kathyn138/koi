# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define pov = Character("[povname]")

# The game starts here.

label start:
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Deez nuts"

    pov "My name is [povname]!"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "My name is Y/N!"

    "I live in Tokyo and have the sweetest girlfriend. Her name is Ai."

    "I cherish her with all my heart."

    "Though, Ai doesn’t live in Tokyo with me. In fact, I only see her once a month. :("

    "Ai was amazing and surprised me with a robot version of herself!"

    "Now I’ll always have her with me ❤️"

    "My life is going to be great."

    # This ends the game.

    return
