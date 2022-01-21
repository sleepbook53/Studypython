#Person.py
#person 클래스
from asyncio.proactor_events import _ProactorSocketTransport
from email.errors import MalformedHeaderDefect
from xml.dom import EMPTY_NAMESPACE


class person :
    name ='무명이' #아직 이름이 없다
    age = 0
    height = 0
    gender = ''
    footsize = 250
    bloodtype  = ''


    #생성자
    def __init__(self,name, age) -> None:  #-> None: 리턴값이 없다는 말 '->' 리턴값 명시. 생략가능
        #__init__() = person() 이런 상황
        self.name = name
        self.age = age
        print('person이 생성되었습니다.')


    def introduce(self):
        greeting = f'''안녕하세요. 저는 {self.name}입니다
        {self.gender}이구요. {self.age}입니다'''

        print(greeting)

    def eat(self, food) :
        print(f'{self.name}이(가) {food}(을)를 먹는다')
    def drink(self, drink):
        print(f'{self.name}이(가) {drink}(을)를 마시면서 일한다')


if __name__ == '__main__':
    # p = person() #p라는 이름의 Person 객체생성
    # print(type(p))
    # print(id(p)) #id 값

    # p2 = person() #p2의 객체 생성
    # print(type(p2))
    # print(id(p2))
   
    hgd = person('홍길동', 14)
    # hgd.age = 30
    hgd.height =175
    hgd.gender = 'male'
    hgd.foodsize=240
    hgd.bloodtype='Rh+B'

    hgd.introduce()        
    hgd.eat('본죽')
    hgd.drink('hottody')
    
    
