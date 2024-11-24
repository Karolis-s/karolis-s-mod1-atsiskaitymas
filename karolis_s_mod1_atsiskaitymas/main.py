import requests
from bs4 import BeautifulSoup
import csv

def crawl(source, return_format='csv'):

    if source == "pigu":
        data = crawl_pigu()
    elif source == "eurovaistine":
        data = crawl_eurovaistine()
    else:
        raise ValueError("Netinkamas tinklalapis")

    if return_format == "csv":
        return save_as_csv(data)
    elif return_format == "dict":
        return data
    else:
        raise ValueError("Klaida")


def crawl_pigu():

    url = "https://pigu.lt/lt/kompiuterine-technika/kompiuteriu-komponentai/termo-pastos/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find("div", class_="site-block clearfix")
    if not product:
        return {"title": "No product found", "price": "N/A"}

    title = product.find("a", class_="c-link--secondary").text.strip()
    price = product.find("span", class_="c-price h-price--medium").text.strip()

    return {"title": title, "price": price}

def crawl_eurovaistine():

    url = "https://www.eurovaistine.lt/kosmetika/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    product_elements = soup.find_all("div", class_="brand")

    for product in product_elements:
        title_element = product.find("a", class_="brand").text.strip()
        price_element = product.find("span", class_="newProductprice").text.strip()

    return products


def save_as_csv(data):

    filename = "output.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ())
        writer.writeheader()
        writer.writerow(data)
    return filename
