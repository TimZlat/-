a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# условие пустоты
f1 = (a1<a2 and b1<a2) or (a2<a1 and b2<a1)

if f1:
    print('пустое множество')
else:
# условия отрезков
    if (a1 < a2 < b2 <= b1):
        print (a2,b2)
    elif (a1 <= a2 < b1 < b2):
        print(a2,b1)
    elif (a2 <= a1 < b2 < b1):
        print(a1, b2)
    elif (a1 == a2 and b1 == b2):
        print(a1,b1)
    elif (a2<a1<b1<=b2):
        print(a1,b1)
# условия точек
    else:
        if(a1<b2 and a2 == b1 and b1<b2):
             print(a2)
        elif (a2<b1 and b2 == a1):
             print(b2)
        elif (a1 == a2 and a2<b1 and b1<b2 or b2<b1):
             print(a1)
        elif (a2<a1 and a2<b1 and b1 == b2 or a1<a2):
             print(b1)
