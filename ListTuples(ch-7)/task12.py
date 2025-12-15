"""
Not listesi:
grades = [45, 78, 90, 66, 84, 55]

En yüksek
En düşük
Ortalama
"""
print()
print("Task 12: Exam Statistics")
print()

grades = [45, 78, 90, 66, 84, 55]

highest = grades[0]
for i in grades :
  if i > highest:
    highest = i

lowest = grades[0]
for i in grades:
  if i < lowest:
    lowest = i

total = 0
for i in grades:
  total += i

avg = total / len(grades)   

print(f"Highest score: {highest}\nLowest score: {lowest}\nAverage: {avg:.2f}")