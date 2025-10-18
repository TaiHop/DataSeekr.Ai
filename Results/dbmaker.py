# import pandas as pd

import sqlite3

with sqlite3.connect('bb_stats.db') as conn:
    
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(players);")
    columns = cursor.fetchall()
    print("Table columns:", columns)

    cursor.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, name TEXT, school TEXT, ba FLOAT, era FLOAT)")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Nick Banez', 'Allegheny College' , '.209' , 'N/A' )")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Eric Gonzalez', 'Geneva', '.424' , 'N/A' )")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Colin Marinpetro', 'Grove City', 0.397, 'N/A')")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Jaden Nestor-fox', 'Bethany', 0.394, 'N/A')")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Josiah Bodie', 'Franciscan', 0.391, 'N/A')")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Aaron Babu', 'Geneva', 0.376, 'N/A')")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Wade Stoehr', 'Franciscan', 0.372, 'N/A')")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('William Wolff', 'Allegheny', 0.371, 'N/A')")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Sam Bevin', 'Grove City', 0.369, 'N/A')")
    cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Matt Jennings', 'Allegheny', 0.360, 'N/A')")






    #cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Walker Cunningham', Allegheny College , N/A ,2.59)")
    # cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Dante Dimatteo', W&J , N/A, 0.83)")
    conn.commit()

    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    print("Players in the database:")
    for player in players:
        print(f"ID: {player[0]}, Name: {player[1]}, School: {player[2]}, Batting Average: {player[3]}, ERA: {player[4]}")

# df = pd.read_csv('hitting_stats.csv')
# df2 = pd.read_csv('pitching_stats.csv')
# df.to_sql('baseball_stats', conn, if_exists='replace', index=False)
# df2.to_sql('baseball_stats', conn, if_exists='replace', index=False)
# conn.close()
