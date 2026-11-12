# import Hello

# Hello.hello
# Hello.bye

# import random

# choices = ["rock", "paper", "scissors"]

# computer = random.choice(choices)

# player = input("rock, paper or scissors?: ")

# print("computer: ",computer)
# print("player: ",player)

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("---------------------")
        print(key)
    for i in options[question_num -1]:
        print(i)
    guess = input("Enter (A, B, C or D): ")
    guess = guess.upper()
    guesses.append(guess)
    correct_guesses += check_answer(questions.get(key),guess)
    question_num += 1
    display_score(correct_guesses,guesses)

questions = {"what year is ronaldo born? :" "A"
             "who is ronaldo? :" "B"
             "which country is he from? :" "C"
             "is he married? :" "A"
             }
options = [["A. footballer", "B. singer", "C. pastor", "D. dancer"],
           ["A. 1991", "B. 1984", "C. 1980", "D. 1999"],
           ["A. Brazil", "B. Nigeria", "C. Portugal", "D. Ghana"],
           ["A. Yes", "B. No", "C. Maybe", "D. Gay"]
           ]


def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG!")
        return 0
    
def display_score(correct_guesses, guesses):
    print("-------------------")
    print("RESULTS")
    print("-------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
        print()
    print("guesses: ", end="")
    for i in guesses:
        print(i, end="")
        print()

def play_again():
    response = input("Do you want to play again? (Yes or No): ")
    response = response.upper
    if response == "YES":
        return True
    else:
        return False
    
new_game()
while play_again():
    new_game()

print("Byeeee: ")


