# import pandas as pd

import sqlite3

with sqlite3.connect('bb_stats.db') as conn:
    
    cursor = conn.cursor()

    # Drop the old players table if it exists
    cursor.execute("DROP TABLE IF EXISTS players")
    
    cursor.execute("PRAGMA table_info(players);")
    columns = cursor.fetchall()
    print("Table columns:", columns)

    cursor.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, name TEXT, school TEXT, ba FLOAT, era FLOAT, year INTEGER)")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Nick Banez', 'Allegheny College' , '.209' , 'N/A', 2025)")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Eric Gonzalez', 'Geneva', '.424' , 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Colin Marinpetro', 'Grove City', 0.397, 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Jaden Nestor-fox', 'Bethany', 0.394, 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Josiah Bodie', 'Franciscan', 0.391, 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Aaron Babu', 'Geneva', 0.376, 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Wade Stoehr', 'Franciscan', 0.372, 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('William Wolff', 'Allegheny', 0.286, 'N/A', '2024')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('William Wolff', 'Allegheny', 0.372, 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Sam Bevin', 'Grove City', 0.369, 'N/A', '2025')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Matt Jennings', 'Allegheny', 0.298, 'N/A', '2023')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Matt Jennings', 'Allegheny', 0.394, 'N/A', '2024')")
    cursor.execute("INSERT INTO players (name, school, ba, era, year) VALUES ('Matt Jennings', 'Allegheny', 0.360, 'N/A', '2025')")






    #cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Walker Cunningham', Allegheny College , N/A ,2.59)")
    # cursor.execute("INSERT INTO players (name, school, ba, era) VALUES ('Dante Dimatteo', W&J , N/A, 0.83)")
    conn.commit()

    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    
    print("Players in the database:")
    for player in players:
        print(f"ID: {player[0]}, Name: {player[1]}, School: {player[2]}, Batting Average: {player[3]}, ERA: {player[4]}, YEAR: {player[5]}")

# df = pd.read_csv('hitting_stats.csv')
# df2 = pd.read_csv('pitching_stats.csv')
# df.to_sql('baseball_stats', conn, if_exists='replace', index=False)
# df2.to_sql('baseball_stats', conn, if_exists='replace', index=False)
# conn.close()
