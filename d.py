
    
f = open("C:/python/복습.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)
f.close()

f = open("C:/python/복습.txt", 'r')
while True:
    line = f.readline()
    if line>=6:break
    print(line)
f.close()

f = open("C:/python/복습.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
