'''
중첩 while
'''

# 구구단 출력
i = 2   # 2단부터 ===> 9단까지
while i<=9:
    print(f'== {i} 단 ==')
    j = 1
    while j <= 9:
        print(f'{i} x {j} = {i*j}')
        j += 1
    
    
    i += 1
    print()
    
    