number = input("Enter a number between 1-12: ")
if int(number) > 1 and int(number)<12:
   print(number)
   for n in range(13):
      print(f"{number}: {number} * {n} = {int(number)*n}")
      print("")
else:
   print("Not Valid1 number")
