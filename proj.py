import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict

@dataclass
class Product:
    body: str 
    title: str 
    price: str 


def get_html(page):
    url = f"https://www.ceneo.pl/Urzadzenia_wielofunkcyjne_atramentowe;0020-30-0-0-{page}.htm"
    resp = httpx.get(url)
    return HTMLParser(resp.text)


def parse_products(html):
    products = html.css("div.product")

    results = []
    for item in products:
        new_item = Product(
            body=item.css_first("span.cat-prod-row__body").text(),
            title=item.css_first("span.cat-prod-row__name").text(),
            price=item.css_first("span.price").text().strip()
        )
        print(asdict(new_item))
 
def main():
    for x in range(1,3):
         html = get_html(x)
         print(html.css_first("title").text())
         parse_products(html)

if __name__ == '__main__':
    main()
