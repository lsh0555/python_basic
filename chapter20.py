def calculate_shipping(total_price):
    if total_price >= 50000:
        return 0
    else :
        return 3000

# 구매 합계 금액이 50000 이상일 경우 배송비 0
# 구매 합계 금액이 50000 미만일 경우 배송비 3000
print(calculate_shipping(49999) == 3000)
print(calculate_shipping(50000) == 0)
print(calculate_shipping(50001) == 0)

#----------------------------------------------

tests = [
    (40000, 3000),
    (49999, 3000),
    (50000, 0),
    (50001, 0),
    (60000, 0),
    (69999, 0),
    (70000, 0),
    (70001, 0),
    (80000, 0),
    (80001, 0),
]