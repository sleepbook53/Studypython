#mycar

from vehicle import Car
if __name__ =='__main__':
    mycar = Car('오오오오', '파랑')
    # mycar.색상 = '파랑'
    mycar.연로 = '가솔린'
    mycar.제조사= '현대기아'
    mycar.출고년도 = 1998
    # mycar.차량번호 = '22나 4212'
    


    # print(mycar.__제조사)
    # print(mycar.연료)
    # print(mycar.기어단수)
    mycar.제조사입력()
    mycar.제조사('쌍용')

    mycar.전진한다(2)
    print(mycar)
    
    