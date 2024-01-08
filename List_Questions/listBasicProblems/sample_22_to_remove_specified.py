# qn: Write a Python program to print a
# specified list after removing the 0th, 4th and 5th elements
animal = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
for pos,i in enumerate(animal):
    if pos not in (0,4,5):
        print(i)
# method 2
animal=[i for pos,i in enumerate(animal) if pos not in (0,4,5)]
print(animal)