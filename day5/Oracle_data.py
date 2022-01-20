from dataclasses import dataclass


#Oracle data
#cx_oracle 설치 : pip install cx_oracle

import cx_Oracle as ora

#makedsn('호스트명'/'ip주소',protnum, service_name)
dsn = ora.makedsn('localhost', 1521, service_name='orcl' )
#connect(user, password, dsn, encoding)
conn = ora.connect(user='scott', password='tiger', dsn=dsn , encoding='utf-8') 

cur = conn.cursor() #커서 만듦

# for row in cur.execute('SELECT * FROM emp') :
    # print(row)
#cur.execute('SELECT COUNT(*) FROM emp')
# result = cur.fetchone()
# print(result)

#cur.close() #커서 닫고
#conn.close() #접속 닫음

#엑셀 []. 리스트 오라클 (). 튜플로 기본으로 넘어옴


#try문 응용
# try :
#     for row in cur.execute('SELECT * FROM emp;') :
# #라이브러리 등으로 불러온 경우 ; 쓰면 예외가 발생할 수 있음
#         print(row)
# except ora.DatabaseError as e :
#     print(f'쿼리문이 잘못되었습니다. n번 라인 확인요 : {e}')
# finally :
#     cur.close() #커서 닫고
#     conn.close() #접속 닫음



cur.execute('SELECT COUNT(*), \'sample\' From emp')
result = cur.fetchone()
print(result) #개수 확인
