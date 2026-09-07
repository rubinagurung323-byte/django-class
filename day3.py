age = int (input ("Age: "))
has_ticket = True

if age >= 18 and has_ticket:
    print("You may enter.")
elif age >= 18 and not has_ticket:
    print("Please buy ticket.")
elif age < 18:
    print("You are a minor.")

else:
    print("Sorry, 18+ only.")