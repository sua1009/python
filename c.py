def is_odd(number):
    if number % 2 ==1:
        return True
    else:
        return False

result = is_odd(7)
print(result)

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)
result = avg_numbers(4,5,7,2,3)
print(result)




a = input ()
life is too short, you need python
print(a)


