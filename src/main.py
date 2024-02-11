from functions import load_operations, filter_and_sort_operations, formatter_date, mask_number


def main():
    """
    основной функционал - для указанного JSON файла с операциями
    выводятся  5 последних выполненных клиентом операций в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """
    file_name = 'operations.json'  # Укажите имя файла
    operations = load_operations(file_name)

    last_operations = filter_and_sort_operations(operations)

    for operation in last_operations:

        print(formatter_date(operation['date']), operation['description'])

        if 'from' in operation:
            print(f'{mask_number(operation["from"])} -> {mask_number(operation["to"])}')
        else:
            print(mask_number(operation["to"]))

        print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')


if __name__ == '__main__':
    main()
