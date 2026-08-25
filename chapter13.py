# 리스트는 위치로 찾고, 딕셔너리는 키로 찾음 / 추가 수정 가능 / 키 값으로 값 조회
# 없는 값을 대괄호로 조회하면 KeyError 발생
# name, age는 키(key) / 철수, 20은 값(value)
student = {"name" : "철수",
           "age" : 20}
print(student["name"])


# -> 빈 중괄호 {}는 빈 딕셔너리
profile = {}
print(type(profile))
# <class 'dict'>


# 항목 추가, 수정
student = {
    "name": "민수",
    "score": 85
}

student["city"] = "서울"
print(student)

student["score"] = 95
print(student)

# 항목 삭제
# del - 지정한 키와 값 삭제
del student["city"]

# pop() - 항목을 삭제하면서 삭제된 값 돌려줌
removed = student.pop("score")
print(removed)
print(student)

# 키 유무 조회 방법 3가지
# 대괄호 [] - 반드시 존재해야 하는 키를 읽을 때 적합
#student["city"]   # 키가 있으면 값 반환, 값 없으면 KeyError 발생

# get() - 없을 수도 있는 선택적 정보에 적합
# student.get("city")    # 키가 있으면 값 반환, 값 없으면 None 또는 기본값 -> get("city", "정보 없음")

# in - 조회나 삭제 전에 존재 여부를 검사
"score" in student      # 키 존재 여부를 True/False로 확인
if "score" in student:
    print(student["score"])




#---------------------------------------------
# mission 01 - 상품 정보 안전하게 조회하기
product = {
    "name": "키보드",
    "price": 39000
}

print(product["name"])
print(product["price"])
product.get("stock")
print("stock", "재고 정보 없음")
"price" in product
if "price" in product:
    print(product["price"])

# mission 02 - 80점 이상 학생만 출력하기
Students = [
    {"name": "민수", "score": 85},
    {"name": "지영", "score": 92},
    {"name": "서준", "score": 78}
]
for student in Students:
    if student["score"] >= 80:
        print(student["name"], student["score"])


# 종합 실습 - 학생 성적 정보 관리하기
students = [
    {"name": "민수", "score": 85, "city": "서울"},
    {"name": "지영", "score": 92, "city": "부산"},
    {"name": "서준", "score": 78, "city": "서울"}
]
# 성적이 80점 이상이고 서울 사는 학생 출력
for student in students:
    if student["score"] >= 80 and student["city"] == "서울":
        print(student["name"], student["score"])


# mission 03 - 상품 목록 관리하기
products = [
    {"name": "사과", "price": 50000, "stock": 10},
    {"name": "바나나", "price": 20000, "stock": 3},
    {"name": "딸기", "price": 80000, "stock": 0}
]

print(products)
# 가격 30000원 이상의 상품 출력
for product in products:
    if product["price"] >= 30000:
        print(product["name"])

# stock이 0인 상품을 찾아 품절 출력
for product in products:
    if product["stock"] == 0:
        print(f"{product["name"]} 상품은 품절입니다.")


# -------------------------------------------------------------------------------

Sentense = "나는 대한민국 서울 구로에서 파이썬 공부를 하고 있습니다." # 단어 100개 이상
words = Sentense.split()
print(words)
print(type(words))

## 과제
# sentense에서 3회 이상 등장하는 단어는 무엇일까요? 각 단어와 빈도수를 출력하시요.
# 딕셔너리를 활용해 주세요. 지금까지 배우지 않은 기능 사용하지 말것(초보자용 코드)
# 2. 가장 간단한 방식으로 처리할 것. 필요할 경우 배우지 않은 개념도 활용

sentense = "오늘 나는 파이썬 공부를 시작하면서 새로운 개념을 하나씩 천천히 이해하기로 했다. 파이썬 문법은 처음에는 조금 낯설었지만 예제를 직접 따라 하니 점점 익숙해졌다. 특히 리스트와 딕셔너리를 배우면서 여러 데이터를 저장하고 필요한 값을 찾는 방법을 알게 되었다. 파이썬 코드를 작성할 때는 결과만 확인하지 않고 왜 이런 결과가 나오는지도 생각하려고 노력했다. 오류가 발생하면 당황하지 않고 오류 메시지를 읽은 뒤 변수와 자료형을 하나씩 확인했다. 반복문을 사용할 때는 값이 어떤 순서로 들어오는지 살펴보고 조건문을 사용할 때는 조건이 참인지 거짓인지 먼저 예상했다. 앞으로도 파이썬 공부를 꾸준히 하면서 배운 내용을 매일 복습하고 직접 작은 문제를 풀어볼 생각이다. 어려운 문제가 나오더라도 바로 정답을 찾기보다는 내가 아는 문법으로 먼저 해결해 보고 틀린 부분을 확인하면서 다시 도전하고 싶다. 이렇게 연습을 계속하면 코드의 흐름을 자연스럽게 이해하고 내가 원하는 기능도 직접 만들 수 있을 것이라고 생각한다."
words = sentense.split()
print(words)
