#변수
#파이썬의 변수에 제약은 거의 없다
a = '헬로우'
print(a)

a= 3.141592
print(a)

a = 10
print(a)

a= 99999999999999999999999
print(a)

a = 1/10
print(a)

#변수 지정(할당) = assign 방법
#left var: 값을 할당받는 것, right var 값을 지정하는 것

a = 3  #3 ≠ a
b = 3.141592
c = 'python'
d = (1, 2, 3) #튜플
e = [1, 2, 3, 4] #리스트
f = [7, '8', '$', a] #파이썬의 장점

#변수명
var = 10 
var2 = 20
var4 = 10
#4var = 50 숫자먼저 안됨(중간은 가능)
#~var = 60 특수문자 먼저 안됨
var_of_change = 20 
chain_reactipn = 100
#var- = 111 다른 특수문자 안됨
#var$ = 999 다른 특수문자 안됨
var_ = 222 #_는 가능
Var_ = 22222
print(var_)
print(Var_)
MyAcountOfBank = 1
은행계좌금액 = 1
print(id(var_)) #id = 고유식별값 확인
print(id(Var_))
#변수타입 확인. 파이썬은 타입 지정 문법이 없어서 확인이 필요
print(type(var_)) #int
print(type(b))#float
print(type(c))#str
print(type(d))#tuple
print(type(e))#list
print(type(f))#list