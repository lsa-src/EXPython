#한문자씩 접근
data = '안녕하세요!'

for ch in data : 
    print(ch)

corona = '''코로나(corona)는 라틴말로 왕관을 뜻하며 통상 태양을 둘러싼 외곽의 빛(광환)을 지칭한다. 
코로나바이러스라는 이름은 전자현미경으로 이 바이러스를 관찰했을 때 마치 코로나와 유사한 모양을 띠어 붙여진 이름이다. 
이번에 중국의 우환에서 시작된 코로나바이러스는 2019년에 발견된 새로운 코로나바이러스라는 뜻으로 2019-nCoV로 붙여졌다.
nCoV는 novel(새로운) CoV(코로나바이러스)라는 뜻이다.'''

print(corona)

word = input('찾고자하는 단어를 입력하시오 : ')
print(f'{word}는 {corona.count(word)}번 나옴')

word = input('찾고자하는 단어를 입력하시오 : ')
print(f'{word}는 {corona.count(word)}번 나옴')

sentence = corona.split('\n')
print(sentence)

sentence = sentence.replace('\n', '')
sentence = corona.split('.')
print(sentence)

for st in sentence:
    print (st)
    
    
corona.replace('\n', '')
print(corona)

sentence = corona.split('.')

for st in sentence:
    print(st)
