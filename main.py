import requests
import pandas as pd


def get_category():

    url = "https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json"
    headers = {
        "authority": "static-basket-01.wb.ru",
        'accept': '*/*',
        'accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'origin': 'https://www.wildberries.ru',
        'referer': 'https://www.wildberries.ru/',
        'sec-ch-ua': '^\^',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\^',
        'sec-Fetch-Dest': 'empty',
        'sec-Fetch-Mode': 'cors',
        'sec-Fetch-Site': 'cross-site',
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',

    }
    response = requests.get(url=url, headers=headers)
    # print(response.json())
    return response.json()
def prepare_items(response):
    products = []
    products_raw = response[0]['childs']
    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                # 'brand': product.get('brand', None),
                'name': product.get('name', None),
                'seo': product.get('seo', None),
                'childs':product.get('childs'[0:-1], None).get('name', None) if product.get('childs'[0:-1], None) != None else None
                # 'priceU': float(product.get('priceU', None)) / 100 if product.get('priceU', None) != None else None,
                # 'salePriceU': float(product.get('salePriceU', None)) / 100 if product.get('salePriceU', None) != None else None
            })
    return products


def main():
    response = get_category()
    products = prepare_items(response)
    print(products)
    pd.DataFrame(products).to_csv('products.csv', index=False)
    pd.DataFrame(response).to_csv('response.csv', index=True)
if __name__ == "__main__":
    main()
