def letter_converter(start_space, end_space):
    """
    Function to convert user letter/number coordinates to (x, y) coordinates. Allows the coordinates to be run through
    Puzzle.py
    :param start_space: Starting space given by the user
    :param end_space: Ending space given by the user
    :return: Two touples, one containing the (x, y) coordinates for the starting position, and the other containing the
    (x, y) coordinates for the ending position
    """
    # Convert coordinate points to uppercase
    start_space = start_space.upper()
    end_space = end_space.upper()

    # Get co-ordinates for start position
    start_position = ()
    if start_space == 'A1':
        start_position = (0, 0)
    elif start_space == 'A2':
        start_position = (0, 1)
    elif start_space == 'A3':
        start_position = (0, 2)
    elif start_space == 'A4':
        start_position = (0, 3)
    elif start_space == 'A5':
        start_position = (0, 4)
    elif start_space == 'B1':
        start_position = (1, 0)
    elif start_space == 'B2':
        start_position = (1, 1)
    elif start_space == 'B4':
        start_position = (1, 3)
    elif start_space == 'B5':
        start_position = (1, 4)
    elif start_space == 'C1':
        start_position = (2, 0)
    elif start_space == 'C2':
        start_position = (2, 1)
    elif start_space == 'C3':
        start_position = (2, 2)
    elif start_space == 'C4':
        start_position = (2, 3)
    elif start_space == 'C5':
        start_position = (2, 4)
    elif start_space == 'D2':
        start_position = (3, 1)
    elif start_space == 'D5':
        start_position = (3, 4)
    elif start_space == 'E1':
        start_position = (4, 0)
    elif start_space == 'E3':
        start_position = (4, 2)
    elif start_space == 'E4':
        start_position = (4, 3)
    elif start_space == 'E5':
        start_position = (4, 4)
    else:
        start_position = (-1, -1)

    # Get coordinates for end position
    end_position = ()
    if end_space == 'A1':
        end_position = (0, 0)
    elif end_space == 'A2':
        end_position = (0, 1)
    elif end_space == 'A3':
        end_position = (0, 2)
    elif end_space == 'A4':
        end_position = (0, 3)
    elif end_space == 'A5':
        end_position = (0, 4)
    elif end_space == 'B1':
        end_position = (1, 0)
    elif end_space == 'B2':
        end_position = (1, 1)
    elif end_space == 'B4':
        end_position = (1, 3)
    elif end_space == 'B5':
        end_position = (1, 4)
    elif end_space == 'C1':
        end_position = (2, 0)
    elif end_space == 'C2':
        end_position = (2, 1)
    elif end_space == 'C3':
        end_position = (2, 2)
    elif end_space == 'C4':
        end_position = (2, 3)
    elif end_space == 'C5':
        end_position = (2, 4)
    elif end_space == 'D2':
        end_position = (3, 1)
    elif end_space == 'D5':
        end_position = (3, 4)
    elif end_space == 'E1':
        end_position = (4, 0)
    elif end_space == 'E3':
        end_position = (4, 2)
    elif end_space == 'E4':
        end_position = (4, 3)
    elif end_space == 'E5':
        end_position = (4, 4)
    else:
        end_position = (-1, -1)

    return start_position, end_position


def coordinate_converter(path):
    """
    Converts the (x, y) coordinates provided by Puzzle.py into letter/number coordinates.
    :param path: A list of (x, y) coordinates that make up the shortest path.
    :return: A list of letter/number coordinates meant for the user to read.
    """
    converted_path = []

    for coord in path:
        if coord == (0, 0):
            converted_path.append('A1')
        elif coord == (0, 1):
            converted_path.append('A2')
        elif coord == (0, 2):
            converted_path.append('A3')
        elif coord == (0, 3):
            converted_path.append('A4')
        elif coord == (0, 4):
            converted_path.append('A5')
        elif coord == (1, 0):
            converted_path.append('B1')
        elif coord == (1, 1):
            converted_path.append('B2')
        elif coord == (1, 3):
            converted_path.append('B4')
        elif coord == (1, 4):
            converted_path.append('B5')
        elif coord == (2, 0):
            converted_path.append('C1')
        elif coord == (2, 1):
            converted_path.append('C2')
        elif coord == (2, 2):
            converted_path.append('C3')
        elif coord == (2, 3):
            converted_path.append('C4')
        elif coord == (2, 4):
            converted_path.append('C5')
        elif coord == (3, 1):
            converted_path.append('D2')
        elif coord == (3, 4):
            converted_path.append('D5')
        elif coord == (4, 0):
            converted_path.append('E1')
        elif coord == (4, 2):
            converted_path.append('E3')
        elif coord == (4, 3):
            converted_path.append('E4')
        elif coord == (4, 4):
            converted_path.append('E5')

    return converted_path
