from flask import Flask, render_template, request, session

from data_utils import save_the_data, process_data, save_the_logs, process_logs
import datetime 

import random
from collections import Counter



app = Flask(__name__)

sourceWord = ""
guessWords = ""   

@app.get("/")
@app.get("/rules")
def show_rules():
    return render_template(
        "rules.html", title="Rules:"
    )  


@app.get("/game")
def game_play():
    setup_txt_file()
    srcwrd = get_source_word()
    global sourceWord
    sourceWord = srcwrd

    return render_template(
        "game.html", title="Gameplay", source_word = sourceWord
    )  



    
@app.get("/checkResults")
def check_results():

    global win
    gsswrds = request.args.get("playerinput").split(" ")  
 
    guessWords = gsswrds

    #guessWords = "cars vail vails nails nail snail lava"

    #guess = guessWords.split(" ")

    for i in guessWords:
        isCorrect = isWordInBigWord(i, sourceWord)
        if(isCorrect == False):
            tempThing = i
            break

    isWordTheSame = False
    for i in guessWords:
        if i == sourceWord:
            isWordTheSame = True
    
    for i in guessWords:
        isWordReused = isWordUsedMoreThanOnce(i, guessWords)
        if isWordReused == True:
             break

        
    win = False
    if len(guessWords) == 5:
        if isCorrect == True:
            #if isWordReused == False:
            if isWordTheSame == False:
                win = True
    print ()

    return render_template(
        "checkResults.html", title="Results", didWin=win
    )  
        

@app.get("/saveScore")
def saveTheScore():

    playerName = request.args.get("playerName")  
    time = datetime.datetime.now()
    position = 1

    score = 2
    ##date_played =120
    players_browser = request.user_agent.string
    players_ip = request.environ.get('HTTP_X_REAL_IP',request.remote_addr)

    


    if win == True:
        save_the_data(playerName,time,sourceWord, guessWords,position)
        process_data()

    save_the_logs(playerName,players_browser,players_ip,guessWords, sourceWord)
    process_logs()
    database = []     
    database = process_data()     
    print(database)

    return render_template(
        "saveScore.html", title="Score saved", data_base= database
    )
    

@app.get("/logs")
def processLogs():
    logbase = []
    logbase = process_logs()
    print(logbase)
    return render_template(
        "logs.html",
        data_base=logbase
    )





def isWordInBigWord(_word, _sourceWord):
    bigWord = Counter(_sourceWord)
    smallWord = Counter(_word)
   #isCorrect = False
    _word = smallWord - bigWord
    if bool(_word) == True:
        isCorrect = False
        print(isCorrect)
    if bool(_word) == False:
        isCorrect = True
        print(isCorrect)
    return isCorrect



def isWordUsedMoreThanOnce(_word,guess):
    tempGuessList = guess.copy()
    wordCounter = 0
    
    
    for words in tempGuessList:
        if _word == words:
            wordCounter = wordCounter + 1
         #   tempGuessList[tempGuessList.index(_word) ].replace(_word,'0', 1)
            if wordCounter > 1:
                break
            
        if wordCounter > 1:
            print('word is reused')
            usedMoreThanOnce = True
        else:
            usedMoreThanOnce = False

            return wordCounter 


def setup_txt_file():
    with open('final.txt', "w") as ff:
        with open('small.txt',"w") as sf:
            with open("big.txt","w") as bf:
                with open("words.txt") as wf:
                    for w in wf:
                        if "'s" not in w:
                            print(w.strip().lower(), file = ff)
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