# 리스트 list
scores = [85, 92, 78, 20, 30, 44]
print(scores)

total = 0
for score in scores:
    total += score

avg = total/ len(scores)
# 전체 학생 인원수, 총 점수, 평균 구하기
print(sum(scores) / len(scores))
print(f"학생 수는 {len(scores)}명 이고 전체 학생 점수는 {total}점 입니다. 학생들의 평균은 {avg}점 입니다.")

# 성적에 따라 상위(51 ~ 100), 하위(0 ~ 50) 두 그룹으로 나눠서 각각 인원수, 총 점수, 평균을 구하기
H_total = 0
L_total = 0
H_count = 0
L_count = 0

for score in scores:
    if score >= 51:
        H_total += score
        H_count += 1
    else:
        L_total += score
        L_count += 1

H_avg = H_total / H_count
L_avg = L_total / L_count

print(f"상위 학생은 {H_count}명이고 이들의 총 점수는 {H_total}점 입니다. 상위 학생들의 평균은 {H_avg}점 입니다.")
print(f"하위 학생은 {L_count}명이고 이들의 총 점수는 {L_total}점 입니다. 하위 학생들의 평균은 {L_avg}점 입니다.")

#-------------------------------------------

foods = ["김밥", "떡볶이", "김말이"]
print(foods[1])

items = []
print(items)
print(len(items))

# 리스트 맨 뒤에 값 추가 - append()
todo = ["공부하기"]
print(todo)
todo.append("책 읽기")
todo.append("운동 하기")
print(todo)
todo.append("밥 먹기")
print(todo)

# 리스트 원하는 위치에 값 추가하기 - .insert()
students = ["서현", "다라", "희주"]
print(students)
students.insert(1,"지나")
print(students)
# 리스트에 여러 값 이어 붙이기 - .extend()
more_students = ["영희", "철수"]
students.extend(more_students)
print(students)

# 리스트 값 선택하여 삭제 - .remove(리스트 값)
## 리스트에 없는 값을 remove()하면 ValueError 발생
students.remove("희주")
print(students)
# 리스트에서 위치 찾아서 삭제 - .pop(인덱스)
## 리스트에서 위치 잘못 접근하면 IndexError 발생
students.pop(2)
print(students)
# pop에서 위치 인덱스 안 넣으면 가장 마지막 값이 삭제 됨 - .pop()
students.pop()
print(students)
# 위치로 바로 삭제 - del 리스트명[인덱스]
del students[1]
print(students)


#----------------------------------------------

fruits = ["사과", "바나나", "사과", "포도"]
for fruit in fruits:
    print(fruit)

# range + indexer로 for 돌리기
for i in range(4):
    print(fruits[i])


# -----------------------------------------------------------
# mission 01 - green을 yellow로 바꾸기
colors = ["red", "green", "blue"]
print(colors)
colors[1] = "yellow"
print(colors)


# mission 02 - 장바구니 관리하기
cart = []
cart.append("우유")
cart.append("계란")
cart.append("빵")
print(f"장바구니에는 {cart}이 담겨있고, 모두 {len(cart)}개가 담겨있습니다.")

print("계란" in cart)
# 계란 삭제
cart.remove("계란")

print(f"장바구니에는 {cart}이 담겨있고, 모두 {len(cart)}개가 담겨있습니다.")

# 장바구니에 사과가 있는지 확인 // 없기 때문에 False 결과값
print("사과" in cart)


# mission 03 - 점수 분석하기
scores = [78, 92, 85, 100, 67]
total = 0
H_score = scores[0]
L_score = scores[0]
score_80 = []

for score in scores:
    total += score

avg = total / len(scores)

for score in scores:
    if score > H_score:
        H_score = score
    elif score < L_score:
        L_score = score
# 80점 이상인 점수 리스트
for score in scores:
    if score >= 80:
        score_80.append(score)

print(f"학생 수는 {len(scores)}명이고, 모든 학생들의 총점은 {total}점 입니다. 학생들의 평균 점수는 {avg}점 입니다.")
print(f"학생들의 최저 점수는 {L_score}점이고, 최고 점수는 {H_score}점 입니다.")
print(f"80점 이상인 점수 출력 : {score_80}")


# misson 04 - 간단한 할 일 목록 만들기
todo_list = []

todo_list.append("파이썬 list 공부하기")
todo_list.append("SQLD 1장 공부하기")
todo_list.append("과제 제출하기")

print("[ TODO LIST ]")
for todo in todo_list:
    print(f"- {todo}")

print(f"오늘 할 일은 총 {len(todo_list)}개 입니다.")

# 과제 제출하기 있는지 확인
print("과제 제출하기" in todo_list)