from flask import Flask, render_template, request, session

from data_utils import save_the_data, process_data
from datetime import datetime

import random
from collections import Counter

app = Flask(__name__)

@app.get("/")
@app.get("/rules")
def show_rules():
    return render_template(
        "rules.html", title="Rules:"
    )  


@app.get("/game")
def game_play():

    sourceword = get_source_word()

    game_core(sourceword)

    return render_template(
        "game.html", title="Gameplay", source_word = sourceword
    )  



@app.get("/checkResults")
def check_results():

    win = 0


    return render_template(
        "checkResults.html", title="Results", didWin=win
    )  
        


def isWordInBigWord(_word):
    bigWord = Counter(wordToGuess)
    smallWord = Counter(_word)
    isCorrect = False
    _word = smallWord - bigWord
    if bool(_word) == True:
        isCorrect = False
        print(isCorrect)
    if bool(_word) == False:
        isCorrect = True
        print(isCorrect)
    return isCorrect



def game_core(sourceword):
    mainWord = Counter(sourceword)
    guesswordList = []
    wordWrong = False
    wordRight = False
    wordMistake = False
    wordShort = False
    wordEqualToSource = False


    starttime = datetime.datetime.now()
    for guesses in range(7):                           
        guessWord = input("Enter Words:")              # Creates a string that will store the guessWord
        guesswordList.append(guessWord)                # Adds to the end of the list which contains all the guess words
        guess = Counter(guessWord)                     # Creates a counter which counts all the letters to check against the source word
        guess = guess - mainWord                       # Checks if all the letters inside the source word, match the letters inside the guess word
        mainWord = Counter(sourceword)                 # Reassigns the source word to main word, so you can check the next word
        
        if sourceword == guessWord:
            wordEqualToSource = True
        
        if len(guessWord) >= 4:
            with open("final.txt", "r") as sf:
                for line in sf:
                    stripped_line = line.strip()
                    if stripped_line == guessWord:
                        wordRight = True
                    else:
                        print("One or more of your words are not correct")
                        wordRight = False

            if wordRight == False:
                wordMistake = True
                print("The word is not real")
            if wordRight == True:
                print("it is found")
                wordRight = False
                if bool(guess) == True: # Checks if the guess word is empty, and if it isn't, the letters don't match
                    print("Your letters don't match")
                    wordWrong = True ## this will currently break out of the loop, if the word does not match
                    break
                if bool(guess) == False: # Checks if the guess word is empty, and if it is, then the letters match
                    print("You guessed correctly")
        else:
            wordShort = True
        
            
    endtime = datetime.now()

    resulttime = endtime - starttime
    resulttime = str(resulttime)
    print("You finished in" ,resulttime)

    duplicates = checkDupes(guesswordList)

    if duplicates == True:
        print("You have a duplicate in your words")
    if wordMistake == True:
        print("One or more of your words are not correct")
    if wordShort == True:
        print("One or more words are less than 4 letters")
    if wordEqualToSource == True:
        print("One or more words are equal to the sourceword")




def setup_txt_file():
    with open('final.txt', "w") as fw:
        with open('small.txt',"w") as sf:
            with open("big.txt","w") as bf:
                with open("words.txt") as wf:
                    for w in wf:
                        if "'s" not in w:
                            print(w.strip().lower(), file = fw)
                            if len(w) > 7:
                                print(w.strip().lower(), file = bf)
                            else: 
                                print(w.strip().lower(),file = sf)


def get_source_word():
    with open("big.txt") as bf:
        myList = bf.read()
    myList = myList.split("\n")
    sourceword = random.choice(myList)
    print("sourceword is :" + sourceword)
    return sourceword


app.secret_key = "fhfho;dsi8 iergo;ireaj 90eru goerij 0re9uirae90eua gerg9eraugaer 9re"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
