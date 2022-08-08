num = int(input("자연수를 입력하시오: "))
""" for i in range(num):
    print(str(i+1) , end=' ') """

sum = 0
for i in range(num+1):
    sum += i
print(sum)
