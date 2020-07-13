'''
안
!
안녕
안녕
요!
안녕하세요!안녕하세요!안녕하세요!
문자열함수
문자의 길이 : 6
문자의 개수 : 1
문자의 시작위치 : 0
문자의 시작위치 : -1
문자의 시작위치 : 5
문자 Replace : **하세요!
안-녕-하-세-요-!
['안', '녕', '하', '세', '요', '!']
<class 'list'>
'''

# 문자열 indexing

data ='안녕하세요!'

print(data[0])
print(data[-1])

# 문자열 slicing

print(data[0:2]) #0~1까지 마지막은 범위에 안들어감
print(data[:2]) #안녕
print(data[4:]) #요!

print(data*3) #안녕하세요!안녕하세요!안녕하세요!

print('문자열함수')
print('문자의 길이 :', len(data))
print('문자의 개수 :', data.count('안녕')) #Sting 클래스의 메소드 
print('문자의 시작위치 :', data.find('안녕'))
print('문자의 시작위치 :', data.find('.')) #못찾을 때 -1 반환
'''
print('문자의 시작위치 :', data.index('.')) # 못찾을 때 오류 발생 그래서 find 권장
'''
print('문자의 시작위치 :', data.find('!')) # !위치
print('문자 Replace :', data.replace('안녕', '**'))

datajn = '-'.join(data)
print(datajn)

datasp = data.split('-') #-로 분리
print(datasp)
print(type(datasp)) #split의 결과는 리스트!!!!!
