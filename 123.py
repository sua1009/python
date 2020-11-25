a = 0
while True:
    a = (input("숫자를 입력하세요"))
    if int(a)%2 == 1:
            print("홀수입니다.")
    elif int(a)%2 ==0:
            print("짝수입니다.")
    elif a == "quit":
            print("종료합니다.")
            break
