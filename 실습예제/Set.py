'''
집합 set, 자료형으로 쓰기 보단 데이터 처리용으로 많이 사용, 데이터 중복없이 하나만 필요할 때..좀 더 프로그램을 편하게 하고자 할 때
컬렉션 데이터 타입은 for in
파이썬은 사람의 마인드와 유사...
'''

lst = [1,2,3]
st = {1,2,4}

print(type(lst))
print(type(st))

print(lst[0])
# print(st[0])
# print(st[0]), TypeError: 'set' object is not subscriptable, set은 인덱싱이 안됨 순서가 없음

lst1 = [1,2,2,2,3,3]
st1 = set(lst1) #중복 데이터 제거, 리스트를 set으로 변환하는 편한 방법
lst2 = list(st1)
print(type(st1))
print(type(lst2))
print(st1)
print(lst2)

st2 = {1,3,4,5,10}
print("교집합 :", st1&st2)
print("합집합 :", st1|st2)
print("차집합 :", st1-st2)

print('-'*50)
print(sorted(st2)) #메소드가 아니라 콜렉션 함수당 리턴값은 정렬된 값 반환, 원본자료는 바뀌진 않는다.

sortedLst = sorted(st2) #반환값을 sortedLst에 저장
print(sortedLst)
