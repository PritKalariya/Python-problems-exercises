import sqlite3

def create_table():
    # 1. Make connection
    conn = sqlite3.connect("data.db")

    # 2. Craete a cursor object
    cur = conn.cursor()

    # 3. Crate the table
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # 4. Commit
    conn.commit()

    # 5. Close the connection
    conn.close()

# Create function to avoid duplicate entry
def insert(item, quantity, price):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

insert("Water Glass", 5, 100)
insert("Coffee Cup", 3, 200)

#Display the data
def view():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())