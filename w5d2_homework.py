import psycopg2
import csv


def add_to_database():
    con = psycopg2.connect(database='w5d2_database', user='Envy')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS players (Id serial PRIMARY KEY,
    No decimal, Name varchar, Age numeric, Game numeric, Yards numeric,
    YardsTotal numeric, Touchdowns numeric);""")

    with open('/Users/Envy/Documents/TIY/week5/player_stats.csv') as f:
        rows = csv.reader(f, delimiter=',')
        header = next(rows)

        player_insert_query = """
        INSERT INTO players (No, Name, Age, Game, Yards, YardsTotal, Touchdowns)
        SELECT %s, %s, %s, %s, %s, %s, %s
        WHERE
            NOT EXISTS (
                SELECT Id FROM players WHERE No = %s
            );
        """

        for row in rows:
            cur.execute(player_insert_query, (row[0], row[1], row[2], row[4], row[7], row[22], row[23], row[0]))

    con.commit()
    cur.close()
    con.close()
