#exception.handle.py
#예외처리  매우 중요

from logging import exception


def add(a, b) :
    return a + b
    
def minus(a, b) :
    return a - b
    
def multi(a, b) :
    return a * b
    
def divide(a, b) :
    return a / b

print('사칙연산 시작')
a, b = 4, 1
numbers = [3, 6, 9] #리스트 생성
try :
    print(f'나누기 결과 : {divide(a, b)}')
    res= int(numbers[3]) *8
    num= int(input('수를 입력하세요'))

except ZeroDivisionError as e:
    print(f'예외발생 . 추가처리1{e}')
except IndexError as e:
     print(f'예외발생 추가처리2 {e}')
except ValueError as e :
    print(f'제발 숫자만 넣으라고{e}')
except Exception as e:
     print(f'예외발생 알 수 없는 예외 추가처리5{e}')

finally :
    print(f'곱하기 결과 : {multi(a, b)}')
    print(f'빼 기 결과 : {minus(a, b)}') 
    print(f'더하기 결과 : {add(a, b)}')

#exception 여러가지로 나뉘는 이우: 상황에 따라 정확한 예외처리를 하기위해
#정 모르겠다면 Eception 하나만 해도 됨
#try에 모든걸 넣지 않는 이유. 예외 발생시 그 안에 있는 것 상황 종료
    #예외발생 코드에만 try에 집어넣어야함
#finlly: 무조건 처리해야 하는 것(없어도 되긴 함)
#try - except에서 예외가 발상하면 몇 천 배 느려짐


print('사칙연산 종료')
