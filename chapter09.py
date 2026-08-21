# mission 01 - 온도에 따라 메시지 바꾸기
temperature = 29
if temperature >= 30:
    print("더워요!")
else:
    print("선선해요!")


#--------------------------------------------------

# mission 02 - 무료배송 조건 만들기
order_amount = 48000
is_member = True

if order_amount >= 50000 or is_member == True:
    print("무료배송입니다.")
else:
    print("배송비가 있습니다.")


#---------------------------------------------------

# mission 03 - 점수에 따라 학습 메시지 출력하기
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("매우 잘했습니다.")
elif score >= 80:
    print("잘했습니다.")
elif score >= 60:
    print("통과했습니다.")
else:
    print("조금 더 연습해 보세요.")


#-----------------------------------------------------------------------

# final mission - 간단한 주문 배송 안내 프로그램
name = input("고객 이름 : ")
total_price = int(input("주문 금액 : "))
member = input("회원 여부[y/n] : ").lower()

if total_price >= 50000 or member == "y":
    print(f"{name}님은 무료배송 대상입니다.")
else:
    print(f"{name}님은 무료배송 대상이 아닙니다. 배달비는 3,000원입니다.")

## 추가 Challenge
if total_price >= 50000:
    print(f"{name}님은 무료배송 대상입니다.")
elif member == "y" and total_price >= 30000:
    print(f"{name}님은 무료배송 대상입니다.")
else:
    print(f"{name}님은 무료배송 대상이 아닙니다. 배달비는 3,000원입니다.")


#--------------------------------------------------------------

# 과제 - 나만의 조건 판단 프로그램
## 과제 A - 연령 안내 프로그램
age = int(input("사용자의 나이를 입력하세요 : "))
if age >= 20:
    print("사용자는 성인입니다.")
elif age >= 17:
    print("사용자는 고등학생입니다.")
elif age >= 14:
    print("사용자는 중학생입니다.")
elif age >= 8:
    print("사용자는 초등학생입니다.")
else:
    print("사용자는 미취학입니다.")


#---------------------------------------------------------------

## 과제 B - 쇼핑 할인 프로그램
price = int(input("상품 금액을 입력해주세요 : "))

if price >= 100000:
    print("10% 할인 대상입니다.")
    print("10% 할인 된 가격은", int(price * 0.9), "원 입니다.")
elif price >= 50000:
    print("5% 할인 대상입니다.")
    print("5% 할인 된 가격은", price * 0.05, "원 입니다.")
else:
    print("할인 대상이 아닙니다.")


#----------------------------------------------------------------

## 과제 C - 간단한 로그인 판정
saved_id = "python"
saved_password = "1234"

id = input("아이디를 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")

if id == saved_id and password == saved_password:
    print("로그인 성공")
else:
    print("아이디 또는 비밀번호를 확인하세요.")