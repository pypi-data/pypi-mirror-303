import json


def create_receipt(input,output):
    with open(input, 'r', encoding='utf-8') as json_file:
        content = json.load(json_file)
        print(content)


        with open(output, 'a', encoding='utf-8') as f:
            sm = 0
            f.write(f'Клиент: {content['customer_name']}\n')
            for item in content['items']:
                f.write(f'Товар: {item['name']}\n')
                f.write(f'  Кол-во: {item['quantity']}\n')
                f.write(f'  Цена за ед.: {item['price']}\n')
                sm += int(item['quantity']) * int(item['price'])
            f.write(f'Сумма: {sm}')