while True: 
    # Проверка и ввод данных
    try:
        k = int(input('Ввод координаты клетки по горизонтали: '))
        if k > 8 or k < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        l = int(input('Ввод координаты клетки по вертикали: '))
        if l > 8 or l < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        m = int(input('Ввод координаты клетки по горизонтали, которую хотите атаковать: '))
        if m > 8 or m < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        n = int(input('Ввод координаты клетки по вертикали, которую хотите атаковать: '))
        if n > 8 or n < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        f = int(input('''Выбор фигуры: 
Чтобы выбрать ферзя, нажмите 1
Чтобы выбрать ладью, нажмите 2
Чтобы выбрать слона, нажмите 3
Чтобы выбрать коня, нажмите 4
Ваш выбор: '''))
        if f > 4 or f < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
    except ValueError:
        print('Введены некорректные данные. Попробуйте снова.')
        continue

    # Проверка на совпадение цвета
    if (k + l) % 2 == (m + n) % 2:
        print('Оба поля', end=' ')
        if (k + l) % 2 == 0:
            print('белого цвета')
        else:
            print('чёрного цвета')
    else:
        print('Поля разных цветов')

    # Расстояние по горизонтали и вертикали
    dx = abs(k - m)
    dy = abs(l - n)

    # Проверка на угрозу полю; второй ход
    if f == 1:     # Угрожает ли ферзь полю
        if k == m or l == n or dx == dy:
            print(f'Ферзь угрожает полю ({m}; {n})')
        else:
            print(f'Ферзь не представляет угрозы полю ({m}; {n})')
            print(f'Чтобы за два хода попасть в это поле встаньте на поле ({m}; {l})')
    elif f == 2:   # Угрожает ли ладья полю
        if k == m or l == n:
            print(f'Ладья угрожает полю ({m}; {n})')
        else:
            print(f'Ладья не представляет угрозы полю ({m}; {n})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m}; {l})')
    elif f == 3:   # Угрожает ли слон полю
        if dx == dy:
            print(f'Слон угрожает полю ({m}; {n})')
        else:
            print(f'Слон не представляет угрозы полю ({m}; {n})')
            if (k + l) % 2 != (m + n) % 2:
                print(f'Слон никаким образом не угрожает полю ({m}; {n})')
            else:   
                m0, n0, m1, n1 = m, n, 0, 0
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 += 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 -= 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 += 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = m
                n0 = n
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 -= 1
                    if abs(k - m0) == abs(l - n0):
                        m1 = m0
                        n1 = n0
                        break
                print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m1}; {n1})')
    else:   # Угрожает ли конь полю
        if abs(dx - dy) == 1:
            print(f'Конь угрожает полю ({m}; {n})')
        else:
            print(f'Конь не представляет угрозы полю ({m}; {n})')
    print('\nХотите продолжить? (Да/Нет)\n')
    vibor = input()
    if vibor == 'нет':
        break
    elif vibor == 'да':
        continue








