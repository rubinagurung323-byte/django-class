fruits = ["apple","banana","cherry"]
fruits.append("orange")
fruits.append("mango")
fruits.insert(1,"blueberry")
#fruits[0] = "blueberry"
fruits.pop()
fruits.remove("cherry")
print(fruits[1])
print(len(fruits))
print(fruits[1:3])

point = (1,2)
x,y = point

print(x,y) 



book = {
    "title" : "django summer class",
    "author" : "someone",
    "publishedAt" : 2026
    

}

book["pages"] =300
print (book["author"])

for key, value in book.items():
    print(f"{key}: {value}")

languages = {"English","Nepali","English"}
languages.add("Chinese")
languages.add("Japanese")

print(languages)

a = [1, 2, 3]
b = a       # same list
b.append(4)
print(a)    # [1, 2, 3, 4]

c = a.copy()  # or list(a)