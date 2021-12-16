from flask import Flask, render_template, request, session

from data_utils import save_the_data, process_data

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


        allWords = []
        bigWords = []
        smallWords = []

        with open("words.txt") as f:
            words = f.readlines()

            for x in words:
                allWords.append(x)

            for j in range(len(allWords)):
                allWords[j] = allWords[j].replace(" ", "")
                allWords[j] = allWords[j].replace("'s", "")
                allWords[j] = allWords[j].replace("\n", "")
        
        for y in allWords:
            if len(y) > 7:
                bigWords.append(y.lower())
            else:
                smallWords.append(y.lower()
            )

        wordToGuess = random.choice(bigWords)
        session['wordToGuess'] = wordToGuess

        session['smallWords'] = smallWords

        return render_template(
            "game.html", title="Gameplay", guessWord=wordToGuess
        )  



@app.get("/checkResults")
def check_results():
    wordToGuess = session.get('wordToGuess')
    smallWords = session.get('smallWords')

    if wordToGuess in smallWords:
        if len(wordToGuess) >= 4:
            wordGood = True

    # bigWord = Counter(wordToGuess)
    # smallWord = Counter(_word)
    # isCorrect = False
    # _word = smallWord - bigWord
    # if bool(_word) == True:
    #     isCorrect = False
    #     print(isCorrect)
    # if bool(_word) == False:
    #     isCorrect = True
    #     print(isCorrect)

    # for i in guess:
    #     isCorrect = isWordInBigWord(i)
    #     if isCorrect == False:
    #         break


    # tempGuessList = guess.copy()
    # wordCounter = 0
    
    # for words in tempGuessList:
    #     if _word == words:
    #         wordCounter = wordCounter + 1
    #         tempGuessList[tempGuessList.index(_word) ].replace(_word,'0', 1)
            
    #     if wordCounter > 1:
    #         print('word is reused')
    #         return True
    #     else:
    #         return False

    # isWordTheSame = False
    # for i in guess:
    #     if i == wordToGuess:
    #         isWordTheSame = True

    # for i in guess:
    #     isWordReused = isWordUsedMoreThanOnce(i, guess)
    #     if isWordReused == True:
    #         break

    win = False
    # if len(guess) == 7:
    #     if isCorrect == True:
    #         if isWordReused == False:
    #             if isWordTheSame == False:
    #                 win = True
    #                 print(win)

    return render_template(
        "checkResults.html", title="Results", didWin=win
    )  
        

   # """ Get, Save, Process and Display the score data. """
  #  the_player = request.form["player"]  # from the HTML form.
  #  the_score = session[
  #      "current_score"
  #  ]   gets the session value for the current browser.
  #  save_the_data(the_player, the_score)
  #  where, how_many, ordered = process_data(the_score, the_player)
 #  return render_template(
 #       title="Here is how you did",
 #       name=the_player,
  #      score=the_score,
  #      position=where,
 #      length=how_many,
    #    topten=ordered,
  # )




app.secret_key = "fhfho;dsi8 iergo;ireaj 90eru goerij 0re9uirae90eua gerg9eraugaer 9re"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
