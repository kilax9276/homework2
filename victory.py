

name = ['А.С. Пушкин','С. Есенин','Ф.И. Тютчев','А. Эйнштейн','Г.Эйнштейн']
was_born = ['06.07.1799', '03.10.1895', '05.12.1803', '14.03.1879', '30.08.1847']


count = 0

count_right_answers = 0


while count < 5:
    answer = input("Скажите когда родился " + name[count] + "?")
    if answer == was_born[count]:
        count_right_answers += 1
    count += 1


print("количество правильных ответов", count_right_answers)
print("количество ошибок", count - count_right_answers)
print("процент правильных ответов ", count_right_answers*100/count, "%", sep="")
