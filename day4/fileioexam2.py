#파일 쓰기


# f = open('write_file', 'w', encoding='utf-8')

# f.write('저는 한국 사람입니다.\n')

# texts = ['저는 한국사람이죠\n', '이번에 2022년이 되었습니다.\n']
# f.writelines(texts)

# f.close()

# f = open('writeline.txt', 'a' , encoding='utf-8')
# f.write('내용 추가할게요!')
# f.close()

f = open('write_file', 'r', encoding='utf-8')

for line in f:
        print(line)
f.close()