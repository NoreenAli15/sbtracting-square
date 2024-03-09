
import random
import math


# function to get the square of numbers from 1 to the starting number
def square(num):
    return [i * i for i in range(1, int(num ** 0.5) + 1)]  # get the square of numbers from 1 to the starting number


# choice A allow user to choose the starting number
# choice B to get any random number
print("Welcome in subtracting square game")
print("please choose one choice on from these choices")
choice = input("1)  enter the number "
               "2)  random number  ").upper()
while True:
    if choice not in ["1", "2"]:  # to ensure that user choose a valid choice
        choice = input("please select valid choice : \n").upper()  # take choice again in case of invalidity

    elif choice == "1":
        starting_number = int(input("please enter your starting number "))  # user input a starting number
        # ensure that the user input a non perfect square starting number
        while starting_number <= 0 or math.sqrt(starting_number) == int(math.sqrt(starting_number)):
            starting_number = int(input("please enter a valid starting number: "))
        break

    else:
        # choose a random number from 1 to 200
        starting_number = random.randint(1, 200)
        # ensure that the random number is not perfect square
        if math.sqrt(starting_number) == int(math.sqrt(starting_number)):
            starting_number = random.randint(1, 200)
        break

# ensure getting a positive starting number
if starting_number <= 0:
    print("please enter a positive starting number")
    starting_number = int(input("enter a starting number"))

while starting_number > 0:
    print(starting_number)
    player1 = int(
        input(" player 1:please enter a perfect sqaure number "))  # take a square number from the first player
    sq_num = square(starting_number)
    print(sq_num)  # list of square numbers that user is allowed only to use in the game
    while True:
        if player1 in sq_num:  # check that player1 choose number from the list
            starting_number -= player1  # subtract player1's input from the starting number
            print(starting_number)
            break
        else:  # in case that user choose number not in the list
            print("Please enter a valid perfect square number")
            player1 = int(input(" player 1:please enter a perfect sqaure number "))
    if starting_number == 0:  # player1 will win if he reach zero
        print("Player1 is the winner")
        break

    player2 = int(
        input("player2:please enter a perfect sqaure number "))  # take a square number from the second player

    sq_num = square(starting_number)
    print(sq_num)  # list of square numbers that user is allowed only to use in the game
    while True:
        if player2 in sq_num:  # check that player2 choose number from the list
            starting_number -= player2  # subtract player2's input from the starting number
            break
        else:  # in case that user choose number not in the list
            print("Please enter a valid perfect square number")
            player2 = int(input("player2:please enter a perfect sqaure number "))

    if starting_number == 0:  # player2 will win if he reach zero
        print("Player2 is the winner")
        break
