def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

num=int(input("How much numbers u want"))
if num<=0:
    print("Invalid Input...!!!!!!")
else:
    for i in range(num):
        print(fibonacci(i))