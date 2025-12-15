"""
grades.txt dosyası oluştur
Dosyayı oku
Ortalama notu hesapla
Dosya yoksa try-except ile hata ver
"""
print()
print("Task 9: Student Grades File")
print()

try:
  with open("ceng113-python-practce\FilesExceptions(ch-6)\grades.txt", "r", encoding="utf-8") as file :
    grades = []
    for line in file:
      parts = line.strip().split()  #strip boşlukları temizler split ise stringi boşluklardan bölüp liste olarak döndürür
      if len(parts) == 2:
        name , grade = parts[0], int(parts[1])
        grades.append(grade)
        print(f"{name}: {grade}")
    if grades:
      total = 0
      for i in grades:
        total += i
      avg = total / len(grades)
      print(f"Average: {avg:.2f}")
    else:
      print("No grade")
    
except FileNotFoundError :
  print("Dosya bulunamadı.")    
except ValueError:
  print("Dosyada geçerli veri bulunamadı")



