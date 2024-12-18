def solve_puzzle(Board, Source, Destination):
    """
    Function to find the shortest path on a given board. Uses BFS to find the shortest path.
    :param Board: Puzzle board to navigate through. Consists of a 2D array filled with either '-' or '#'. '-' indicates
    the space is passable and '#' indicates the space is impassable.
    :param Source: Starting coordinates in the form of a tuple.
    :param Destination: Ending coordinates in the form of a tuple.
    :return: A tuple with a list of coordinates that make up the shortest path and a string indicating the directions
    needed to move from one space to another on the shortest path.
    """
    # Check if source and destination are the same
    if Source == Destination:
        return [Source]

    # Initialize 2d array with spaces from Board. Includes distance (infinity, parent, row, and column)
    board_spaces = []
    row_num = 0
    column_num = 0
    for row in Board:
        board_spaces.append([])
        column_num = 0
        for space in row:
            # distance, parent, row, column
            board_spaces[row_num].append([float('infinity'), None, row_num, column_num])
            column_num += 1
        row_num += 1

    # Set source tuple distance = 0
    board_spaces[Source[0]][Source[1]][0] = 0

    # Create visited array
    visited = []
    visited.append(board_spaces[Source[0]][Source[1]])

    # Create list of directionals (up, down, left, and right)
    move_row = [0, 0, -1, 1]
    move_column = [1, -1, 0, 0]

    found_space = False
    path = [Destination]
    directions = ''

    # while length of queue is valid
    while len(visited) > 0:
        # pop min distance node
        current_node = visited.pop(0)
        distance = current_node[0]
        row = current_node[2]
        column = current_node[3]

        # for neighboring nodes
        for direction in range(len(move_row)):
            # Calculate potential node to move to
            new_row = row + move_row[direction]
            new_column = column + move_column[direction]

            # Check if new node coordinates are valid
            if new_row < 0 or new_row >= len(Board) or new_column < 0 or new_column >= len(Board[new_row]):
                continue
            # Check if neighboring space is passable
            elif Board[new_row][new_column] == '#':
                continue
            else:
                # Calculate distance to neighboring node
                new_distance = distance + 1

                # Check if new distance is less than previous distance
                if new_distance < board_spaces[new_row][new_column][0]:
                    # Update board_spaces array
                    board_spaces[new_row][new_column][0] = new_distance
                    board_spaces[new_row][new_column][1] = (row, column)

                    # Push node onto visited heap
                    visited.append(board_spaces[new_row][new_column])

        # Check if target node has been reached
        if current_node == board_spaces[Destination[0]][Destination[1]]:
            found_space = True

    # Check if Destination was found
    if found_space:
        node = Destination
        parent = board_spaces[Destination[0]][Destination[1]][1]

        # Loop backwards through each node's parent to find path and directions
        while parent is not None:
            # Add parent coordinates to path
            path.insert(0, parent)

            # Find directions
            if node[0] < parent[0]:
                directions = 'U' + directions
            elif node[0] > parent[0]:
                directions = 'D' + directions
            elif node[1] < parent[1]:
                directions = 'L' + directions
            elif node[1] > parent[1]:
                directions = 'R' + directions

            # Update node and parent variables
            node = parent
            parent = board_spaces[parent[0]][parent[1]][1]

        return path, directions
    else:
        return None

# puzz1 = [
#     ['-', '-', '-', '-', '-'],
#     ['-', '-', '#', '-', '-'],
#     ['-', '-', '-', '-', '-'],
#     ['#', '-', '#', '#', '-'],
#     ['-', '#', '-', '-', '-']
# ]
# puzz2 = [
#     ['-', '-', '-'],
#     ['-', '#', '-'],
#     ['-', '-', '-']
# ]
# print(solve_puzzle(puzz1, (0, 2), (2, 2)))
