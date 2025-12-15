"""
Ortalama al

Not aralığına göre:
90–100 → A
80–89 → B
70–79 → C
60–69 → D
else → F

"""

print()
print("Task 3: Letter Grade Calculator")
print()

gpa = int(input("Enter your gpa: "))
if 100 <= gpa <= 90:
  print("letter grade A")
elif 89 <= gpa <= 80:
  print("letter grade B")
elif 79 <= gpa <= 70:
  print("letter garde C")
elif 69 <= gpa <= 60:
  print("letter grade D")
else:
  print("letter grade F")