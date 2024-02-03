'''
1부터 100사이의 모든 정수중에서 7의 배수만 출력하세요
'''
i = 1

while i <= 100:
    # res = i % 7
    if not(i % 7):print(i)
    i += 1
        
print('탈출')
        
        