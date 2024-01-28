'''
기본적인 출력문
'''

print('test1','test2','test3')  # 기본적인 출력문으로, 구분하여 출력할 내용을 적음
print('test1','test2','test3', sep = '-')   # 출력 내용을 'sep'으로 지정된 문자로 구분
print('test1','test2','test3', sep = '===')
print('test1','test2','test3', sep = ' , ')
print() # 줄바꿈
print('\n')
# end : 출력내용 가장 뒤에 붙을 출력 문자, 기본값은 '\n'
print('test1','test2','test3', sep = ',', end = '\n')
print('test1','test2','test3', sep = ',', end = '\t')
print('test1','test2','test3', sep = ',')

# 형식을 갖는 문자열
# 포맷 연산자 % 를 이용한 문자열 만들기
# 문자열 객체의 format() 메소드 이용하기
# f-string 객체를 이용하여 문자열 만들기

print( '%d'%10 )
print( '%d %x'%(10,15) )

print('제 나이는 %d살이고 키는 %f 입니다'%(10,170), '몸무게는 %f입니다'%80, sep = ' === ')
print('원주율은 %f 입니다'%3.14)
print('제 이름은 %s입니다'%'ostin')
print('원주율은 %s 입니다'%3.14)

# %d : 데이터를 정수로 표현
# %o : 데이터를 8진수로 변환하여 표현
# %x : 데이터를 16진수로 변환하여 표현 (0~9,a,b,c,d,e,f,...)
# %f : 데이터를 실수형식으로 표현
# %s : 데이터를 문자열 형식으로 표현

print('========================================')
print('%5d'%1, '%5d'%2)
print('%-5d'%1, '%-5d'%2)
print('%5.2f'%3.14) # 소수점 포함하여 5자리를 확보하고 그 이하를 2자리로 만들어준다.
print('%-5.2f'%3.143416758964362)
print('%.5f'%3.1435198023905364)
print('========================================')
print('제 나이는 {}살이고 키는 {}입니다'.format(10,170))
print('제 나이는 {1}살이고 키는 {0}입니다'.format(10,170))

print('========================================')
# f-string
age = 10
height = 170
print('제 나이는 10살이고 키는 170입니다')
print(f'제 나이는 {age}살이고 키는 {height}입니다')

age = 20
height = 180
print(f'제 나이는 {age}살이고 키는 {height}입니다')

# 입력문
myData = input('프롬프트 : 데이터를 입력해주세요 >>> ')
print(f'입력하신 내용은 {myData} 입니다')

float() # 실수형으로 변환
pi = str(3.14) # 문자열형으로 변환
num1 = int(input('첫번째 숫자를 입력해주세요 >>> '))
num2 = int(input('두번째 숫자를 입력해주세요 >>> '))
num3 =  num1 + num2
print(f'{num1} + {num2} = {num3}')
print(f'{num1} + {num2} = {num1 + num2}')   # 간단한 수식을 {}내에 사용할 수 있다.
