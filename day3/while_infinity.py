#While 무한루프
val = 0

while True :
    print('''작업할 번호를 입력하세요.
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료
숫자입력 : ''', end ='')
    val = int(input()) #입력
    
    if val == 1:
        print("회원입력")
    elif val ==2 :
        print("회원검색")
    elif val ==3 :
        print("회원수정")
    elif val ==4 :
        print("회원삭제")
    elif val ==5 :
        print("종료")
    elif val ==6 : 
        break
    else :
        print('1~6사이의 수를 입력하세요')
        continue