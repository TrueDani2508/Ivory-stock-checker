import requests
from bs4 import BeautifulSoup

item = "3080"
firm = "asus"

print(item, "stock checker!")


def get_page_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    # print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    products = soup.findAll("div", {
        "class": "col-md-12 col-12 title_product_catalog mb-md-1 hoverorange main-text-area"})
    # for product in products:
    #     if item in product.text and firm in product.text.lower():
    #         print("In stock:", product.parent.parent.parent.attrs['href'])
    stock = [product.parent.parent.parent.attrs['href'] for product in products if item in product.text and firm in product.text.lower()]
    return stock


def check_inventory():
    url = "https://www.ivory.co.il/catalog.php?act=cat&id=2652&f=1258.2517&orderBy=priceHigh"
    page_html = get_page_html(url)
    stock_list = check_item_in_stock(page_html)
    if len(stock_list) != 0:
        print("In stock in the following links:")
        for link in stock_list:
            print(link)
    else:
        print("Out of stock") 


check_inventory()
