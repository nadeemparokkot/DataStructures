num = [20, 70, 30, 90, 10, 30, 90, 10, 80]
# in-built
print(num.index(30))

# user defined
target=30
for i in range(len(num)):
    if num[i]==target:
        print(i)
        break