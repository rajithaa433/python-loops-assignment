# Task Requirements
        # Create a Python script named game_score.py that accomplishes the following:

        # Input Collection: Prompt the user to enter the player's name and store it as a string
        # Numeric Input Processing: Accept the number of games played and convert it to an integer data type
        # Score Data Entry: Collect the total score achieved and store it as an integer
        # Computation: Calculate the average score per game using division
        # Output Display: Present the results in the specified format shown below
        
# Expected Output Format
        # Player: <name>

        # Games Played: <number>

        # Total Score: <score>

        # Average Score: <average>        

##Input Collection
player_name = input("Enter the player's name: ")

# Numeric Input Processing
Number_of_games_played = int(input("Enter the number of games played: "))

# Score Data Entry
total_score = int(input("Enter the total score achieved: "))

# Computation
average_score = total_score / Number_of_games_played


# Output Display
print("\n--- Game Score Summary ---")
print("Player :", player_name)
print("Games Played:", Number_of_games_played)
print("Total Score:", total_score)
print("Average Score:", average_score)



######OUTPUT###################
# Enter the player's name: Raghu
# Enter the number of games played: 6
# Enter the total score achieved: 435

# --- Game Score Summary ---
# Player : Raghu
# Games Played: 6
# Total Score: 435
# Average Score: 72.5




