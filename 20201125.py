user_input = input("저장할 내용을 입력하세요: ")
f = open("C:/python/test.txt", 'a')
f.write(user_input)
f.write("\n")
f.close()


print ("=========7번문제 ======\n")

f = open("C:/python/test1.txt", 'r')
body = f.read()
f.close()

body= body.replace("java","python")

f = open("C:/python/test1.txt", 'w')
f.write(body)
print(body)
f.close()


print("====7번 다른 풀이 ====")

f = open("C:/python/test1.txt", 'r')
body = f.readlines()
f.close()

f = open("C:/python/test1.txt", 'w')
for line in body:
    line = line.replace("python", "java")
    f.write(line)
    print(line)
f.close()



print(" ======5번문제 ======\n")

f1 = open("C:/python/복습.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("C:/python/복습.txt", 'r')
d = f2.read()
print(d)
f2.close()
