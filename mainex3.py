# number of gusses
# number of gusses left and then game over

n = 18
number_of_guesses = 1
print("number of guesses is limited to only 9 times : ")
while (number_of_guesses<=9):
    guess_number = int(input("guess the number : \n"))
    if guess_number>18:
        print("you enter greater number please enter smaller one.\n")
    elif guess_number<18:
        print("you enter a smaller number please enter greater one.\n")
    else:
        print("you won\n")
        print(number_of_guesses,"no of guesses he took to finish")
        break
    print(9-number_of_guesses,"no of guesses left")
    number_of_guesses = number_of_guesses + 1
if (number_of_guesses>9):
    print("game over")