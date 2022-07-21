import random

#initializing the list of words
words_list = []
print("Enter (in lowercase only) words of length less than 12")
for _ in range(12):
    entry = input("Enter a word here: ")
    words_list.append(entry)

#randomly selecting a word from the list
word = random.choice(words_list)
#length of the word
total_len = len(word)

#total 12 attempts given
making = []
for _ in range(total_len):
    making.append("_") 

for j in range(12):
    alpha = input("\nGuess an alphabet: ")

    #list of indexes of all the occurences of the alphabet
    l = []
    if alpha in word:
        # first occurence of the alphabet in the word
        first_occ = word.find(alpha)
        l.append(first_occ)
        if word.count(alpha) > 1:
            for k in range(total_len - first_occ):
                if word.find(alpha, 1+first_occ+k, k+2+first_occ) == k+1+first_occ:
                    l.append(k+1+first_occ)

        for i in l:
            making[i] = alpha
        current_guess_status = "".join(making)
        print(current_guess_status, f"\n{11-j} guesses left!")

        if "_" not in making:
            print(f"Congrats! You have guessed the right word!\n You won in {j+1} attempts!")
            break

    else:
        print(f"{alpha} not in the word. Try again!\n{11-j} guesses left!")
        print(current_guess_status)
