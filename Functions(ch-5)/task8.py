"""
1. Calculate factorial
2. Check even/odd
3. Exit
Seçime göre fonksiyon çağır
"""
print()
print("Task 8: Menu-Based Program")
print()

def factorial(num):
  fac = 1 
  for i in range(2,num+1):
    fac *= i
  return fac

def even_odd(num):
  return "even" if num % 2 == 0 else "odd"

while True:
  print("\n1. Calculate factorial\n2. Check even/odd\n3. Quit")
  choice = input("Choose an option(1, 2, or 3): ")

  if choice == "1":
    try:
      number = int(input("Enter a number: "))
      print(f"Factorial: {factorial(number)}")
    except ValueError:
      print("invalid input!")
  elif choice == "2":
    try:
      number = int(input("Enter a number: "))
      print(even_odd(number))
    except ValueError:
      print("invalid input!")
  elif choice == "3":
    break
  else:
    print("invalid input")