# 1. 시험점수를 입력받아서...
# 90~99 : A
# 80~89 : B
# 70~79 : C
# 60~69 : D
# 그 외에는 F를 출력하세요

#  점수를 입력하세요 >>> 90
#  점수는 90점이고, 학점은 A학점입니다.

p = int(input('점수를 입력하세요 >>> '))

grade = 'F'
if p >= 90:
    grade = 'A'
elif p >= 80:
    grade = 'B'
elif p >= 70:
    grade = 'C'
elif p >= 60:
    grade = 'D'

print(f'점수는 {p}점이고, 학점은 {grade}학점입니다.')
