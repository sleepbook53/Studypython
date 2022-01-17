#리스트 연산
arr = list(range(5))#0부터 5까지
print(arr)
arr = list(range(1, 6)) #1부터 5까지
print(arr)

arr= list(range(2, 101, 2)) #2부터 100까지 2배수
print(arr)
print(arr[0] + arr[5]) #더하기도 가능

#2차원 배열(리스트)
arr2 = [1, 2, ['HI', 'My', 'Friend']]
print(arr2[0]) #1
print(arr2[2]) #['HI', 'My', 'Friend']
print(arr2[2][1]) #2번째의 index 1번째 배열 값: My
print(arr2[2][1][0]) #2번째의 index 1번째 배열의 0번째 배열 값: M

arr3 = list(range(1,4))
print(arr3)
print(arr3*3) # 3번 반복
#print(arr3 + 3) 이건 안됨
print(arr3 + arr) #이건 됨
print(len(arr))

#list funtipn
print('-- 리스트 내장함수--')
del(arr3[1]) #특정 인덱스값을 지워라
print(arr3)

arr3.remove(1) #특정 값을 지워라
print(arr3)

arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3)#값을 찾아서 최초의 값만 지움. 없으면 에러
print(arr4) 
del(arr4[4])#3번째 인덱스 삭제
print(arr4) 

arr4.sort() #오름차순
print(arr4)

arr4.reverse() #내림차순
print(arr4)

arr4.insert(2, 10) #인덱스 값과 내가 넣을 값을 함께 넣는 것
print(arr4)

arr4[0] =100
print(arr4)

#Tuple

tup1 = tuple(range(1, 6))
print(tup1)
print(tup1[3])

# tupl[0] = 99
# print(tupl)  #값을 할당 할 수 없음. 바꿀 수 없음. 리무브 등 안됨.

#딕셔너리. 새로 갱신 및 수정 등 가능
dicl = {1 : 'a'}
dicl[2] = 'b'
print(dicl)

dicl ['name'] = 'Hugo'
print(dicl)

#딕셔너리 지우기
del dicl['name']
print(dicl)

#딕셔너리 연산자
print(dicl.keys()) #dict_keys([1, 2])
print(dicl.values()) #dict_values(['a', 'b'])
print(dicl.items()) #dict_items([(1, 'a'), (2, 'b')])

#리스트를 튜플 변환
print('-- 리스트/튜플 변환--')
print(arr4)
tup2 = tuple(arr4)
print(tup2) #튜플이라 값 수정 안됨

arr5 = list(tup1)
print(arr5) #튜플을 리스트로 

arr5.append(5)
print(arr5)
tup1 =tuple(arr5)
print(tup1)
