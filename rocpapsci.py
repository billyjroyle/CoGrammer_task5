import random

user_score = 0
computer_score = 0
play = True


def get_user_choice():
    while True:
        try:
            user_choice = input("Enter your choice (Rock, Paper or Scissors): ").lower()
            if user_choice not in ['rock', 'paper', 'scissors']:
                raise ValueError("Invailid choice! Please enter 'rock', 'paper' or 'scissors'.")
            return user_choice
        except ValueError as e:
            print(e)


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scisssors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        global user_score
        user_score += 1
        return "You win!"
    else:
        global computer_score
        computer_score += 1
        return "Computer wins!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

def reset_score():
    user_score = 0
    computer_score = 0
    

print("Let's play Rock, Paper, Scissors!")

while play == True:
    play_game()
    try:
        continue_play = input("Enter your choice (Rock, Paper or Scissors): ").lower()
        if continue_play not in ['y', 'n']:
            raise ValueError("Invailid choice! Please enter 'Y' or 'N'.")
    except ValueError as e:
            print(e)
    
    if continue_play == "y":
        play = True
    else:
        play = False
else:
    print("Thank you for playing, see you next time!")
    print(f"FINAL SCORE: User {user_score}:{computer_score} Computer")
    reset_score()