#While 문
from ast import While


hit = 0

while hit < 10 : #이 값이 참인 동안
    hit = hit + 1  #hit +=1
    print(f'나무를 {hit}번 찍습니다.')
    if hit == 10:
        print('나무가 넘어갑니다')
        break
print('나무찍기를 마칩니다')

#For로 하면?
for hit in range(1, 11) :
    if hit > 9:
        break
    print(f'나무를 {hit}번 찍습니다')
