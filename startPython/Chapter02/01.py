from datetime import date

#01 변수
name = "마스터이"
level = 5
health = 800
attack = 90

print(name, level, health, attack)

level = level + 1

print(level)

# 입력함수
#input()

# x = input("숫자를 입력하세요 >>>")
# print(x)

# x1 = int(input("첫번째 숫자를 입력하세요 >>>"))
# x2 = int(input("두번째 숫자를 입력하세요 >>>"))
# print(x1 * x2)

today = date.today()
y = today.year
birth = input("태어난 연도를 입력하시오 >>> ")
age = y - int(birth) + 1 
print("당신의 나이는 " + str(age) + "세 입니다.")
