while True:
    year = input('Введите год рождения Пушкина: ')
    if year == '1799':
        while True:
            day = input('Введите день рождения Пушкина: ')
            if day == '26':
                break
            else:
                print('День введен неверно')
        break
    print('Год введен неверно')
print('Верно')