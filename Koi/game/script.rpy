# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "My name is Y/N!"

    e "I live in Tokyo and have the sweetest girlfriend. Her name is Ai."

    e "I cherish her with all my heart."

    e "Though, Ai doesn’t live in Tokyo with me. In fact, I only see her once a month. :("

    e "Ai was amazing and surprised me with a robot version of herself!"

    e "Now I’ll always have her with me ❤️"

    e "My life is going to be great."

    # This ends the game.

    return
