from w5d2_homework import add_to_database
import psycopg2

add_to_database()
con = psycopg2.connect(database='w5d2_database', user='Envy')
cur = con.cursor()

user_choices = ['a', 'u', 's', 'p', 'x']
while True:
    print("Please enter A to add a player and his stats")
    print("Please enter U to update a players yards")
    print("Please Enter S to search for a player with a certain amount of yards")
    print("Please enter P to print out all players")
    print("Please enter X to exit")
    user_choice = input("Enter your choice: ").lower()
    if user_choice not in user_choices:
        continue
    if user_choice == 'a':
        cur.execute("INSERT INTO w5d2_database(no, name, age, game, Yards, YardsTotal, Touchdowns) VALUES(%s, %s, %s, %s, %s, %s, %s)", (input('Enter no: '), input('Enter name: '), input('Enter age: '), input('Enter game: '), input('Enter yards: '), input('Enter yardsTotal: '), input('Enter Touchdowns: ')))
        continue
    if user_choice == 'u':
        cur.execute("UPDATE w5d2_database SET yards=(%s) WHERE no = (%s)", (input('Enter new yards: '), input('Enter player no: ')))
        continue
    if user_choice == 's':
        cur.execute("SELECT * FROM w5d2_database WHERE yards > %s", (input('choose minimum yards: '),))
        results = cur.fetchall()
        print(results)
        continue
    if user_choice == 'p':
        cur.execute("SELECT * FROM w5d2_database;")
        cur.fetchall()
        continue
    if user_choice == 'x':
        con.commit()
        cur.close()
        con.close()
        exit()
