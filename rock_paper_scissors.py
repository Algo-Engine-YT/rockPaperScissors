import random

def user_wins(user, computer):
    if (user == 'rock' and computer == 'scissors' or
        user == 'paper' and computer == 'rock' or
        user == 'scissors' and computer == 'paper'):
        return True
    return False
    

def get_input():
    user = input("Choose rock, paper, scissors: ")
    user = user.lower().strip()
    return user


def main():
    user_score = 0
    computer_score = 0
    user = ""
    
    print('Quit anytime by typing "end"')
    while user != "end":
        print(f"Score: {user_score} - {computer_score}\n")
        computer = random.choice(['rock', 'paper', 'scissors'])
        user = get_input()

        # User ends game
        if user == 'end':
            print("Goodbye!")
        
        # Invalid input
        elif user not in ['rock', 'paper', 'scissors']:
            print("Invalid input")

        # Tie
        elif user == computer:
            print(f"I chose {computer} too. It's a tie!")

        # User wins
        elif user_wins(user, computer):
            print(f"I chose {computer}. You win!")
            user_score += 1
                
        # User loses
        else:
            print(f"I chose {computer}. You lose!")
            computer_score += 1


if __name__ == "__main__":
    main()

