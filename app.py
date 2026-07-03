from flask import Flask, render_template #This means we're importing Flask class from the Flask library
from scraper import scrape_books

app = Flask(__name__) #This creates the web application

@app.route("/") #This is a decorator
def home():
    books = scrape_books() #run scraper and store the list in variable 'books'
    return render_template("home.html", books=books) #Flask opens home.html and sends info of books to the browser

if __name__== "__main__":
    app.run(debug=True)