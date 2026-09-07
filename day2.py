bio = """
I am rubina 
I am here in django class
I am learning python
"""
print(bio)
bioLength = len(bio)
print(bioLength)

language = "Python"
print(language[-6])
print(language[0:2])
print(language[:2])
print(language[2:])

title = " Python Django "
print(title.strip())
print(title.upper())
print(title.lower())
print(title.split(","))
print(title.count("Python"))
print(title.split(" "))

email = "User@example.com"
clean = email.strip().lower().upper().split()
print(clean)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

print("ha" *(3))
print("hello" * 3 + "" + "world"*3)

print(5<3)
print(5==3)
print(5<=3)

name = "Romukaka"
score = 95
print(f"Student: {name}, Score: {score}")
print(f"Next year age: {19 + 2}")
print(f"Price: ${19.99:}")

username = input("What is your username? ")
print(username)
print ("You username:" + username)
print(f"You must be {age} years old")
print(f"You will be {age + 2} years old after 2 years")

print(f"You will be {int(age) + 2} years old after 2 years")

print(int("10"))
print(float("3.14"))
print(str(100))

