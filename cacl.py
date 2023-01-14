import os
def clearscr():
    os.system('cls' if os.name == 'nt' else 'clear')
print("Привет! Это программа создана для перевода из десятичной сисетмы в любые другие системы счисления")
print("")

while True:    

    a = input("Введите число которое хотите конвертировать: ")
    if (a.isdigit() == True):
        if (int(a) == 0):
            print("Ошибка, введите число ещё раз")
            continue
    else:
        print("Ошибка, введите число ещё раз")
        continue
    
    b = input("Введите систему числа: ")
    if (b.isdigit() == True):
        if (int(b) < 2 or int(b) > 16):
            print("Ошибка, введите число ещё раз")
            continue
    else:
        print("Ошибка, введите число ещё раз")
        continue
    
    n = input("Введите систему в которую хотите перевести число: ")
    if (n.isdigit() == True):
        if (int(n) < 2 or int(n) > 16):
            print("Ошибка, введите число ещё раз")
            continue
    else:
        print("Ошибка, введите число ещё раз")
        continue

    b = int(b)
    n = int(n)

    if b != 10:
        a = int(a, b)

    s = ''

    while a > 0:

            s = str(a % n) + s 

            a //= n
    print(s)
    
    cnt = int(input(('Введите 1, что бы продолжить или 0 для завершения работы: ')))
    if cnt == 0:
          break
    elif cnt != 1:
        break
    elif cnt == 1:
        clearscr()
        continue
       
