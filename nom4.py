from datetime import datetime, timedelta

date = datetime
while True:
    try:
        print('Введите дату отправления поезда в формате ДД/ММ/ГГ')
        date = datetime.strptime(input(), "%d/%m/%y")
        break
    except ValueError:
        print('Дата в неверном формате') 

print("Вам исполниться 10 000 дней в", date + timedelta(days=10000))
print("Вам исполниться 1 000 000 минут в", date + timedelta(minutes=1_000_000))
print("Вам исполниться 1 000 000 000 секунд в", date + timedelta(seconds=1_000_000_000))
