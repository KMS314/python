'''
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]

100점 받은 사람 제외하고, 나머지 학생들의 점수를 5점씩 증가하여 score라는 리스트를 생성하고 출력하시오.
단, 100점이 초과되지 않도록 처리하세요.
'''

exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]

score = []

for n in exam:
    po = n + 5
    if po > 100:
        po = 100
    score.append(po)
        
print(score)