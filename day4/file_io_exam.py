#file입출력

#파일 출력
# f = open('newfile.txt', 'w')
# f.close() #클로즈 안하면 과부화될 수 있음

# 특정경로에 파일 생성
# f = open('C:/Sources/Sample/test2.txt', 'w')
# f.close()
# print('파일이 생성되었습니다')


#newfile.txt 파일입력(일어오기)
f = open('newfile.txt', 'r', encoding ='utf-8')
# # while True :
# #     line = f.readline()
# #     if not line :
# #             break

# #     print(line)
# # f.close()

# lines = f.readlines()
# for line in lines :
#     print(line)
# f.close()

for line in f:
    print(line.replace('\n', ''))
f.close()