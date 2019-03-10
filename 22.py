numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    if answer in numbers:
           print("You guessed correctly!")
    else:
          print("You guessed incorrectly!")
