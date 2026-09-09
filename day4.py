for letter in "Django":
    print(letter)

fruits = ["raspberry","strawberry","blueberry"]
for fruit in fruits:
    print(fruit)

    

for i in range(5):
    print(i)

for j in range(1,10):
    print(j)

for j in range(1,10,2):
    print(j)

# 1 - 10 sum ???
total = 0
for n in range(1,10):

    total = total + n
print(total)
count = 5
while count > 0:
    print(count)
    # count-=1
    # count = count - 1
    count = count -1 
print("finished") 

for n in range(10):
    if n %2 == 0:
        print(f"Even:{n}")
        #print("Even:" + str (n))
    else:
        print(f"Odd:{n}" )
        #print("Odd:" + str (n))

for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()


