# input()의 결과는 항상 문자열이기에 필요에 따라 형변환 필요
# 입력 문자열은 strip()으로 정리 가능
# ValueError : 숫자로 바꿀 수 없는 입력 오류 -> 데이터형 확인

## try/except : 잘못 입력했을 때 프로그램이 종료되지 않게 만듦

#-----------------------------------------------------------------------

# mission 01 - 주문 금액 계산 프로그램
customer = input("고객 이름 : ").strip()
product = input("상품명 : ").strip()
price = int(input("상품 가격 : ").strip())
quantity = int(input("수량 : ").strip())
total = price * quantity

print(f"{customer}님이 주문하신 총 금액은 {total}원 입니다.")


# change it - 주문 프로그램 확장하기
## 도전 A 배송비
delivery_price = int(input("배송비를 입력하세요 :"))
total_price = total + delivery_price

print(f"{customer}님의 배달비를 포함한 주문하신 금액은 {total_price}원 입니다.")

## 도전 B 주문 요약 한 문장
print(f"{customer}님이 {product} {quantity}개를 주문했습니다. 총 주문 금액은 {total_price}원 입니다.")


#--------------------------------------------------------------

# mission 02 학습 시간 계산기
name = input("이름 : ")
day_study_time = float(input("하루 학습 시간 : "))
study_day = int(input("학습 일수 : "))

all_study_time = day_study_time * study_day

print(f"{name}님의 총 학습 시간은 {all_study_time}시간입니다.")

#----------------------------------------------------------------

# 과제 A - 카페 주문 계산기
drink = input("음료 이름 : ")
drink_price = int(input("가격 : "))
drink_quantity = int(input("수량 : "))

total_drink_price = drink_price*drink_quantity

print(f"주문 하신 {drink}의 총 금액은 {total_drink_price}원 입니다.")

#-------------------------------------------------------------------

# 과제 B - 운동 시간 계산기
Name = input("이름 : ")
day_hour = int(input("하루 운동 시간 : "))
day = int(input("운동 일수 : "))

all_hour = day_hour*day

print(f"총 운동 시간은 {all_hour}시간입니다.")


#-----------------------------------------------------------------

# 과제 C - 여행 경비 계산기
place = input("여행지 : ")
day_price = int(input("1일 예상 비용 : "))
trip_day = int(input("여행 일수 : "))

trip_price = day_price*trip_day

print(f"전체 예상 비용은 {trip_price}원 입니다.")