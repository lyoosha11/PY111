import json


"""Task_DZ"""
with open("DZ_json.json", 'w', encoding='utf-8') as purchase:
    shop_list = []
    while True:
        product = input('Enter product (or "stop" to exit): ')
        if product == 'stop':
            break
        pr = int(input('Enter price of product: '))
        shopping = dict(name=product, price=pr)
        shop_list.append(shopping)
    json.dump(shop_list, purchase, ensure_ascii=False)

with open("DZ_json.json", encoding='utf-8') as purchase:
    all_shop = json.load(purchase)
    print(all_shop)
    summ = 0
    for prod in all_shop:
        summ += prod['price']
    print(f'The price of purchases per day = {summ}')