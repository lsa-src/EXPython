'''
파일처리
'''

#파일 열기
fp = open('지역평균기온.txt', 'r', encoding='utf-8') #한글 때문에 인코딩 추가
data = fp.read() #객체생성하여 파일 넘김

#파일 닫기
fp.close()
print(data)
print(type(data))

#문자열 처리, 한줄씩 자르자!
lines = data.split('\n')
print(type(lines))
print(lines)

for line in lines :
    item = line.split(",")
#    print (item)
    print (item[0], "=>", item[1])

for line in lines :
    print (line.replace(",", "=>")) #replece는 객체에 반영 안됨

# 평균기온 구해보자
temp = [] # 기온만 담을 임시 객체 생성!!!! 
for line in lines :
    item = line.split(",")
    print(item[0], '=>', item[1])
    temp.append(int(item[1]))

print(f'평균기온 : {sum(temp) /len(temp):0.2f}')



