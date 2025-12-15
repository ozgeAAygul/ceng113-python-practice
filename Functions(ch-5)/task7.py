"""
Aşağıdaki fonksiyonları yaz:

def is_even(n)
def factorial(n)
def average(numbers)


Ana programda test et.
"""
print()
print("Task 7: Utility Functions")
print()

def is_even(num):
  return num % 2 == 0

def factorial(num):
  fac = 1
  for i in range(2, num+1):
    fac *= i
  return fac

def average(numbers):
  sum = 0
  for i in numbers:
    sum += i
  avg = sum / len(numbers)
  return avg

def main():
  num_iseven = int(input("Enter a integer that you wonder it is even or not: "))
  print(is_even(num_iseven))

  num_fac = int(input("Enter a integer that you want to calculate factorial: "))
  print(factorial(num_fac))

  numbers_input = input("Enter numbers (coma-seperated): ")
  numbers = []
  for num_str in numbers_input.split(","):
    numbers.append(int(num_str))
  print(f"Average: {average(numbers)}")

main()

  
