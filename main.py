import requests
from lxml import html
import csv

def gesintuvu_kainos(url: str, output_format: str):
    response = requests.get(url)
    responce.raise_for_status()
    tree = html.fromstring(response.content)

    products = tree.xpath("//div[contains(@class, product-title)]/text()")
    prices = [price.strip() for price in prices]

    if output_format == "dict":
        return {"products": products, "prices": prices}
    elif output_format == "list":
        return list(products, prices)
    elif output_format == "csv":
        csv_file = "gesintuvai.csv"
        with open(csv_file, "w", newline="", encoding = "utf - 8") as file:
            writer = csv.writer(file)
            writer.writerow(["Gesintuvas", "Kaina"])
            writer.writerows(products, prices)
        csv_file = "gesintuvai.csv"

    else:
        raise ValueError("Klaida")