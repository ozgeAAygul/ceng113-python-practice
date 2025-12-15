"""
Kullanıcıdan mesaj al
log.txt dosyasına ekle
Program her çalıştığında log büyüsün
"""
print()
print("Task 10: Log Writer")
print()

try:
  message = input("Enter a message: ")
  with open("ceng113-python-practce\FilesExceptions(ch-6)\log.txt", "a", encoding="utf-8") as file:
    file.write(message + "\n")
except Exception as e:
  print("An error occured: ", e)
             
    


