'''
BMI=체중(KG)/키(m)x키(m)
'''

x = float(input ('키를 입력하시오')) / 100
y = float(input ('체중을 입력하시오'))

print('BMI', end='=')
print({y/(x*x):0.2})

weight = float(input('몸무게(kg):'))
height = float(input('키(cm)'))/100

BMI = weight/height**2
print(f'몸무게{weight}kg, 키{height*100}cm => BMI :{BMI :0.2f}')
