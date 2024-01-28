# 임의의 두자리 정수(10~99)를 입력받아
# 십의자리, 일의자리 분리 출력
# 10 ~ 99 사이의 정수를 입력하세요 >>> 
e = int(input("정수를 입력하세요(10 ~ 99) >>> "))

print(f'십의 자리 : {e // 10}')
print(f'일의 자리 : {e % 10}')

sec = int(input('초를 입력하세요 >>> '))
hour = sec // 3600
min = sec % 3600 // 60
sec = sec % 60

print(f'변환 결과는 {hour}시 {min}분 {sec}초 입니다.')



# 사원번호의 끝자리 숫자가 5이상이면 '오전', 아니면 '오후'를 출력
# 4자리 사원번호를 입력하세요 >>>

num = int(input('사원번호를 입력하세요(4자리) >>> '))
num %= 10

print('오전' if num >= 5 else '오후')




# 국어, 영어, 수학 점수를 입력받아서 평균을 구하고, 80점 이상이면 '합격' 아니면 '불합격

kor = float(input('국어 점수를 입력하세요 >>> '))
eng = float(input('영어 점수를 입력하세요 >>> '))
math = float(input('수학 점수를 입력하세요 >>> '))

average = (kor+eng+math) / 3.0 

result = '합격' if average >= 80 else '불합격'
print(f'평균은 {average:.2f}점이고, 결과는 {result}입니다.')