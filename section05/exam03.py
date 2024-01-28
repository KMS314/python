'''
3개의 정수를 입력받아서 그 중에서 가장 큰 수를 출력하세요
'''

num1 = int(input('첫번째 정수를 입력하세요'))
num2 = int(input('두번째 정수를 입력하세요'))
num3 = int(input('세번째 정수를 입력하세요'))

hnum = num1

if hnum<=num2:
    hnum = num2
elif hnum<=num3:
    hnum = num3
    
print(f'가장 큰 수는 {hnum}입니다')