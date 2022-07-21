import random

#initializing the list of words
words_list: list = []
print("Enter (in lowercase only) words of length less than 12")

for _ in range(12):
    entry: str = input("Enter a word here: ")
    words_list.append(entry)

#randomly selecting a word from the list
set_word: str = random.choice(words_list)
set_word = set_word.lower()

#length of the word
total_len: int = len(set_word)

#total 12 attempts given
empty_list: list = ["_"]*total_len


for j in range(12):
    my_guess: str = input("\nGuess an alphabet: ").lower()

    #list of indexes of all the occurences of the alphabet
    l: list = []
    if my_guess in set_word:
        # first occurence of the alphabet in the word
        first_occ: int = set_word.find(my_guess)
        l.append(first_occ)
        if set_word.count(my_guess) > 1:
            for k in range(first_occ+1, total_len):
                if set_word.find(my_guess, k, k+1) == k:
                    l.append(k)

        for i in l:
            empty_list[i] = my_guess
        current_guess_status = "".join(empty_list)
        print(current_guess_status, f"\n{11-j} guesses left!")

        if "_" not in empty_list:
            print(f"Congrats! You have guessed the right word!\n You won in {j+1} attempts!")
            break

    else:
        print(f"{my_guess} not in the word. Try again!\n{11-j} guesses left!\n")
        if empty_list.count("_") != total_len:
            print(current_guess_status)
