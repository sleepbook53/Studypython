#연산자 (기본적인 사칙연산)
a = 11
b = 4
print( a + b) #더하기
print( a - b) #빼기
print( a * b) #곱하기
print( a ** b)#제곱
print( a / b) #나누기
print( a // b) #정수나누기
print( a % b) #나머지

#문자열 연산
stat1 = 'Hellow'
stat2 = "World"
print(stat1 + stat2) #'+' 문자열 두 개를 합쳐줌
print(stat1, stat2) #',' 보이는대로 출력하기 위해 사용
res = stat1 + stat2
print(res)
res = stat1, stat2
print(res)

#문자열 연산에서는 +, *만 있음
print(stat1 + stat2)
#print(stat1 - stat2) 문자열엔 빼기 없음
print(stat1 * 5)
#print(stat1 * stat2)#문자열끼리 곱하기 없음
#print(stat1 /3) 문자열 나누기 없음

#문자열 길이
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

#문자열 인덱스, 리스트와 동일한 작업
print(stat3[0]) #안
print(stat3[1]) #녕
print(stat3[2]) #하
print(stat3[3]) #세
print(stat3[4]) #요
#print(stat3[5]) 예외발생
#인덱스는 0부터 시작, 개수 넘어가면 안됨

#stat3[0] = '저'
#stat3[1] = '리'
#print(stat3)
print(stat3[-1]) #요
print(stat3[-2]) #세
print(stat3[-3]) #하
print(stat3[-4]) #녕
print(stat3[-5]) #안

#문자열 자르기
current = '2022-01-17 14:39:25'
print(current[:4],'년')
print(current[5:7],'월')
print(current[8:10],'일')
print(current[11:13],'시')
print(current[14:16],'분')
print(current[17:],'초') 

print(current[-5:-3], '분')

# list_a = [1,2,3,4,5]
# list_a = a[1] = 19
# print(list_a) #리스트에서는 문자를 바꾸지 못한다고..

stat4 = '저리가' + stat3[3:]
print(stat4) #저리가세요

#문자열 포맷팅
str1 = "I'm so happy {0} U".format('to')
print(str1)
str1 = "I'm so happy {0} U. are {1}?" .format('to', 'you')
#{0}과 {1}의 숫자는 인덱스

frist = '투'
second = '유'
str1 = "I'm so happy {0} U. are {1}".format(frist, second)
print(str1)

#조금 더 편한 방법, 최신 포맷팅 앞에 'f' 써준다
str2 = f"I'm so happy {frist} U. are {second}"
print(str2)

money = 10000000000
print(format(money, ',d')) #1000단위마다 ',' 찍어달라는 것

from datetime import datetime
now = datetime.now() #현재시일
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math
mypi = math.pi
print(mypi)
print('{0}' .format(mypi))
print('{0:0.2f}' .format(mypi))
print(f'{mypi:0.2f}')


full_name = "In Kim"
age =30
greeting = f'''안녕하세요. 저는 {full_name}입니다.
나이는 {age:0.1f}살 이구요'''
print(greeting)

#split
#문자열을 maxsplit 횟수만큼 sep의 구분자를 기준으로
#문자열을 구분하여 잘라서 리스트로 만듦
part_name = full_name.split()
print(type(part_name)) #<class 'list'>
print(part_name) #['In', 'Kim']

test = 'Hey, guys'
print(test.split(','))

#| split
code = 'TEST|20220`|17|F145678'
split_codes = code.split('|')
print(split_codes)

#단어교체 replace
print(full_name.replace('In Kim', 'wang'))

#문자열 공백 제거, intrip(), rstrip(), strip() = Oracle TRIM과 동일
aaa = '      Hello World'
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())
print(full_name.index('I')) #0
print(full_name.index('n')) #1
print(full_name.index('K')) #3
print(full_name.index('i')) #4
print(full_name.index('m')) #5






