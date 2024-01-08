fruit_list=['apple','orange','banana','mango','grapes']
# for i in range(len(fruit_list)):
#     print(i,fruit_list[i])

#we can use enumerate if we want print position along with elements
for pos,fruit in enumerate(fruit_list):
    print(pos,fruit)