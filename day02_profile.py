name = input("Enter your name")
Score1 = input("Enter your grade in maths:")
Score2 = input("Enter your grade in english:")
Score3 = input("Enter your grade in science:")

print(f"""
Student : {name}
Score1: {Score1}, {Score2}, {Score3}
Average: {(float(Score1) + float(Score2) + float(Score3)) / 3}
""")
    
print(f"""
Student : {name}
Scores : {Score1}, {Score2}, {Score3}
Average: {(float(Score1) + float(Score2) + float(Score3)) / 3:.1f}          
""")