from english_words import english_words_lower_set
import random

fiveletterwords = []
counter = 6

for word in english_words_lower_set:
    if len(word) == 5:
        fiveletterwords.append(word)


def wordguess(guess, choice, counter):
    counter -= 1
    if counter > 0:
        if len(guess) != 5 or guess not in fiveletterwords:
            print("Unkown word, or not 5 letters long")
            print(counter, "tries left")
            wordguess(input("enter a 5 letter word"), choice, counter)
        else:
            wordcomparisson(guess, choice)
            wordguess(input("enter a 5 letter word"), choice, counter)
    else:
        print("you ran out of tries")
        return

def wordcomparisson(guess, choice):
    if guess == choice:
        print("well done")
    else:
        for i in range(0,5):
            if guess[i] in choice:
                if guess[i] == choice[i]:
                    print(guess[i], "is in the right place")
                else:
                    print(guess[i], "is in the word, but not in the right place")
            else:
                print(guess[i], "is not in the word")
        wordguess(input("enter a 5 letter word"), choice, counter)

choice = random.choice(fiveletterwords)
wordguess(input("enter a 5 letter word"), choice, counter)
