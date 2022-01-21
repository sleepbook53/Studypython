#book rental shop
# table : divtbl, membetbl
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def getAllDataFromDivtbl(conn) :
    cur = conn.cursor()
    query = 'SELECT * FROM divtbl'
    for row in cur.execute(query) :
        print(row)

# def setDataIntoDvitbl(conn, tup):
#     cur =conn.cursor()
#     query = '''INSERT INTO divtbl (division, names)
#                 VALUES (:1, :2)'''
#     cur.execute(query,tup)
#     cur.close()
#     conn.commit() #COMMIT ; 필수 !

#membertbl에서 일부 데이터 가져오기   
# def getSomeDataFrommembertbl(conn):
#     cur = conn.cursor()
#     query = '''SELECT names, levels, addr, mobile, email 
#                 FROM membertbl
#                WHERE addr LIKE '서울%'
#                  AND UPPER(email) LIKE '%@NAVER.COM'
#                ORDER BY idx DESC'''
#     for row in cur.execute(query) :
#         print(row)
#     cur.close()

 # membertbl에 신규회원 입력하기
# def setNewMemberIntoMembertbl(conn,tup):
#     cur = conn.cursor()
#     query = '''SELECT ROWNUM, idx
#                 FROM (
#                     SELECT idx FROM membertbl
#                     ORDER BY idx DESC  
#                              ) 
#                 WHERE ROWNUM = 1''' #인덱스 삽입
#     cur.execute(query)
    
#     idx = cur.fetchone()[1]
#     if idx is None:
#         idx = 0
#     else :
#             idx = idx[1]
#      #예외 방지를 위한 구문(if 쪽)       
#     intup = (idx+1, tup[0], tup[1], tup[2], tup[3])
#     query = '''INSERT INTO membertbl
#                      (idx, names, levels, userid, password)
#                VALUES (:1, :2, :3, :4, :5)''' #나머니 불러오기
   
#     cur.execute(query,intup)
#     cur.close()
#     conn.commit()


#회원정보 수정
# def setChangeMemberFrommembertbl(conn, tup):
#     cur = conn.cursor()
#     query = '''UPDATE membertbl
#                   SET addr = :1
#                   , mobile = :2
#                    , email = :3
#                  WHERE idx = :4'''
#     cur.execute(query, tup)
#     cur.close()
#     conn.commit()

#장르 삭제
def deleteDivision(conn, division) :
    cur = conn.cursor()
    query = 'DELETE FROM divtbl WHERE division = :1'
    cur.execute(query, (division,)) #데이터가 하나면 튜플로 변경
    #,를 반드시 넣어줘야함
    cur.close()
    conn.commit()



if __name__ == '__main__' :
    print('책대여점 프로그램 시작')
    scott_con = myconn() #DB접속
    #1. divtbl에서 데이터 조회
    print('책 장르 정보조회')
    # getAllDataFromDivtbl(scott_con)
    
    #2. divtbl에서 새 데이터 입력
    # print('책 장르 정보입력')
    # division = input('구분 코드 입력:')
    # names = input('장르명 입력:')
    # tup = (division, names)
    # setDataIntoDvitbl(scott_con, tup)
    # print('정보 입력 성공')

    #3. membertbl에서 데이터 조회
    # getSomeDataFrommembertbl(scott_con)
    
    #4. membertbl에 새 데이터 입력
    # print('신규 회원 입력')
    # names = input('회원 이름 입력: ')
    # levels =input('레벨 입력(a~d)까지:')
    # userid =input('아이디 입력(최대 20자): ')
    # password = input('패스워드 입력(최대 20자): ')
    # tup = (names, levels, userid, password)
    # setNewMemberIntoMembertbl(scott_con, tup) 

    # #5. membertbl에 새 데이터 수정
    # print('기존회원 수정')
    # idx = input('변경회원 번호 : ')
    # addr = input('주소 입력: ')
    # mobile = input('폰 번호 입력(-포함): ')
    # email = input('이메일 입력: ')
    # tup = (addr, mobile, email, idx) #나오는 순서가 달라서 위랑 순서 다름
    # setChangeMemberFrommembertbl(scott_con, tup)
    # print('기존회원 수정완료')

    #6. divtbl에 임의 데이터 삭제
    print('divisoin 장르 정보 삭제')
    division = input('삭제할 장르 코드 입력')
    deleteDivision(scott_con,division)
    print('삭제 완료')



