# 다른 파일에서도 쓸 함수 두개
def calculate_total(price, quantity):
    return price * quantity

def apply_discount(total, rate=0.1):
    return total * (1 - rate)