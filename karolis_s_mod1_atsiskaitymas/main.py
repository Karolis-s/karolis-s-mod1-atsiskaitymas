import requests
from lxml import html
from lxml.html import fromstring
import csv

def crawl(source, return_format='csv'):

    if source == "eurovaistine":
        data = crawl_eurovaistine()
    else:
        raise ValueError("Netinkamas tinklalapis")

    if return_format == "csv":
        return save_as_csv(data)
    elif return_format == "dict":
        return data
    elif return_format == "list":
        return [list(item.values()) for item in data]
    else:
        raise ValueError("Klaida")


def crawl_eurovaistine():

    url = "https://www.eurovaistine.lt/kosmetika/"
    response = requests.get(url)
    response.raise_for_status()

    tree = html.fromstring(response.content)

    products = tree.xpath ("//div[contains(@class, 'Content')]")

    for product in products:

        titles = product.xpath (".//input[@name= 'title')]/@value")[0]
        prices = product.xpath (".//input[@name= 'priceContainer')]/@value")[0]

        print (f"Product Name: {titles}")
        print (f"Product Price: {prices}")

    return products

def save_as_csv(data):

    filename = "output.csv"

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'priceContainer']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerow(data)
    return filename