import sys

# Calculates the final score of the game based on the current state of marble piles    
def calculate_final_score(marbles_piles, depth):   
    return None if (marbles_piles[0] != 0 and marbles_piles[1] != 0 and (depth is None or depth > 0)) else (3 * marbles_piles[1]) - (2 * marbles_piles[0])
    
# Generates next moves given the current state of the marble piles 
def generate_next_moves(marbles_piles):
    red_blue_moves = []
    # If there are red marbles left, create a move by removing one red marble   
    if marbles_piles[0] > 0:
        red_blue_moves.append((marbles_piles[0] - 1, marbles_piles[1]))
    # If there are blue marbles left, create a move by removing one blue marble    
    if marbles_piles[1] > 0:
        red_blue_moves.append((marbles_piles[0], marbles_piles[1] - 1))
    return red_blue_moves

# Determines the best move for the computer player using the minimax algorithm with alpha-beta pruning
def eval_best_computer_move(marbles_piles, depth):
    _, optimal_move  = min_max_alpha_beta_pruning(marbles_piles, True, -float("inf"), float("inf"), None if depth is None else depth)
    return optimal_move 

#  Implements the Minimax algorithm with alpha-beta pruning to find the optimal move
def min_max_alpha_beta_pruning(marbles_piles, max_player, alpha, beta, depth):

    # Calculate the final score of the current state or check if the maximum depth is reached   
    result = calculate_final_score(marbles_piles, depth)
    
    # If terminal state or maximum depth is reached, return the score and no move        
    if result is not None or depth == 0:
        return result, None
        
    # Initialize the best_value based on whether it's a maximizing or minimizing player's turn 
    best_value = -float("inf") if max_player else float("inf")  
    optimal_move = None
    
    # Iterate through all possible moves generated from the current state    
    for next_move in generate_next_moves(marbles_piles):
        # Recursively explore the potential move to calculate its score
        potential_score, _ = min_max_alpha_beta_pruning(next_move , not max_player, alpha, beta, None if depth is None else depth - 1)                 
        
        # Update best_value and optimal_move based on maximizing or minimizing player's turn       
        if (not max_player and potential_score < best_value) or (max_player and potential_score > best_value):
            best_value = potential_score
            optimal_move = next_move
            beta = min(beta, potential_score) if not max_player else beta
            alpha = max(alpha, potential_score) if max_player else alpha
            
        # Perform alpha-beta pruning: if beta (minimizer's best value) <= alpha (maximizer's best value), break the loop          
        if beta <= alpha:
            break
    # Return the best calculated score and the corresponding optimal move
    return best_value, optimal_move 

# Determine the winner based on the game version and display the result  
def announce_winner(version, amt):
    if version == "misere":
        print(f"Computer wins with a score of {amt}")
    else:
        print(f"Human wins with a score of {amt}")


# Displays the current state of the marble piles and checks if the game is over.            
def display_and_check(marbles_piles, version, depth):

    # Display the number of marbles left in each pile
    print(f"Number of marbles left:- Red marbles = {marbles_piles[0]},marbles_piles Blue marbles = {marbles_piles[1]}")
    
    # Check if either of the marble piles is empty
    if marbles_piles[0] == 0 or marbles_piles[1] == 0:
        # Calculate the final score and announce the winner
        score = calculate_final_score(marbles_piles, depth)
        announce_winner(version, score)
        return True
    
    return False 




# Starting point
# Get marble count from cmd
red_marbles, blue_marbles= int(sys.argv[1]),int(sys.argv[2])

# storing red and blue marbles in marble piles
marbles_piles = (red_marbles, blue_marbles)

# Get game version
if len(sys.argv) < 4 or sys.argv[3].lower() != "misere":
    version = "standard"
else:
    version = "misere"

# Set first player as computer and depth value as none 
first_player = 'computer'
depth = None

# Check if player choice and depth are provided as command line arguments
if len(sys.argv) >= 5:
    # Retrieve the player choice and convert it to lowercase for case-insensitive comparison  
    player_choice = sys.argv[4].lower()
    # If player choice is 'human' or 'computer' with a valid depth argument, assign values accordingly   
    if player_choice == 'human' or (player_choice == 'computer' and len(sys.argv) >= 6 and sys.argv[5].isdigit()):
        first_player = player_choice
        depth = int(sys.argv[5]) if len(sys.argv) >= 6 and sys.argv[5].isdigit() else None
    # If the player choice is a numeric value, assign it as the depth    
    elif player_choice.isdigit():
        depth = int(player_choice)

while True:
         # Check if both marble piles are empty
        if marbles_piles[0] == 0 and marbles_piles[1] == 0:
            print('Enter marble values more than 0')
            break
       
        # Computer's turn
        if first_player == "computer":
             # Shows the current status of the marble piles and verifies if the game is completed.    
            if display_and_check(marbles_piles, version, depth):
                break
            
            print("Computer's turn")
            
            # Evaluate computer's move and update marble piles
            marbles_piles = eval_best_computer_move(marbles_piles, depth)
            print(f"Number of marbles left:- Red marbles = {marbles_piles[0]}, Blue marbles = {marbles_piles[1]}")

            # Switch to human's turn
            first_player = "human"          
           
            
        # Human's turn    
        else:        
            
            # Shows the current status of the marble piles and verifies if the game is completed.        
            if display_and_check(marbles_piles, version, depth):
                break
            
            # Get move from the user
            chosen_color = input("Please specify the marble color you wish to remove (Red/Blue): ")
            
            
            # Update marble piles based on user's choice
            if chosen_color.lower().strip() == "red":
                marbles_piles = (marbles_piles[0] - 1, marbles_piles[1])
            elif chosen_color.lower().strip() == "blue":
                marbles_piles = (marbles_piles[0], marbles_piles[1] - 1)
            else:
                print("Invalid choice. Please select either red or blue.")
                continue
                
            print(f"Number of marbles left:- Red marbles = {marbles_piles[0]},marbles_piles Blue marbles = {marbles_piles[1]}")
            
            if marbles_piles[0] == 0 or marbles_piles[1] == 0:
                amount = calculate_final_score(marbles_piles, depth)
                if version == "misere":
                    print("Human wins with a score of", abs(amount), "!")
                else:
                 print("Computer wins with a score of", abs(amount), "!")
                break
            
            # Switch to computer's turn
            first_player = "computer"
           


