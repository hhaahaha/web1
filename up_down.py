"""
# 에러! 업 혹은 다운이 무한 반복된다.

import random

#함수 선언
user=0
computer=0
count=0

computer = random.randint(1,100)

#함수 연산식

print("1~100까지의 숫자 중에서 맞혀 보세요.")
user= int(input("맞혀 보세요> "))

while user != computer:  # 업 혹은 다운이 무한 반복된다.
    if user < computer:
        print("다운")
        continue

    else :
        print("업")
        continue

print("정답")
"""

import random

#함수 선언
user=0
computers=[]
computer=0

computers= [a for a in range(1,101)]                #list comprehension을 사용하여 컴퓨터가 고를 수 있는 숫자를 한정하고 오류 대비한다.
computer = random.randint(1,100)                    #random 함수를 활용하여 임의의 정수를 받는다.

#함수 연산식

for i in range(len(computers)):                     #computers 리스트의 인자 개수만큼 반복한다.(100번)
    print("1~100까지의 숫자 중에서 맞혀 보세요.")   
    user=int(input("맞혀 보세요> "))                #사용자가 맞출 정수를 입력받는다.

    #에러 대비                                      #만일 1~100 사이의 값을 벗어난 숫자를 받으면 프로그램을 종료한다.
    if user not in computers :                      #함수를 만들어서 try 구문 써보기. ## 프로그램 종료말고 for 구문으로 돌아가게 하는 법은?
        print("범위를 벗어났습니다.")
        break                                       #반복문에서 벗어난다.

    else: 
        if user != computer:                        #1 user 이 computer 와 다르다면
            if user < computer:                       #2 user가 computer보다 작으면 업을 출력한다.
                print("업")
            else:                                     #그렇지 않으면(user가 computer 보다 크면) 다운을 출력한다.
                print("다운")

        else:                                       ##1이 거짓이라면(user가 computer와 같다면) 정답을 출력하고
            print("정답")
            break                                   #for 반복문을 종료한다.

"""


import random

#함수 선언
user=0
computer=0
count=0

computer = random.randint(1,100)

#함수 연산식



while True:
    print("1~100까지의 숫자 중에서 맞혀 보세요.")
    user= int(input("맞혀 보세요> "))
    if user != computer:  # 업 혹은 다운이 무한 반복된다.
        if user < computer:
            print("다운")

        else :
            print("업")
            continue
    else:
        print("정답")
        break
"""
