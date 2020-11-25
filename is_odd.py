def is_odd(num):
    if int(num)%2 == 0 :
        return True
    else:
        return False

while True:
    num = input("수를 입력하세요. >")

    if num in ['exit','EXIT','quit']:
        print("종료합니다.")
        break

    result = is_odd(num)

    if result == True :
        print("짝수입니다.")
    else :
        print("홀수입니다.")
        
