# 집합set은 알아서 중복을 제거한다.
# 요소가 하나인 튜플은 쉼표 필요 (쉼표가 없으면 type이 tuple이 아닌 int가 됨)
# 튜플 요소를 바꾸면 TypeError 발생
int_num = (2, 3, 4 )
print(f"{int_num}의 타입은 {type(int_num)}입니다.")

print(int_num [1])
print(len(int_num))

# 패킹(packing) : 여러 값을 하나로 묶는 것 (양쪽 값의 개수가 맞아야 한다 / 다르면 ValueError 발생)
# 언패킹(unpacking) : 튜플의 값을 여러 변수로 나누어 받는 것

student = ("민수", 21, "Python")
name, age, language = student

print(f"학생의 이름은 {name}이고 나이는 {age}살 입니다. {name}학생이 사용하는 언어는 {language}입니다.")


#----------------------------------------
# mission 01 - 좌표를 튜플로 표현하기
x = 37.5
y = 127.0

location = (x, y)

print(location)
print(location[len(location)-1])


# mission 02 - 기술 집합 관리하기
skills = {"Python", "SQL"}
skills.add("AI")
skills.add("Python")

print(skills)



# 과제 - set 사용하지 않고 list 기능만 사용하여 unique_tags 구현하기
tags = ["Python", "AI", "Python", "Data", "AI"]
print(tags)

unique_tags = []

for tag in tags: 
    if tag not in unique_tags:
        unique_tags.append(tag)

print(unique_tags)