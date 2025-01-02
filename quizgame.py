print("Welcome This is my 1st project")

player = input("Do you want to play the game? ")
print("player", player)
if player.lower() != "yes":
    quit()
print("Let's play the Game")

answer = input("What does CPU stands for ")
if answer.lower() == 'central processing unit':
    print("Your Answer is correct")
else:
    print("Your answer is not correct")
answer = input("What does GPU stands for ")
if answer.lower() == 'graphics processing unit':
    print("Your Answer is correct")
else:
    print("Your answer is not correct")
