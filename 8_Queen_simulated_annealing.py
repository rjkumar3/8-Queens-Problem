import random
import math

def calculate_cost(board):
    """Calculate the number of conflicting pairs of queens."""
    try:
        cost = 0
        n = len(board)
        for i in range(n):
            for j in range(i + 1, n):
                if board[i] == board[j]:
                    cost += 1
                if abs(board[i] - board[j]) == abs(i - j):
                    cost += 1
        return cost
    except Exception as e:
        print(f"Error calculating cost: {e}")
        return float('inf')  # Return a very high cost in case of an error

def get_random_neighbour(board):
    """Generate a neighbouring solution by altering the position of one queen."""
    try:
        neighbour = board[:]
        i = random.randint(0, len(board) - 1)
        new_position = random.randint(0, len(board) - 1)
        neighbour[i] = new_position
        return neighbour
    except Exception as e:
        print(f"Error generating neighbour: {e}")
        return board  # Return the original board in case of an error

def simulated_annealing(board, temperature, cooling_rate):
    """Perform the Simulated Annealing algorithm."""
    try:
        current_board = board
        current_cost = calculate_cost(current_board)
        
        while temperature > 0 and current_cost != 0:
            new_board = get_random_neighbour(current_board)
            new_cost = calculate_cost(new_board)
            delta_cost = new_cost - current_cost
            
            if delta_cost < 0 or random.random() < math.exp(-delta_cost / temperature):
                current_board = new_board
                current_cost = new_cost
            
            temperature *= cooling_rate
        
        return current_board, current_cost
    except Exception as e:
        print(f"Error during simulated annealing: {e}")
        return board, calculate_cost(board)  # Return the current best board in case of an error

def print_board(board):
    """Print the chessboard with queens."""
    try:
        n = len(board)
        for i in range(n):
            row = ['.'] * n
            row[board[i]] = 'Q'
            print(' '.join(row))
        print()
    except Exception as e:
        print(f"Error printing board: {e}")

# Parameters
n = 8
initial_temperature = 10000
cooling_rate = 0.995

try:
    # Initialize board with a random configuration
    initial_board = [random.randint(0, n-1) for _ in range(n)]

    # Solve the 8-Queens problem using Simulated Annealing
    solution_board, solution_cost = simulated_annealing(initial_board, initial_temperature, cooling_rate)

    # Print the result
    print("Initial board configuration:")
    print_board(initial_board)
    print(f"Initial cost (number of conflicts): {calculate_cost(initial_board)}")

    print("Solution board configuration:")
    print_board(solution_board)
    print(f"Solution cost (number of conflicts): {solution_cost}")

except Exception as e:
    print(f"Error in main execution: {e}")
