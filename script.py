import cards
import sqlite3

connect = sqlite3.connect('cards.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS cards_list(
            id INTEGER,
            title TEXT,
            link TEXT,
            description TEXT
        )""")

idea = cards.idea

for i in idea:
    connect = sqlite3.connect('cards.db')
    cursor = connect.cursor()
    a = f"{cards.idea[f'{i}']['title']}"
    b = f"{cards.idea[f'{i}']['link']}"
    c = f"{cards.idea[f'{i}']['description']}"
    print(i, a, b, c)
    content = [i, a, b, c]
    cursor.execute("INSERT INTO cards_list VALUES(?,?,?,?);", content)
    connect.commit()
