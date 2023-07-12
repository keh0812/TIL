#퀴즈02
#자연수를 입력받고 0부터 자연수까지의 합계를 출력하라.

integer = int(input("자연수를 입력하시오. >>> "))

total = 0
for i in range(1, integer+1) :

    total = total + i

print(total)

#퀴즈03
#사용자로부터 -1을 입력받으면 프로그램이 종료되는 프로그램을 작성하라.

print("프로그램 시작")

while exit != -1 :
    exit = int(input("종료하려면 -1을 입력하세요 >>> "))

print("프로그램 종료")

#퀴즈04

while True :
    default = print("[메뉴를 입력하세요]")
    num = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >>> "))

    if num == 1 :
        print("-> 게임을 시작합니다.")
    elif num == 2 :
        print("-> 랭킹보기")
    elif num == 3 :
        print("-> 게임을 종료합니다.")
        break
    else :
        print("-> 다시 입력해주세요")

