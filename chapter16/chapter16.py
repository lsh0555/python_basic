# mission 01 - 나의 학습 로그 파일 만들기
## w 모드로 첫 번째 학습 기록 저장
with open("study_log.txt", "w", encoding="utf-8") as file:
    file.write("파이썬 파일 쓰기 실습\n")
    file.write("파이썬 mission\n")

## a 모드로 두 번째 기록 추가
with open("study_log.txt", "a", encoding="utf-8") as file:
    file.write("w와 a 모드 차이 확인\n")


# mission 02 - 상품별 매출 출력하기


# mission 03 - 평균 주문 금액 추가하기
 