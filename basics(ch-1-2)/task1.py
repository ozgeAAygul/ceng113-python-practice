#Task 1: Student Info Program
"""
Kullanıcıdan: ad, bölüm, vize notu, final notu al
Ortalamayı hesapla (%40 vize + %60 final)

Çıktı:

Student: Özge
Department: Computer Engineering
Average: 78.4
"""
#Kullanılanlar: input, type casting, print
print()
print("Task 1: Student Info Program")
print()

name = input("Enter your name: ")
field = input("Enter your field: ")
midterm = int(input("Enter your midterm grade: ")) * 0.4
final = int(input("Enter your final grade: ")) * 0.6
gpa = midterm + final 
print()
print(f"Student: {name}\nDepartment: {field}\nAverage: {gpa}")
print()