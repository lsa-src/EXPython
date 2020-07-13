'''
리스트와 튜플
'''
lst = [2,5,3,1,5]
print('리스트 요소의 개수:', len(lst))
print('리스트 5요소의 개수:', lst.count(5))
print('리스트 5요소의 위치:', lst.index(5))
lst.sort()
print('리스트정렬:', lst) #replace와 비교, 정렬과 동시에 값이 변함
lst.sort(reverse=True)
print('리스트 역정렬 :', lst)

x, y = 10, 20
print(x, y)

x1, y1, z1=(1,2,3) #튜플의 각각의 변수에 값을 넣을 수 있다. 딕셔너리의 아이템즈는 튜플로 반환됨 개념 이해 요망
print(x1, y1, z1)             #반환되는 값을 추출하여 각각의 값을 활용 가능

lst = [2,5,3,1,5]

for item in lst:
    print(item)
print("="*30)
