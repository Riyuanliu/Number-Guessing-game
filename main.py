
import random
def number_guess():
    target = random.randint(0,100)
    guess = -1
    for i in range(1,8,1):
        guess=int(input(f"{i}th guess, Enter you Guess:"))
        if(guess == target):
            print(f"{i}th guess,Congratulations！！！")
            break
        elif guess > target:
            print(f"{i}th guess,Too high")
        elif guess < target:
            print(f"{i}th guess,Too low")

def main():
    number_guess()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
