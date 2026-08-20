name = "임서현"
age = 26
height = 163
is_student = True
city = "수원"

# 각 변수 타입 출력
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(city))

# 18번 과제 1
product_name = "파이썬 기초"
price = 28000
discount_rate = 0.15
is_on_sale = True
stock = 12
   # 각 변수 타입 출력
print(type(product_name))
print(type(price))
print(type(discount_rate))
print(type(is_on_sale))
print(type(stock))

   # 정수 price 문자열로 바꿔서 출력
price_text = str(price)

print(price_text)

## "파이썬"은 문자열(str)이기 때문에 int로 출력하면 오류가 난다.
# print(int("파이썬"))

#------------------------------------------------------------------

# 대입연산자 : = , 비교연산자 : ==  !=  >  >=  <  <= , 논리 연산자 : and or not .

# .isdigit() : 문자열 안에 숫자만 들어있는지 검사하는 기능   [True, False로 결과가 나옴]

# f-string은 변수의 값을 문자열 안에 쉽게 넣는 방법
# f"문자열 {변수}"    Ex. print(f"이름은 {name}이고 나이는 {age}살입니다.")
## ,는 천 단위마다 쉼표를 넣으라는 표시
price = 15000
print(f"{price:,}")
### .2f는 소수점 아래 2자리까지 보여줘라는 뜻
avg = 86.666666
print(f"{avg:.2f}")

###  >8 → 8칸 확보 후 오른쪽 정렬    (공백 8칸)
###  <3 → 3칸 확보 후 왼쪽 정렬      (공백 3칸)
###  ^10 → 10칸 확보 후 가운데 정렬  (공백 10칸)
###  
print(f"{15000:>8,}")

# 연산 순서
# 괄호() → 거듭제곱 → 곱하기·나누기·몫·나머지 → 더하기·빼기 → 비교·논리 연산

# 0으로 나누면 에러(ZeroDivisionError) 발생
# ZeroDivisionError: division by zero
# Ex. print(10 / 0)


#----------------------
# mission 01 구매 금액 계산 프로그램
price = 18000
quantity = 3
shipping_fee = 3000

total_product_price = price * quantity
total_price = total_product_price + shipping_fee

print("상품 금액 : ", total_product_price)
print("배송비", shipping_fee)
print("최종 금액 : ", total_price)


# mission 02 시간을 시간과 분으로 바꾸기
total_time = 250
hour = 250 // 60
minute = 250 % 60

print(hour, "시간", minute, "분")

# 과제 A. 카페 주문 금액
coffee_price = 4500
cake_price = 6500

coffee_count = 3
cake_count = 2

coffee_total_price = coffee_price * coffee_count
cake_total_price = cake_price * cake_count

total_order_price = coffee_total_price + cake_total_price

print("총 금액 : ", total_order_price)

# 과제 B. 학습 시간 반환
total_studytime = 385
hours = total_studytime // 60
minutes = total_studytime % 60

print("총 학습 시간은 ", hours,"시간 ", minutes, "분 입니다.")

# 과제 C. 직사각형 계산
width = 12
height = 8

nnn = (width + 3) * height

print("넓이는 ", nnn)