# mission 01 - 합계와 평균 함께 반환하기
## 1)
def calculate_summary(a, b):
    total = a + b
    avg = total / 2
    return total, avg

a = int(input("숫자를 입력하세요 : "))
b = int(input("숫자를 입력하세요 : "))

total, avg = calculate_summary(a, b)

print(f"두 수의 합은 {total}이고 두 수의 평균은 {avg}입니다.")

## 2)
import inspect

def calculate_summary(a, b):
    total = a + b
    return total

a = int(input("숫자를 입력하세요 : "))
b = int(input("숫자를 입력하세요 : "))

avg = calculate_summary(a, b) / len(inspect.signature(calculate_summary).parameters)

print(f"두 수의 합은 {calculate_summary(a,b)}입니다. 두 수의 평균은 {avg}입니다.")

# mission 02 - 리스트 평균 함수 만들기
scores = [85, 92, 78]

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total

average = calculate_average(scores) / len(scores)

print(f"평균은 {average}입니다.")

# 종합 실습 - 학생 점수 보고서 함수 만들기
name = "민수"
scores = [85, 90, 95]
score = scores(0) + scores(1) + scores(2)

def calculate_average(scores):    # 평균 반환
    total = 0
    for score in scores:
        total += score
    avg = total / len(scores())

    return avg

average =  calculate_average(scores)


def get_grade(score):     # 등급 반환
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"    

grade = get_grade(scores)

def show_report(name, average, grade):
    a = f"{name}학생의 평균은 {average}이고, 등급은 {grade}입니다."

    return a