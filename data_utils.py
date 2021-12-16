import DBcm


config = {
    'host': '127.0.0.1',
    'database': 'leaderboardDB',
    'user': 'leaderuser',
    'password': 'leaderpasswd',
}




def save_the_data(name, score):
    SQL = """
        insert into board
        (name, score)
        values
        (%s, %s)
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL, (name, score))


def process_data(the_score, the_player):
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select name, score
            from board
            order by score desc
        """
        db.execute(SQL)
        scores = db.fetchall()
    where = scores.index((the_player, the_score)) + 1
    how_many = len(scores)

    return where, how_many, scores[:10]
