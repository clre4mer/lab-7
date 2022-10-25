def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        return -1
    return n
def Vvod(h, p):
    n = 0
    if h == 1:
        while n == 0:
            n = input(f'Введите положение {p} клетки по горизонтали от 1 до 8\n')
            n = errorCheck(n)
            if (n > 8) or (n < 1):
                print('Ошибка ввода. Необходимо ввести цифру число от 1 до 8\n')
                n=0
        return n
    else:
        while n == 0:
            n = input(f'Введите положение {p} клетки по вертикали от 1 до 8\n')
            n = errorCheck(n)
            if (n > 8) or (n < 1):
                print('Ошибка ввода. Необходимо ввести цифру число от 1 до 8\n')
                n=0
        return n
def diag(n,m,i,k):
        k1=k
        i1=i
        while k1!=8 and i1!=8:
            i1=i1+1
            k1=k1+1
            if k1==m and i1==n:
                return 1
                
        k1=k
        i1=i
        while k1!=1 and i1!=1:
            i1=i1-1
            k1=k1-1
            if k1==m and i1==n:
                return 1
                
        k1=k
        i1=i
        while k1!=8 and i1!=1:
            i1=i1-1
            k1=k1+1
            if k1==m and i1==n:
                return 1
                
        k1=k
        i1=i
        while k1!=1 and i1!=8:
            i1=i1+1
            k1=k1-1
            if k1==m and i1==n:
                return 1
        return 0

k = Vvod(1, 1)
i = Vvod(2, 1)
m = Vvod(1, 2)
n = Vvod(2, 2)
print(f'Клетка 1: ({k},{i}); Клетка 2: ({m},{n})')
if ((i+k+m+n) % 2 == 0):
    print ('Клетки одинакового цвета\n')
    same=1
else:
    print('Клетки разных цветов\n')
    same=0
e=0
while e == 0:
    fig=int(input(""""Какая фигура находится на 1 клетке? Введите соответствующую цифру
              1 - ферзь
              2 - ладья
              3 - слон
              4 - конь\n"""))
    fig = errorCheck(fig)
    if (fig > 4) or (fig < 1):
        print('Ошибка ввода. Необходимо ввести цифру от 1 до 4\n')
        e=0
    else:
        e=1
res=0
attack=0
end=0
if fig == 1:
    if same == 1:
        attack = diag(n,m,i,k)
    if (attack==1 or i==n or k==m):
        print(f'Клетка 2 ({m},{n}) находится под ударом фигуры на клетке 1 ({k},{i})')
    else:
        print (f'Клетка, на которую перейдёт фигура, для атаки по клетке 2 ({m},{n}): ({m},{i})')
elif fig == 2:
    if i==n or k==m:
        print(f'Клетка 2 ({m},{n}) находится под ударом фигуры на клетке 1 ({k},{i})')
    else:
        print (f'Клетка, на которую перейдёт фигура, для атаки по клетке 2 ({m},{n}): ({m},{i})')
elif fig == 3:
    if same == 1:
        attack = diag(n,m,i,k)
        if attack == 0:
            i1=i
            k1=k
            while (k1!=1 and i1!=1) and res!=1:
                i1=i1-1
                k1=k1-1
                attack = diag(n,m,i1,k1)
                if attack == 1:
                    print(f'Клетка, на которую перейдёт фигура, для объявления атаки по клетке 2 ({m},{n}): ({k1},{i1})')
                    res=1
            i1=i
            k1=k
            while (k1!=8 and i1!=8) and res!=1:
                i1=i1+1
                k1=k1+1
                attack = diag(n,m,i1,k1)
                if attack == 1:
                    print(f'Клетка, на которую перейдёт фигура для объявления атаки по клетке 2 ({m},{n}): ({k1},{i1})')
                    res=1
            i1=i
            k1=k
            while (k1!=1 and i1!=8) and res!=1:
                i1=i1+1
                k1=k1-1
                attack = diag(n,m,i1,k1)
                if attack == 1:
                    print(f'Клетка, на которую перейдёт фигура для объявления атаки по клетке 2 ({m},{n}): ({k1},{i1})')
                    res=1
            i1=i
            k1=k
            while (k1!=8 and i1!=1) and res!=1:
                i1=i1-1
                k1=k1+1
                attack = diag(n,m,i1,k1)
                if attack == 1:
                    print(f'Клетка, на которую перейдёт фигура для объявления атаки по клетке 2 ({m},{n}): ({k1},{i1})')
                    res=1
        else:
            print (f'Клетка 2 ({m},{n}) находится под атакой фигуры на клетке 1 ({k},{i})\n')
    else:
        print(f'Клетка 2 ({k},{i}) не находится под атакой фиигуры на клетке 1 ({k},{i}) и не может быть под атакой через 1 ход')
elif fig == 4:
    if (((m-k)+(n-i)==3) or ((m-k)+(i-n)==3) or ((k-m)+(n-i)==3) or ((k-m)+(i-n)==3)) and m!=k and n!=i and (-2<=(m-k)<=2) and (-2<=(n-i)<=2):
        print(f'Клетка 2 ({m},{n}) находится под ударом фигуры на клетке 1 ({k},{i})')
    else:
        for q1 in range(1, 8):
            for q2 in range(1, 8):
                if (((q1-k)+(q2-i)==3) or ((q1-k)+(i-q2)==3) or ((k-q1)+(q2-i)==3) or ((k-q1)+(i-q2)==3)) and q1!=k and q2!=i and (-2<=(q1-k)<=2) and (-2<=(q2-i)<=2):
                    if (((m-q1)+(n-q2)==3) or ((m-q1)+(q2-n)==3) or ((q1-m)+(n-q2)==3) or ((q1-m)+(q2-n)==3)) and m!=q1 and n!=q2 and (-2<=(q1-m)<=2) and (-2<=(q2-n)<=2):
                        print(f'Клетка 2 ({m},{n}) будет находится под ударом фигуры на клетке 1 ({k},{i}) через 1 ход на клетку ({q1},{q2})')
                        end=1
                        break
            if end == 1:
                break
        if end == 0:
            print(f'Клетка 2 ({k},{i}) не находится под атакой фиигуры на клетке 1 ({k},{i}) и не может быть под атакой через 1 ход')