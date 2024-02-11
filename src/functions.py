import json


def load_operations(file_name):
    """
    Чтение данных из файла JSON
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        return json.load(file)


def filter_and_sort_operations(operations):
    filter_operations = []
    for oper in operations:
        if 'state' in oper and oper['state'] == 'EXECUTED':
            filter_operations.append(oper)

    sort_operations = sorted(filter_operations, key=lambda x: x['date'], reverse=True)[:5]
    return sort_operations


def formatter_date(date):
    date = date.split('T')
    date = date[0].split('-')
    return f'{date[2]}.{date[1]}.{date[0]}'


def mask_number(number):
    # Замаскировать номер карты или счета
    if 'Счет' in number:
        return 'Счет **' + number[-4:]
    else:
        card_number = number.split(' ')
        card_number[-1] = ' '.join([card_number[-1][:4], (card_number[-1][4:6] + '**'), '****', card_number[-1][-4:]])
        return ' '.join(card_number)
