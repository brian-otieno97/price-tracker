import sqlite3
from scraper import scrape_books

# Connect to the database
connection = sqlite3.connect("price_tracker.db")

# Create a cursor
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    date_scraped TEXT
)
""")

# Get books from the scraper
books = scrape_books()

# Temporary date
date = "2026-07-04"

# Insert every book into the database
for book in books:
    print(book["title"])

    # Check the latest stored price for this book
    cursor.execute("""
    SELECT price
    FROM prices
    WHERE title = ?
    ORDER BY id DESC
    LIMIT 1
    """, (book["title"],))
    
    result = cursor.fetchone()
    
    if result is None:
        cursor.execute("""
        INSERT INTO prices (title, price, data_scraped)
        VALUES (?, ?, ?)
        """, (
            book["title"],
            book["price"],
            date 
        ))
    
    elif result[0] != book["price"]:
        cursor.execute("""
        INSERT INTO prices (title, price, date_scraped)
        VALUES (?, ?, ?)
        """, (
            book["title"],
            book["price"],
            date
        ))


# Retrieve all rows
cursor.execute("SELECT * FROM prices")

rows = cursor.fetchall()

print(rows)

# Save changes
connection.commit()

print("Table created successfully!")

# Close the connection
connection.close()