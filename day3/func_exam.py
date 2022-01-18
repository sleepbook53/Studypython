#Function 함수 선언 및 사용

#더하기 함수 선언
def add(a, b) :
    res = a + b

    return res 

# #함수 사용
print(add(24786, 4324))

mid_val = add(3, 4)
print(mid_val * 3)

#함수종류
#매개변수(입력값)가 없는 형태
def say_hello():
    return "hello~"
print(say_hello(), 'my friend')

val = say_hello()
print(val.replace('o~' , ''))

#결과값이 없는 형태
def say_hello(name) :
    print(f'Hello~ {name}')

say_hello('hogo') #리턴 없는 방법, return  None과 같은 의미(생략)

## 둘 다 없는 경우
def say_goodbye() :
    print('Bye bye')

say_goodbye()

#매개 변수 지정
def multi(a, b) :
    return a * b
print(multi(2, 9))
print(multi(8, 9))

#매개 변수 개수가 가변적일 때
def plus(*args) :
    res = 0
    for i in args :
        res += i

    return res
print(plus(1))
print(plus(1, 2, 3))
print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(plus())

#함수 결과가 하나 이상인 경우 (최근 업데이트) . 리턴값 두 개 이쌍
    #튜퓰을 사용하는 이유
def mul_and_div(x, y) :
    mul = x * y
    div = x / y

    return (mul, div) #튜플
(res1, res2) = mul_and_div(7, 8)
print(res1, res2)

def 사칙연산(x, y) :
    return(x+y, x-y, x*y, x/y)
res1, res2, res3, res4 = 사칙연산(9,5)
print(res1, res2, res3, res4)
print(type(사칙연산(1,2)))

#함수와 변수의 라이프 스코프

