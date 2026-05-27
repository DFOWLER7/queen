import random

BOARD_SIZE = 8


def generate_random_state():
    """
    Creates a random board state.
    Each index represents a column.
    Each value represents the row where the queen is placed in that column.
    Example: [0, 4, 7, 5, 2, 6, 1, 3]
    """
    return [random.randint(0, BOARD_SIZE - 1) for _ in range(BOARD_SIZE)]


def calculate_heuristic(state):
    """
    Heuristic = number of pairs of queens attacking each other.
    Lower is better.
    Goal state has h = 0.
    """
    conflicts = 0

    for col1 in range(BOARD_SIZE):
        for col2 in range(col1 + 1, BOARD_SIZE):
            row1 = state[col1]
            row2 = state[col2]

            same_row = row1 == row2
            same_diagonal = abs(row1 - row2) == abs(col1 - col2)

            if same_row or same_diagonal:
                conflicts += 1

    return conflicts


def print_board(state):
    """
    Prints the board using 0s and 1s.
    1 = queen
    0 = empty square
    """
    print("Current State")

    for row in range(BOARD_SIZE):
        row_values = []

        for col in range(BOARD_SIZE):
            if state[col] == row:
                row_values.append("1")
            else:
                row_values.append("0")

        print(",".join(row_values))

    print()


def get_neighbors(state):
    """
    Generates all possible neighboring states by moving one queen
    within its column to a different row.
    """
    neighbors = []

    for col in range(BOARD_SIZE):
        original_row = state[col]

        for new_row in range(BOARD_SIZE):
            if new_row != original_row:
                new_state = state.copy()
                new_state[col] = new_row
                neighbors.append(new_state)

    return neighbors


def get_best_neighbor(state):
    """
    Finds the best neighboring state.
    Returns:
    - best_neighbor
    - best_neighbor_heuristic
    - number of neighbors with lower heuristic
    """
    current_h = calculate_heuristic(state)
    neighbors = get_neighbors(state)

    best_neighbor = None
    best_h = current_h
    lower_h_neighbors = 0

    for neighbor in neighbors:
        neighbor_h = calculate_heuristic(neighbor)

        if neighbor_h < current_h:
            lower_h_neighbors += 1

        if neighbor_h < best_h:
            best_h = neighbor_h
            best_neighbor = neighbor

    return best_neighbor, best_h, lower_h_neighbors


def solve_8_queens():
    restarts = 0
    state_changes = 0

    current_state = generate_random_state()

    while True:
        current_h = calculate_heuristic(current_state)

        print(f"Current h: {current_h}")
        print_board(current_state)

        if current_h == 0:
            print("Solution Found!")
            print(f"State changes: {state_changes}")
            print(f"Restarts: {restarts}")
            break

        best_neighbor, best_h, lower_h_neighbors = get_best_neighbor(current_state)

        print(f"Neighbors found with lower h: {lower_h_neighbors}")

        if lower_h_neighbors == 0:
            print("RESTART")
            print()
            current_state = generate_random_state()
            restarts += 1
            state_changes += 1
        else:
            print("Setting new current state")
            print()
            current_state = best_neighbor
            state_changes += 1


if __name__ == "__main__":
    solve_8_queens()
