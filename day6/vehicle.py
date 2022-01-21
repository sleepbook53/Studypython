#vehicle
class Car :
    차량번호 ='dd'
    제조사 = 'dd'
    색상 = 'dd'
    연로 = 'dd'
    출고년도 = 'dd'
 
    def __init__(self, 차량번호, 색상) -> None:
        self.차량번호 = 차량번호
        self.색상 = 색상

    def __str__(self) -> str:
        return f'제 차는 {self.출고년도}에 만들어진 {self.제조사}차 입니다'

    #private
    def 제조사입력(self, 제조사) :
        self.__제조사 = 제조사

    def 제조사확인(self):
        print(f'제조사{self.__제조사}') #프라이빗임 __제조사
    

    def 전진한다(self,leval):
        print(f'{self.색상}차가 {leval}단으로 전진')

    def 후진한다(self):
        print('후진')

    def 좌회전한다(self):
        print('좌회전')

    def 우회전한다(self):
        print('우회전')

    def 정지한다(self):
        print('정지')
    