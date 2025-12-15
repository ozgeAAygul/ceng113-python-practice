"""
Kullanıcıdan metin al
Tekrar eden kelimeleri çıkar
Unique kelimeleri yazdır (set kullan)
"""
print("\nTask 16: Unique Words\n")
text = input("Enter a sentence: ")
if not text.strip():
  print("Invalid input")
else:
  punctuation = ".,?!"
  for char in punctuation:
    text = text.replace(char, " ")

  words = set(text.lower().strip().split())

  print("Unique Words")
  for i in words:
    print(i)