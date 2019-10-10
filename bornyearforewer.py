
is_bad_answer = True

while  is_bad_answer:
    answer = input('Tell me, when A.S. Pushkin was born?')

    if answer == "06.07.1799":
        print('You are right!')
        is_bad_answer = False
    else:
        print('Try again!')
