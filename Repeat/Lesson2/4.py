import datetime as dt

with open("tumnus_diary.txt", 'r', encoding='UTF-8') as f:
    date = f.readline().strip().rsplit(" ", maxsplit=1)[1]

date = dt.datetime.strptime(date, "%d.%m.%Y")
current_date = dt.datetime.strptime(input().strip(), "%d.%m.%Y")

print(f"До встречи осталось {(date - current_date).days} дней")