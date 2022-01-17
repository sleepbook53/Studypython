#자료형
print(None)
print(type(None))
print(0 == None)
a = None
print(a)
print(type(a))

#숫자형
금액 = 12_315_666
print(금액) #단위수를 끊어서 가능 그러나 출력값엔 영향 x 

#문자열형
bruce_eckel = "Life is short, You need Python"
print(bruce_eckel)

bruce_eckel = "Life is short, \nYou need Python"
#/n=탈출문자 : newline, 새로운 줄로 만들겠다
print(bruce_eckel)
bruce_eckel = "Life is short, \\You need Python"
print(bruce_eckel)
#\\ \를 출력하고 싶을 때
bruce_eckel = '''Life is short,
You need Python
난 필요 없는데 '''
print(bruce_eckel)
#줄을 바꿔서 표현하고 싶을 때, ''' 사용./n 필요 없음

#불형
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 999)
#print(val_sum = 10) 이렇게는 안됨

bl_true = True
print(bl_true) #True
print(type(bl_true)) #class 'bool'
print(bl_true == (True)) #True
print(bl_true is True) #True
print(a is None) #True
print(val_sum is 1000) #True

#의미가 있는 bool
print(bool(1)) #True
print(bool(0)) #False

#list , 기반 데이터
b = [1,2,3,4,5,6,7,8,9,10]
print(b)

arr2 = ['Life' , 'is', 'short', 'you', 'need', 'python', 3]
print(arr2)

arr3 = [[1,2,3], [4,5,6]] #행렬배열
print(arr3)

# 빈 리스트 ≠None
arr4 = list()
print(arr4)

#튜플1
tuple = (1, 2, 3, 4, 5)
print(tuple)

#딕셔너리
spitherman = {'name' : '피터 파커'
             , 'age' : 18
             , 'weampon' : 'web shooter'}
print(spitherman)
print(type(spitherman))

#집합 set, 요소의 중법을 허용하지 않음
set_int = set([1, 2, 3, 4, 5, 6, 7, 1, 2, 2])
print(set_int)



