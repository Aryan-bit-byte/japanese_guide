import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "words.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Japanese_words (
        name TEXT PRIMARY KEY,
        meaning TEXT
    )
""")
conn.commit()


def add_words(word, meaning):
    if not word or not meaning:
        print("Word and meaning cannot be empty.")
        return

    cursor.execute(
        "INSERT OR REPLACE INTO Japanese_words (name, meaning) VALUES (?, ?)",
        (word, meaning),
    )
    conn.commit()
    print("Added successfully.")


def get_word_meaning(word):
    """Retrieve the meaning of a word from the database."""
    cursor.execute("SELECT meaning FROM Japanese_words WHERE name = ?", (word,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return "Word not found. Try adding it first."


if __name__ == "__main__":
    try:
        while True:
            print("\n--- Word Management ---")
            print("1. Add word")
            print("2. Search word")
            print("3. Exit")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                word = input("Enter Japanese word: ").strip()
                meaning = input("Enter meaning: ").strip()
                add_words(word, meaning)
            elif choice == "2":
                word = input("Enter word to search: ").strip()
                print(get_word_meaning(word))
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    finally:
        conn.close()