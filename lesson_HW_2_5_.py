
#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например,
#my_list = [7, 5, 3, 3, 2].



raiting_1 = []

while True:
    item = input('Пожалуйста введите число: ')
    if not item.isdigit():
        print("Введены некорректные данные. Попробуйте снова")
        continue
    else:
        item = int(item)

    idx = None

    for i, num in enumerate(raiting_1):
        if item > num:
            idx = i+1
            break

    if idx is None:
        raiting_1.append(item)
    else:
        raiting_1.insert(idx, item)

    print(raiting_1)

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break
    print(raiting_1)