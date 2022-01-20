#커서 접근 코드 함수로 작성
import cx_Oracle as ora

def myconn() : #되도록 함수 선언은 메인함수 위에

    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user ='scott', password='tiger', dsn =dsn, encoding='utf-8')
    return conn

def getAllData(conn) : #conn객체를 매개 변수 받아서 쿼리를 실항할 함수
    cur = conn.cursor() #커서 생성
    query = 'SELECT * FROM emp' #emp테이블에서 데이터를 모두 가져와라
    for row in cur.execute(query) : #emp 최상단에 커서가 위치하면서 모든 데이터를
        print(row) #한 줄 씩 출력

#두 번째 무언가 활동을 위한 함수 지정
# def getNamdAndJobeData(conn):
#     cur =conn.cursor()
#     query = 'SELECT ename, job FROM emp' #emp 테이블, ename, job
#     for row in cur.execute(query) :
#             print(row)

#세 번째. 두번째와 같은데 다르게 쓰기
def getNamdAndJobeData(conn):
    cur =conn.cursor()
    query = 'SELECT ename, job FROM emp' #emp 테이블, ename, job
    cur.execute(query) #실행
    while True :
        row = cur.fetchone() #한 row(레코드) 읽기 함수
        if row is None :
            break
        else :
            print(row)

#네 번째, 특정 정보 하나 받기
# def getDaptName(conn, no) : #튜플로 받기
#     cur = conn.cursor()
#     query = f'SELECT * FROM dept WHERE deptno = {no}' #DB는 1부터 시작함
#     cur.execute(query)
#     row = cur.fetchone()
#     print(row)

#다섯 번째, 정보 두 개받기
# def getDaptName(conn, no, loc) : #튜플로 받기
#     cur = conn.cursor()
#     query = f'SELECT * FROM dept WHERE deptno = {no} AND loc = \'{loc}\''
#     cur.execute(query)
#     row = cur.fetchone()
#     print(row)



#여섯 번째, 파라미터 변수 최소화, 튜플쓰기
# def getDaptName(conn, tup) : #튜플로 받기
#     cur = conn.cursor()
#     query = f'SELECT * FROM dept WHERE deptno = {tup[0]} AND loc = \'{tup[1]}\''
#     cur.execute(query)
#     row = cur.fetchone()

#     print(row)

def getDaptName(conn, tup) : #튜플로 받기
    cur = conn.cursor()
    query = 'SELECT * FROM dept WHERE deptno = :1 AND loc = :2'
     # = : n을 쓰는 이유, 문법 ( 1에 1 2에 2가 될 수 있게 아니면 출력 값이 고정됨)
     #: 는 인자값
    cur.execute(query,tup)
    row = cur.fetchone()

    print(row)

if __name__ == '__main__' : #언더바 2개씩. 엠트리 포인트
    print('프로그램 시작') #메인함수: 주가되는 함수에 대한 묶음(이 안에 쭈욱 포함)
    #함수 호출
    scott_con= myconn() #dsn, connect() 후 접속객체 conn 리턴

    print('emp 테이블 전체 조회 (SELECT *)')
    getAllData(scott_con)
    print('emp 2개 컬럼 조회')
    getNamdAndJobeData(scott_con)
    no = input('1.검색할 부서 번호를 입력하세요')
    loc = input('2. 지역명을 입력하세요').upper()
    tup =(no, loc)
    # print(f'{no}번호의 부서명, 지역: {loc}') #다섯번째 사례까지는 사용해야함
    #여섯 번째에서는 upper을  위 처럼 써야함
    getDaptName(scott_con, tup) #upper: 소문자로 적어도 대문자로 나옴
    #해당 테이블은 지역명이 다 대문자로 되어 있는 상황
print('프로그램 종료')
