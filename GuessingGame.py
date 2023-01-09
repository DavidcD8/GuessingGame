secret_word = "jelly"
guess = ""
guess_count = 0
available_guesses = 3

while guess != secret_word and available_guesses > 0:
    guess = input("Enter a word: ")
    if guess == "1" or guess == "100":
        print("Wrong character try again")
        continue
    else:
        guess_count += 1
        available_guesses -= 1

        if available_guesses == 0 and guess != secret_word:
            print("No more tries available, You lost")
        elif guess != secret_word:
            print("Incorrect, Try again!")
            print("Number of tries", guess_count)
            print("Nuber of tries remaining", available_guesses)
        elif guess == secret_word:
            if guess == secret_word and available_guesses == 2:
                print("You win!")
                print("You guessed the word in", guess_count, "Attempt")
            elif guess == secret_word:
                print("You win!")
                print("You guessed the word in", guess_count, "Attempts")
