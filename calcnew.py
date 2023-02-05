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
        if int(max(str(a))) > int(b):
            print("Ошибка, введите число ещё раз")
            continue
    else:
        print("Ошибка, введите число ещё раз")
        continue
    
    n = input("Введите систему в которую хотите перевести число: ")
    
    b = int(b)
    n = int(n)
    s0 = 0

    if b != 10 and 2 < b < 16:
        a = int(a, b)
    else:
        s1 = str(a)[::-1]
        for i in range(len(s1)):
            s0 += int(s1[i]) * b**i 
        a = s0
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
