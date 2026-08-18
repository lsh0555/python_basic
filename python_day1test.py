# 간단한 ATM 프로그램

# 초기 잔액 100,000원
money = 100000

print("1. 잔액 조회")
print("2. 입금")
print("3. 출금")
print("4. 종료")

num = int(input("필요한 서비스의 번호를 입력해 주세요. : "))

# 잔액 조회
def see_ATM(num):
    print("현재 잔액 : ", money, "원")


# 입금
def input_money(num):

    in_m = int(input("입금할 금액 : "))

    if in_m > 0: 
        
        print(in_m,"원이 입금되었습니다.")
        print("현재 잔액 : ", money + in_m)

    else:
        print("잘못된 금액입니다.")

# 출금
def output_money(num):

    out_m = int(input("출금할 금액 : "))

    if out_m > 0 and out_m <= money:
        print(out_m, "원이 출금되었습니다.")

    elif out_m > money:
     print("잔액이 부족합니다.")

    else:
        print("잘못된 금액입니다.")


# 종료
def finish_ATM(mum):
    print("ATM을 종료합니다.")

# 잘못된 입력 오류 메시지 + 각 서비스 실행
if num == 1:
    see_ATM(num)

elif num == 2:
    input_money(num)

elif num == 3:
    output_money(num)

elif num == 4:
    finish_ATM(num)

else:
    print("잘못된 입력입니다.")


    ## 고쳐야 할 것 : money 변수 값 바뀌게 하기..
    # 4번 하기 전까지 코드 계속 실행하게 하기