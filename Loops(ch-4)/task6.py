"""
Program 1–50 arası sayı tutsun

Kullanıcı tahmin etsin
Doğruysa:
You found it in 7 attempts!
"""
print()
print("Task 6: Guess the Number")
print()

import random
random_num = random.randint(1, 50)

count = 0
while True :
  guess= int(input("Guess a number between 1 and 50: "))
  count += 1
  if guess == random_num:
    break
  elif guess > random_num :
    print("Too high!")
  else:
    print("Too low!")

print(f"You found it in {count} attempts!") 

