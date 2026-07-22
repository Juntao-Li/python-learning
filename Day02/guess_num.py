import random

num = random.randint(1, 100) #[1 ,100]

while True:
    guess_num = int(input("Input a number:"))
    if guess_num > num:
        print("The number you guess is bigger than the result!")
    elif guess_num < num:
        print("The number you guess is smaller than the result")
    else:
        print("Congratulations, you are right!")
        break
