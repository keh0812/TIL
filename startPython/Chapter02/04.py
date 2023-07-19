# 로또 번호 6개 생성
# 로또 번호는 1~45까지의 수
# 6개 숫자 모두 달라야 함
# 로또 생성 함수로 작성

import random

def lotto():
    lotto_list = []
    for i in range(1,7):
        num = random.randint(1,45)

        while True :

            if num not in lotto_list: 
                lotto_list.append(num)
                break
    
    print("lotto list >> ", lotto_list)
        

lotto()
    
