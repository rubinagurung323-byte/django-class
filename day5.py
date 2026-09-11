def greet():
    print("Hello")

def greetUser(username):
    print(f"Namaste : {username}")

def sum(a,b,c):
    return a+b+c

def calculateAvg(x,y,z):
    """This function calculates average of 3 number"""
    total =sum(x,y,z)
    avg = total/3
    return avg

myavg = calculateAvg(2,5,6)
print(myavg)

def make_profile(name,age,city="Pokhara"):
    print(f"{name} is {age} years old from {city}")

make_profile("Max",22,"Pokhara")
make_profile("Ramu",19,"Kathmandu")
make_profile("Haru",19)

x = 10 #global

#foo function
def foo():
    x = 5 #local
    print(x)

greetUser("Haru")
greetUser("Ramu")
print("Alien Pradi")

total = sum(30,37)
print(total)

foo()


