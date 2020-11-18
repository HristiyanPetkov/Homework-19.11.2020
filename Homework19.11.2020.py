# Exercise 1

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
string = input("Enter a string: ")
i = 0

for c in string:
    if c in vowels:
        i = 0
        while i < 4:
            print(c, end="")
            i += 1
    else:
        print(c, end="")
        
print( )
print( )

# Exercise 2

number = int(input("Enter a number: "))
lenght = 1
loop1 = 0

while loop1 == 0:
    if number / 10 > 1:
        lenght += 1
        number = number / 10
    else:
        loop1 += 1
print("Lenght: ", lenght)

print( )

# Exercise 3

import math

num1 = int(input("Enter a num: "))
root = math.sqrt(num1)
repetitions = 1

while root > 2:
    root = math.sqrt(root)
    repetitions += 1
print(repetitions)

print( )

# Exercise 4

num = int(input("Enter a num: "))
n = 3
result = 2

while n <= num:
    loop = 0
    for k in range(2, n):
        if (n%k) == 0:
            loop += 1
            break
    if loop == 0:
        result += n
    n += 1
print(result)