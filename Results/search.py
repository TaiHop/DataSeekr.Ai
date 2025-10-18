
import sqlite3

def search_player_by_name(name):
    # Connect to the SQLite database
    conn = sqlite3.connect('bb_stats.db')  
    cursor = conn.cursor()

    # Use a parameterized query to avoid SQL injection
    cursor.execute("SELECT * FROM players WHERE name = ?", (name,))
    player = cursor.fetchone()  # Use fetchone to get a single result

    if player:
        # Display the player's stats if found
        print(f"Player Found: ")  # noqa: F541
        print(f"ID: {player[0]}")
        print(f"Name: {player[1]}")
        print(f"School: {player[2]}")
        print(f"Batting Average: {player[3]}")
        print(f"ERA: {player[4]}")
    else:
        # If no player is found, print a message
        print("Player not found in the database.")

    # Close the connection
    conn.close()

# Main execution
if __name__ == "__main__":
    # Take input from the user
    player_name = input("Enter the player's name: ")

    # Search for the player in the database
    search_player_by_name(player_name)
