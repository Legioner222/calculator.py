import math
from colorama import Fore
from time import sleep

print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Калькулятор сделан {Fore.WHITE}Legioner X#0723{Fore.LIGHTBLACK_EX}")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Вы можете подписатся на меня на Github: {Fore.WHITE}https://github.com/lnxcz")

answer=2
while answer > 1:
    print('''Выберите режим
[1] Обычный
[2] Возведение
[3] сложный
[4] Дополнительный
[5] настройки''')
    mode=int(input())

    if mode == 1:
        answer=2
        while answer > 1:

            print('''\nВыберите действие
1 Сложение
2 Вычитание
3 Умножение
4 Деление''')
            mode=int(input())
            if mode == 1:
                print('Введите первое число:',end=' ')
                a=input()
                print('Введите второе число:',end=' ')
                b=input()

                otv = float(a)+float(b)
                print('Ответ: %s'%(otv))
            elif mode == 2:
                print('Введите первое число:',end=' ')
                a=input()
                print('Введите второе число:',end=' ')
                b=input()

                otv = float(a)-float(b)
                print('Ответ: %s'%(otv))
            elif mode == 3:
                print('Введите первое число:',end=' ')
                a=input()
                print('Введите второе число:',end=' ')
                b=input()

                otv = float(a)*float(b)
                print('Ответ: %s'%(otv))
            elif mode == 4:
                print('Введите первое число:',end=' ')
                a=input()
                print('Введите второе число:',end=' ')
                b=input()

                otv = float(a)/float(b)
                print('Ответ: %s'%(otv))
            print('\nВыйти из режима?\n1 да\n2 нет')
            answer=int(input())


    elif mode == 2:
        answer=2
        while answer > 1:
            print('''\nВыберите действие
1 Возведение в степень
2 Возведение в корень''')
            mode=int(input())

            if mode == 1:
                print('Введите число:',end=' ')
                a=input()
                print('Введите степень:',end=' ')
                b=input()

                otv = float(a)**float(b)
                print('Ответ: %s'%(otv))

            if mode == 2:
                print('''\nВыберите режим
1 Возведение в корень
2 Найти корень числа''')
                mode=int(input())

                if mode == 1:
                    print('Введите число:',end=' ')
                    a=input()
                    otv = math.sqrt(float(a))
                    print('Ответ: %s'%(otv))
                elif mode == 2:
                    print('Введите число:',end=' ')
                    a=input()
                    otv = float(a)**float(2)
                    print('Ответ: %s'%(otv))
        print('\nВыйти из режима?\n1 да\n2 нет')
        answer=int(input())

    elif mode == 3:
        answer=2
        while answer > 1:
            print('''\nВыберите действие
1 Найти синус
2 Найти косинус
3 Найти тангес
4 Найти арксинус
5 Найти арккосинус
6 Найти арктангенс''')
            mode=int(input())

            if mode == 1:
                otv = math.sin(int(a))
                print('Ответ: %s'%(otv))
            elif mode == 2:
                otv = math.cos(int(a))
                print('Ответ: %s'%(otv))
            elif mode == 3:
                otv = math.tan(int(a))
                print('Ответ: %s'%(otv))
            elif mode == 4:
                otv = math.asin(int(a))
                print('Ответ: %s'%(otv))
            elif mode == 5:
                otv = math.acos(int(a))
                print('Ответ: %s'%(otv))
            else:
                otv = math.atan(int(a))
                print('Ответ: %s'%(otv))
        print('\nВыйти из режима?\n1 да\n2 нет')
        answer=int(input())

    elif mode == 4:
        answer=2
        while answer > 1:
            print('''\nВыберите действие
1 Перевод оценок/триместровых оценок в разные системы''')
            mode=int(input())

            if mode == 1:
                print('\nКакую оценку ты хочешь перевести',end=' ')
                bal=int(input())
                if bal <= 5:
                    inbal=int(1)
                elif bal <= 10:
                    inbal=int(2)
                elif bal <= 100:
                    inbal=int(3)
#1========================================================================================================#
                if inbal == 1:
                    print('\nВ какую систему вы хотите перевести оценку\n1 10-бальной\n2 100-бальной')
                    outbal=int(input())
                    
                    if outbal == 1:
                        anbal = int(bal)+int(bal)
                        print('Ответ: %s'%(int(anbal)))
                    elif outbal == 2:
                        anbal = int(bal+bal)*10
                        print('Ответ: %s'%(int(anbal)))
#2========================================================================================================#
                elif inbal == 2:
                    print('\nВ какую систему вы хотите перевести оценку\n1 5-бальной\n2 100-бальной')
                    outbal=int(input())

                    if outbal == 1:
                        anbal = int(bal)//int(2)
                        if anbal <= 1:
                            print('Ответ: 2')
                        else:
                            print('Ответ: %s'%(int(anbal)))
                    elif outbal == 2:
                        anbal = int(bal)*10
                        print('Ответ: %s'%(int(anbal)))
#3=========================================================================================================#
                elif inbal == 3:
                    print('\nВ какую систему вы хотите перевести оценку\n1 5-бальной\n2 10-бальной')
                    outbal=int(input())

                    if outbal == 1:
                        if bal <= 0:
                            print('Ответ: 2')
                        elif bal <= 60:
                            print('Ответ: 3')
                        elif bal <= 80:
                            print('Ответ: 4')
                        elif bal <= 90:
                            print('Ответ: 5')
                        print('Ответ: %s'%(int(anbal)))
                    elif outbal == 2:
                        anbal = int(bal)//10
                        delbal = bal
                        dotanbal = int(delbal)%10
                        print('Ответ: %s.%s'%(int(anbal),int(dotanbal)))
#=========================================================================================================#
                else:
                    print('\nТакой системы нет')
#=========================================================================================================#
        print('\nВыйти из режима?\n1 да\n2 нет')
        answer=int(input())
    else:
        print('Такого режима не существует')
print('\nВыключить?\n1 да\n2 нет')
answer=int(input())