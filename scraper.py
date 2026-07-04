import requests
from bs4 import BeautifulSoup

def scrape_books(): #defining scrape_books library we created that visit website and extract info
    url = "https://books.toscrape.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    book_cards = soup.find_all("article", class_="product_pod")

    book_list = [] #adding a dictionary for each book

    for book in book_cards:
        title = book.h3.a["title"]
        price = float(
            book.find("p", class_= "price_color")
                .text
                .replace("Â£", "")
        )
        availability = book.find("p", class_="instock availability").text.strip()

        print(price, type(price))
        
        book_list.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    return book_list