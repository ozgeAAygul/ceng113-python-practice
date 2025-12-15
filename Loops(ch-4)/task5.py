"""
Kullanıcıdan pozitif bir sayı al

1’den o sayıya kadar:
kaç tane çift
kaç tane tek

sonucu yazdır
"""
print()
print("Task 5: Number Analyzer")
print()

num = int(input("Enter a positive integer: "))
even = 0
odd = 0
for i in range(1, num+1):
  if i % 2 == 0:
    even += 1
  else:
    odd += 1
print(f"From 1 to the number you enter, there are {odd} odd and {even} even numbers.")
