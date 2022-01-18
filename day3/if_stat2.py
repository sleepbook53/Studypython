# 종합 if
x = -10

if x > 0 :
    print('양수')
    if x > 5 :   #중복if 문
         print('10보다 큰 수')
    else :
        print('10보다 작은 수')
elif x == 0 :
    print(0)
else :
    print('음수')