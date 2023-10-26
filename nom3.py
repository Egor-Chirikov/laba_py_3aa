from datetime import datetime

start_date = datetime
end_date = datetime

while True:
    try:
        print('Введите дату отправления поезда в формате ДД/ММ/ГГ ЧЧ:ММ')
        start_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
        break
    except ValueError:
        print('Дата в неверном формате')

while True:
    try:
        print('Введите дату прибытия поезда в формате ДД/ММ/ГГ ЧЧ:ММ')
        end_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
        if end_date <= start_date:
            print("Время прибытия должна быть больше времини отправления")
            continue
        break
    except ValueError:
        print('Дата в неверном формате')

print("Время в пути:", end_date - start_date)
