import json
import os

def generate_receipt(input_file: str, output_file: str):
    # Проверяем существование входного файла
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Файл {input_file} не найден.")

    # Читаем данные из входного файла
    with open(input_file, 'r', encoding='utf-8') as f:
        order_data = json.load(f)

    customer_name = order_data['customer_name']
    items = order_data['items']
    
    total_amount = sum(item['quantity'] * item['price'] for item in items)

    # Формируем текст чека
    receipt_lines = [f"Чек для: {customer_name}\n"]
    receipt_lines.append("Товары:\n")
    
    for item in items:
        receipt_lines.append(f"{item['name']} (количество: {item['quantity']}, цена за единицу: {item['price']} руб.)\n")
    
    receipt_lines.append(f"\nОбщая сумма заказа: {total_amount} руб.\n")

    # Записываем чек в выходной файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(receipt_lines)

    print(f"Чек успешно создан: {output_file}")
