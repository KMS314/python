cnum = input('차량번호를 입력하세요 >>> ')

enum = int(cnum[-1])

hjnum = enum % 2

result = '운행불가' if hjnum else '운행가능'

print(f'차량번호{cnum}은 오늘 {result}입니다') 

