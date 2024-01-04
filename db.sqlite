import sqlite3

def create_table():
    with sqlite3.connect('ages.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE Ages ( 
          name VARCHAR(128), 
          age INTEGER
        )''')

def insert_data():
    with sqlite3.connect('ages.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Ages")
        cursor.execute("INSERT INTO Ages (name, age) VALUES ('Jagoda', 21)")
        cursor.execute("INSERT INTO Ages (name, age) VALUES ('Alicia', 29)")
        cursor.execute("INSERT INTO Ages (name, age) VALUES ('Kaydn', 26)")
        cursor.execute("INSERT INTO Ages (name, age) VALUES ('Mishkat', 37)")

def get_hex_data():
    with sqlite3.connect('ages.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
        result = cursor.fetchone()
        return result[0]

create_table()
insert_data()
hex_data = get_hex_data()
print(hex_data)