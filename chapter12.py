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
skills.add("Python")  #  집합set은 중복을 제거하기 때문에 Python 부분은 추가 되지 않는다.

skills.remove("SQL")
skills.discard("Java")  # 에러 없이 그냥 진행 된다.  // remove()였으면 KeyError 발생

print(skills)

# 종합 실습 - 두 팀의 기술 목록 비교하기
team_a_list = ["Python", "SQL", "AI", "Python"]
team_b_list = ["Python", "Java", "AI", "Java"]

team_a = []
team_b = []

# 중복 제거하여 team_a에 넣기
for a in team_a_list:
    if a not in team_a:
        team_a.append(a)

for b in team_b_list:
    if b not in team_b:
        team_b.append(b)


print("A팀 고유 기술:", team_a)
print("B팀 고유 기술:", team_b)
# set에서는 집합 연산자 (&, |, - ) 사용 가능
# list로도 중복을 없앨 수 있지만 이 경우 team_a/ team_b를 set으로 저장하는게 코드 간결해짐
print("공통 기술:", set(team_a) & set(team_b)) # 교집합
print("전체 기술:", set(team_a) | set(team_b)) # 합집합
print("A팀만:", set(team_a) - set(team_b))   # A에만 있는 차집합 
print("B팀만:", set(team_b) - set(team_a))   # B에만 있는 차집합



# 심화 과제 - set 사용하지 않고 list 기능만 사용하여 unique_tags 구현하기
tags = ["Python", "AI", "Python", "Data", "AI"]
print(tags)

unique_tags = []

for tag in tags: 
    if tag not in unique_tags:
        unique_tags.append(tag)

print(unique_tags)