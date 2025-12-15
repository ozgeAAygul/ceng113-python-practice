"""
Şifre:
en az 8 karakter
en az 1 rakam
en az 1 büyük harf
"""
print()
print("Task 13: Password Validator")
print()

def is_strong_password(password):
  global errors
  errors = []
  
  if len(password) < 8:
    errors.append("şifre 8 haneden az, fazla olmalı!")

  has_digit = False
  has_upper = False

  for i in password:
    if i.isdigit():
      has_digit = True
    if i.isupper():
      has_upper = True

  if not has_digit:
    errors.append("Şifrede en az bi sayı olmalı!")
  if not has_upper:
    errors.append("Şifrede en az büyük harf olmalı!")
  return errors

def main():
  password = input("Enter a password: ")
  errors = is_strong_password(password)
  if len(errors) == 0:
    print("\npassword is valid\n")
  else:
    for error in errors:
      print("-",error)



main()