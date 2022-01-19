#random 함수
#import random #같은 방식 아래


from random import *

# print (random.choice(range(1, 7))) #주사위

#lottorey
numbers = list(range(1,46))
print(numbers)
lottorey = [] #list()  이렇게 해도 됨

for i in range(6) :
    lottorey.append(choice(numbers))#lottorey.append(random.choice(numbers))

print(lottorey)