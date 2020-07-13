'''
딕셔너리
'''

#key값으로 접근

dt = {'a':10, 'b':20}
print(dt['a'])
#추가
dt['c']=100
print(dt)
#수정
dt['c']=10
print(dt)


#삭제
# del dt['a']
# dt.pop('c')
# print(dt)

print("="*30)


for item in dt:
    print(item)

for item in dt:
    print(item, '=>', dt[item])

keys = list(dt.keys()) #keys만 추출
print(keys)
values = list(dt.values()) #값만 추출
print(values)
items = list(dt.items()) #아이템 추출
print(items)

for key,value in dt.items(): #튜플, items 메소드로 쌍으로 값 반환, 자주 씀
    print(key,'=>', value)

lst1 = ['x','y','z']
lst2 = [10,20,30]

dt = zip(lst1, lst2) #<zip object at 0x0000023005512C40>
print(dt)

dt = dict(zip(lst1, lst2)) #딕셔너리화, 키, 값으로 참조 가능, items로 참조
print(dt)
for x,y in dt.items():
    print(x, ':', y)

dt1 = list(zip(lst1, lst2)) #리스트, 튜플의 쌍으로 반환
print(dt1)
for x,y in dt1:
    print(x, ',', y)
