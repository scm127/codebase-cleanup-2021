
from random import choice

VALID_OPTIONS=["rock","paper", "scissors"]

def determine_winner(p1,p2):
    return 

if __name__ == '__main__':
    pass


# USER SELECTION
#
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

#if u == "rock" and c == "rock":
#    print("It's a tie!")
#elif u == "rock" and c == "paper":
#    print("The computer wins")
#elif u == "rock" and c == "scissors":
#    print("The user wins")

#elif u == "paper" and c == "rock":
#    print("The computer wins")
#elif u == "paper" and c == "paper":
#    print("It's a tie!")
#elif u == "paper" and c == "scissors":
#    print("The user wins")

#elif u == "scissors" and c == "rock":
#    print("The computer wins")
#elif u == "scissors" and c == "paper":
#    print("The user wins")
#elif u == "scissors" and c == "scissors":
#    print("It's a tie!")
if u=="rock":
    if c=="rock":
        print("It's a tie!")
    elif c=="paper":
        print("The computer wins")
    if c=="scissors":
        print("The user wins")
elif u=="paper":
    if c=="rock":
        print("The user wins")
    elif c=="paper":
        print("It's a tie!")
    elif c=="scissors":
        print("The computer wins")
elif u=="scissors":
    if c=="rock":
        print("The computer wins")
    elif c=="paper":
        print("The user wins")
    elif c=="scissors":
        print("It's a tie!")

