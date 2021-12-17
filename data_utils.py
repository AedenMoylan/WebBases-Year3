import DBcm


config = {
    'host': '192.168.1.5',
    'database': 'wordgameDB',
    'user': 'wordgameuser',
    'password': 'wordgamepasswd',
}


tempTime = 1

# def save_the_data(name, timeTaken, bigWord, smallWords, position):
#     guessStr=" ".join(smallWords)
#     SQL = """
#         insert into wordgametable
#         (name, time_taken, big_word, small_words, position)
#         values
#         (%s, %s, %s, %s, %s)
#     """
#     with DBcm.UseDatabase(config) as db:
#         db.execute(SQL, (name, timeTaken, bigWord, guessStr, position))

def save_the_data(name,timeTaken,bigWord, smallWords,position):
    guessStr=" ".join(smallWords)
    SQL = """
        insert into wordgametable
        (name,time_taken,big_word,small_words,position)
        values
        (%s,%s,%s,%s,%s)
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL,(name,timeTaken,bigWord, smallWords,position))




def save_the_logs(name,players_browser,players_ip,players_word, word_given):
    guessStr=" ".join(players_word)
    SQL = """
        insert into aedensLogs
        (name,players_browser,players_ip,players_words,word_given)
        values
        (%s,%s,%s,%s,%s)
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL,(name,players_browser,players_ip,guessStr, word_given))



def process_logs():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select * from aedensLogs order by date_played desc
        """
        db.execute(SQL)
        logs = []
        logs = db.fetchall()



    return logs


def process_data():
    with DBcm.UseDatabase(config) as db:
        SQL = """
          select * from wordgametable order by position desc
        """
        db.execute(SQL)
        scores = []
        scores = db.fetchall()
        non_null=lambda x : "  "
        for row in SQL:
            list=map(non_null,row)
            next=tuple(list)
            scores.append(next)




    return scores[:10]



    
