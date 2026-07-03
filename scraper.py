import requests
from bs4 import BeautifulSoup

def scrape_books(): #defining scrape_books library we created that visit website and extract info
    url = "https://books.toscrape.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    book_list = [] #adding a dictionary for each book

    for book in books:
        title = book.h3.a["title"]
        price = (
            book.find("p", class_= "price_color")
                .text
                .replace("Â", "")
        )
        availability = book.find("p", class_="instock availability").text.strip()

        book_list.append({
            "title": title,
            "price": price,
            "availabiliy": availability
        })

    return book_list