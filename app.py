from flask import Flask, render_template #This means we're importing Flask class from the Flask library
import sqlite3

app = Flask(__name__) #This creates the web application

@app.route("/") #This is a decorator
def home():
    connection = sqlite3.connect("price_tracker.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT title, price, date_scraped
    FROM prices
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    books = []

    for row in rows:
        books.append({
            "title": row[0],
            "price": row[1],
            "date_scraped": row[2]
        })

    return render_template("home.html", books=books) #Flask opens home.html and sends info of books to the browser

if __name__== "__main__":
    app.run(debug=True)