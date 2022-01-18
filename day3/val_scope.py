#변수 라이프스코프

from re import X


a = 10 #매개변수, 전역변수

def vartest(a) : #매개변수, 지역 변수. 함수 내에서만 활용
    a = a + 1
    return a 
a = vartest(a)
print(a)

def vartest(x) :
    y = x + 1
    return y
res = vartest(a)
print(res)
