#기본 for 문

# arr = list=(range(1,100))      #[1, 2, 3, 4, 5]

# for  i in arr :
#     print(f'{i : 2.1f}')


#Tuple로 for문
# arr2 = ('me' , 'my', 'friend', 'jane')

# for item in arr2 :
#     print(f'{item : >10}')


#합계 for 문
# numbers  = list(range(1, 21, 2)) #1~20까지
# res = 0
# for item in numbers :
#     res += item
# print(f'{numbers[-1]} 까지의 총합은 {res}입니다')

#홀수 짝수 구문, 들어온 데이터에서 홀수나 짝수 구하기
from re import A


numbers  = list(range(1, 21)) #1~20까지

# for item in numbers :
#     if item % 2 == 0 : #짝수
#         print(f'{item}은 짝수')

# for item in numbers :
#     if item % 2 != 0  : #홀수
#        #혹은 if item % 1 == 0 : #홀수
#         print(f'{item}은 홀수')

#break, 13 이상이면 탈출(종료)
# for item in numbers :
#     if item > 12 :
#         break
#     if item % 2 == 0 : #짝수
#         print(f'{item}은 짝수') 

#continue, 해당 조건만 빼고 넘어감(계속)
for item in numbers :
    if item > 15 :
        continue
    if item % 2 == 0 : #짝수
        print(f'{item}은 짝수')

#구구단 구현
print('구구단 프로그램')
print('')
for i in range(2, 10): #2부터 9까지니까
    print(f'{i}단 시작')
    for j in range(1, 10): #1부터 9까지니까
        print(f'{i} x {j} = {i*j:2d}', end='   ') #2d =결과값이 두 자리로 표시됨
    print(' ') #== print() / 그냥 엔터, 공백 같은 것
#하나하나 확인해나가면서 작업


#inline for 문
a = [1, 2, 3, 4]
result = [i *3 for i in a]
print(result)

#기존 for 문
t = [] 
for i in a:
        t.append(i *3)
print(t)
