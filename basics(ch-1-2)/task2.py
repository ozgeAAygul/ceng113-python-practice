"""
Task 2: Simple Calculator

Kullanıcıdan iki sayı ve işlem al (+ - * /)

Sonucu yazdır

Bölme işleminde 0’a bölme kontrolü yap
"""
print()
print("Task 2: Simple Calculator")
print()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter a operator(+, -, *, /): ")

if operator == "+":
  result = num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == "/":
  if num2 == 0:
    print("undefined")  
  else:
    result = num1 / num2
print()
print(f"Result: {result}")
print()