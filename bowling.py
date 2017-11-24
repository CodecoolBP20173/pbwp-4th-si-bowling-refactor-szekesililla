def score(game):
    """Gets a valid sequence of rolls for one line of American Ten-Pin Bowling and produces the total score for the game. 

    Args:
        game = string or list of chars. Valid values each char: numbers 1-9, "x", "/", "-"

    Returns:
        the total score (integer)
    """

    game = game.lower()
    result = 0
    in_first_half = True
    frame = 1
    MAX_FRAMES = 10   

    for i in range(len(game)):
        # calculates the score of the roll
        result += get_value(game[i])
        if game[i] == '/':
            result += - get_value(game[i-1])
        if frame < MAX_FRAMES and game[i] in ['x', '/']:
            result += get_value(game[i+1])
            if game[i] == 'x':
                result += get_value(game[i+2])
                if game[i+2] == '/':
                    result -= get_value(game[i+1])

        # checks the frame's number
        if not in_first_half or game[i] == 'x':
            frame += 1
            in_first_half = True
        else:
            in_first_half = False

    return result


def get_value(char):
    """Gets the character, whih indicates the roll and returns .

    Args:
        char

    Returns:
        the score of the roll (integer)
    """
    if char >= '1' and char <= '9':
        return int(char)
    elif char in ['x', '/']:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
