# 지정한 횟수만큼 반복
print('/' * 10)

print(len("world"))

# 문자열 + 문자열 → 연결
# 문자열 * 정수 → 반복

my_word = "Gilbert"
print(my_word[0])
print(my_word[1])
print(my_word[-1])


#--------------------------------------------------

# mission 01 - 이메일 주소 일부 잘라내기
email = "student@example.com"

print(email[0])
print(email[-1])
print(email[0:7])
print(email[8:18])
print(email[8:-1])
print(email)

# ------------------------------------
text = "Pythonn"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.find("y"))
print(text.count("n"))

# \n 줄바꿈 | \t 탭 | \" 큰 따옴표 | \\ 역슬래시 자체

#-----------------------------------------------------------------

# mission 02 - 문자열 프로필 카드 만들기
Name = " 문길동 "
City = "seoul"
language = "Python"
intro = "I like java"

print(Name.strip())
print(City.upper())
print(intro.replace("java", "Python"))
print(language(0), language(-1))
print(len(language))
print(f"name : {Name}\nCity : {City}\nintro : {intro}")

# 추가 challenge
print(language[:3])

#-------------------------------------------

# 과제 - 나의 문자열 가공 프로그램
name = " 길동 "
email = "gil@example.com"
city = "seoul"
message = " I like java"

print(name.strip())
print(city.upper())
print(message.replace("java", "Python"))
print(email(0), email(-1))
print(len(email))

print(email[:3])
print(name(0), name(-1))
print(message[-1:-5])
print(f"{name}님의 아이디는 {email}입니다.\n{name}님의 고향은 {city}입니다.\n{name}님이 \"{message}\"라는 메시지를 남겼습니다.")