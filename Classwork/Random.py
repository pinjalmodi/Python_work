import random

#print(random.randint(1,100))
#l=[1,2,10,20,"tops","tech","python",true,false,100,200]
#print(random.choice(l))

num=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 to 20"))
    if guess==num:
        print("You Guessed a correct Number")
        break
    elif guess>num:
        print("You guesses A greater Number")

    elif guess<num:
        print("You guessed A smaller Number")
