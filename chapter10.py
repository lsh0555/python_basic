a = 0
for i in range(5):
    a += i
print(a)

# mission 01 - 1부터 10까지 홀수 출력하기
for i in range(1,11):
    if i % 2 != 0:
        print(i)

# --------------------------------

for i in range(1, 11, 2):
    print(i)


# mission 02 - 1부터 100까지 합계 구하기
total = 0
for num in range(1, 101):
    total += num
print(total)

# 추가 미션 - 1부터 10까지 짝수의 합만 계산
num_total = 0
for number in range(1, 11):
    if number % 2 ==0:
        num_total += number

print(num_total)

# ------------------------------

# mission 03 - 특정 숫자에서 멈추기
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#---------------------------------
# 종합 실습 - 입력받은 숫자의 구구단 출력하기
# 1부터 12까지 출력, 짝수일 때 메시지 추가
dan = int(input("출력할 단을 입력하세요 : "))
message = "짝수 결과 입니다."

print(f"< {dan}단 >")
for number in range(1, 13):
    result = dan * number
    if result % 2 ==0:
        print(f"{dan} X {number} = {result}, {message}")
    else:
        print(f"{dan} X {number} = {result}")
    
#-----------------------------------------------

# mission 04 - 1부터 입력값까지의 합계
int_num = int(input("양의 정수를 입력해주세요 : "))
int_total = 0

for i in range(1, int_num):
    int_total += i
print(int_total)

#----------------------------------------------

# Final mission - 반복문으로 작은 프로그램 만들기
## 미션 A - 카운트 다운
count_number = int(input("시작 숫자를 입력해주세요 : "))
for i in range(count_number, 0, -1):
    print(i)
print("시작!")

## 미션 B - 배수 찾기
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

## 미션 C - 합계 계산기
int_number = int(input("양의 정수를 입력해주세요 : "))
int_num_total = 0

for i in range(1, int_number):
    int_num_total += i
print(int_num_total)

## 미션 D - 비밀번호 재입력 연습
password = 10
input_password = int(input("비밀번호를 입력해주세요 : "))

while input_password != password:
    if input_password == password:
        break
    else:
        print("비밀번호가 일치하지않습니다.")
        input_password = int(input("비밀번호를 입력해주세요 : "))