"""
Sabit kullanıcı:
username = "admin"
password = "1234"

Kullanıcıdan giriş al

Doğruysa → “Login successful”
Yanlışsa → “Access denied”
"""
print()
print("Task 4: Login Simulation")
print()

username = "admin"
password = "admin123"

user = input("Enter your username: ")
pas = input("Enter your password: ")

if user == username and pas == password :
  print("Login successful")
else:
  print("Access denied")