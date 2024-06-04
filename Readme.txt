Name: Archi Sahu
Id: 1002104548

Programming Langauge: Python 3.11.2

Code structure:
First I am reading the inputs from command line and setting version as standard and first-player as computer if value is not given. Now, According to computer or human turn will proceed further. During the computer's turn, it calculates the best move using the minimax algorithm, while the human player makes moves based on input provided through the command line.


Steps to run the code:
1. Install python in your system and extract the zip 
2. Open the command prompt where you save the files
3. To run the python code in the command prompt write "python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>"


Example: python red_blue_nim.py 3 4 standard human 4
output:

Number of marbles left:- Red marbles = 3,marbles_piles Blue marbles = 4
Computer's turn
Number of marbles left:- Red marbles = 2, Blue marbles = 4
Number of marbles left:- Red marbles = 2,marbles_piles Blue marbles = 4
Please specify the marble color you wish to remove (Red/Blue): red
Number of marbles left:- Red marbles = 1,marbles_piles Blue marbles = 4
Number of marbles left:- Red marbles = 1,marbles_piles Blue marbles = 4
Computer's turn
Number of marbles left:- Red marbles = 0, Blue marbles = 4
Number of marbles left:- Red marbles = 0,marbles_piles Blue marbles = 4
Human wins with a score of 12


Example: python red_blue_nim.py 3 4  misere computer 4
output:

Number of marbles left:- Red marbles = 3,marbles_piles Blue marbles = 4
Computer's turn
Number of marbles left:- Red marbles = 2, Blue marbles = 4
Number of marbles left:- Red marbles = 2,marbles_piles Blue marbles = 4
Please specify the marble color you wish to remove (Red/Blue): red
Number of marbles left:- Red marbles = 1,marbles_piles Blue marbles = 4
Number of marbles left:- Red marbles = 1,marbles_piles Blue marbles = 4
Computer's turn
Number of marbles left:- Red marbles = 0, Blue marbles = 4
Number of marbles left:- Red marbles = 0,marbles_piles Blue marbles = 4
Computer wins with a score of 12
   

