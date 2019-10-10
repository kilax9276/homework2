
print('Скажите а вы знаете когда родился А.С. Пушкин?')
answer_year = input('Сначала введите год: ')

if int(answer_year) != 1799:
    print('Неверный год')
    exit(0)

answer_month = input('Теперь введите месяц: ')
answer_day = input('А теперь введите день: ')

if int(answer_month) != 7 and int(answer_day) != 6:
    print('Неверный день рождения')
else:
    print('Верно')
