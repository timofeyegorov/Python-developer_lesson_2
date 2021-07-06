''' Игра викторина'''

play = 'да'

while True:
    if play == 'нет':
        break
    if play == 'да':
        year1 = input('Введите год рождения Криштиану Роналду: ')
        year2 = input('Введите год рождения Антуана Гризмана: ')
        year3 = input('Введите год рождения Рахима Стерлинга: ')
        year4 = input('Введите год рождения Лоренцо Инсинье: ')
        year5 = input('Введите год рождения Альваро Мората: ')

        answers = [year1, year2, year3, year4, year5]
        right_answers = ['1985', '1991', '1994', '1991', '1992']
        right = len([item for idx, item in enumerate(answers) if item == right_answers[idx]])
        wrong = len([item for idx, item in enumerate(answers) if item != right_answers[idx]])

        print('Правильных ответов: ', right)
        print('Ошибок: ', wrong)
        print('Процент правильных ответов: ', right/len(right_answers)*100)

        play = input('Сыгать еще раз? (да/нет): ')

print('Спасибо за игру!!!')