# 양수, 음수 판별
num = int(input("숫자를 입력하세요:"))

if num > 0:
    print("양수입니다.")
elif num < 0:
    print("음수입니다.")
else:
    print("영입니다.")


# 성인 판별
age = int(input("나이를 입력하세요:"))

if age >= 18 and age > 0:
    print("성인입니다.")

elif age < 18 and age >0:
    print("미성년자입니다.")

else:
    print("잘못된 나이입니다.")


# 학점 판별
## score = 80
score = int(input("점수를 입력하세요:"))

if score < 0 or score >100:
    print("잘못된 점수입니다.")
elif score >= 90:
    print("A학점")
elif score >=80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else :
    print("F학점")


# 홀짝 판별
num = int(input("숫자를 입력하세요:"))

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")



# 나이에 따른 입장료

age = int(input("나이를 입력하세요"))

if age < 0:
    print("잘못된 나이입니다.")

elif age >= 19:
    print("12,000원")
elif age >=13 and age < 19:
    print("8,000원")
elif age > 7 and age < 13:
    print("5,000원")
else:
    print("무료")