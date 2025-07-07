import sqlite3

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()

# Create a sample users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Add some dummy data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Naveen", "naveen@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Priya", "priya@example.com"))

conn.commit()
conn.close()

print("demo.db and users table initialized.")