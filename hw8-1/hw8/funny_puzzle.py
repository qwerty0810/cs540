import heapq




def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0
    for i in range(len(from_state)):
        if from_state[i] != 0:
            row_from = i // 3
            col_from = i % 3
            idx_to = to_state.index(from_state[i])
            row_to = idx_to // 3
            col_to = idx_to % 3
            distance += abs(row_from - row_to) + abs(col_from - col_to)
    return distance




def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    
    empty_tile_index_1 = state.index(0)
    empty_tile_index_2 = state.index(0, empty_tile_index_1 + 1)
    empty_tile_1_row, empty_tile_1_col = divmod(empty_tile_index_1, 3)
    empty_tile_2_row, empty_tile_2_col = divmod(empty_tile_index_2, 3)
    successors = []
    for index, tile in enumerate(state):
        if tile != 0:
            tile_row, tile_col = divmod(index, 3)
            if ((empty_tile_1_row - 1 == tile_row or tile_row == empty_tile_1_row + 1) and (empty_tile_1_col == tile_col)) \
            or ((empty_tile_1_col - 1 == tile_col or tile_col == empty_tile_1_col + 1) and (empty_tile_1_row == tile_row)):
                new_state = state.copy()
                new_state[index] = 0
                new_state[empty_tile_index_1] = tile
                successors.append(new_state)
            if ((empty_tile_2_row - 1 == tile_row or tile_row == empty_tile_2_row + 1) and (empty_tile_2_col == tile_col)) \
            or ((empty_tile_2_col - 1 == tile_col or tile_col == empty_tile_2_col + 1) and (empty_tile_2_row == tile_row)):
                new_state = state.copy()
                new_state[index] = 0
                new_state[empty_tile_index_2] = tile
                successors.append(new_state)
    return sorted(successors)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    def reconstruct_path(state_tracker):
        path = []
        index = len(state_tracker) - 1

        while index != 0:
            path.append(state_tracker[index])
            index = state_tracker[index][2][2]

        path.append(state_tracker[0])

        return path

    open_list = []
    closed_list = []
    state_tracker = []
    max_queue_length = 0

    initial_state = (get_manhattan_distance(state), state, (0, get_manhattan_distance(state), -1))
    heapq.heappush(open_list, initial_state)

    while open_list:
        max_queue_length = max(len(open_list), max_queue_length)
        current_state = heapq.heappop(open_list)

        closed_list.append(current_state[1])
        state_tracker.append(current_state)

        if get_manhattan_distance(current_state[1]) == 0:
            path = reconstruct_path(state_tracker)

            for idx, step in enumerate(reversed(path)):
                print(f"{step[1]} h={step[2][1]} moves: {idx}")

            print(f"Max queue length: {max_queue_length}")
            return

        successors = get_succ(current_state[1])

        for successor in successors:
            successor = [int(i) for i in successor]
            if successor not in closed_list:
                dist = get_manhattan_distance(successor)
                new_state = (current_state[2][0] + dist + 1, successor, (current_state[2][0] + 1, dist, state_tracker.index(current_state)))
                heapq.heappush(open_list, new_state)

        max_queue_length = max(len(open_list), max_queue_length)

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()

    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([2,5,1,4,0,6,7,0,3])
    print()
