import sqlite3

def search_player_by_name(name):
    # Connect to the SQLite database
    conn = sqlite3.connect('bb_stats.db')
    cursor = conn.cursor()

    # Use LOWER() for case-insensitive search
    cursor.execute("SELECT * FROM players WHERE LOWER(name) = LOWER(?)", (name,))
    players = cursor.fetchall()  # fetchall() returns all matching results

    if players:
        print(f"Players found for '{name}':")
        for player in players:
            # Display each player's stats if found
            print(f"ID: {player[0]}")
            print(f"Name: {player[1]}")
            print(f"School: {player[2]}")
            print(f"Batting Average: {player[3]}")
            print(f"ERA: {player[4]}")
            print(f"Year: {player[5]}")
            print("-" * 40)  # Separator between players
    else:
        # If no player is found, print a message
        print(f"No player found with the name '{name}'.")

    # Close the connection
    conn.close()

# Main execution
if __name__ == "__main__":
    # Take input from the user
    player_name = input("Enter the player's name: ").strip()

    # Search for the player in the database
    search_player_by_name(player_name)
