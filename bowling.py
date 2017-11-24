def score(game):
    """Gets a valid sequence of rolls for one line of American Ten-Pin Bowling and produces the total score for the game. 

    Args:
        game = string or list of chars. Valid values each char: numbers 1-9, "x", "/", "-"

    Returns:
        the total score (integer)
    """

    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        # if not in_first_half:
            # frame += 1
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
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

