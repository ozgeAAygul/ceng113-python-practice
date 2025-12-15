"""
Cümle al
Kaç kelime olduğunu yazdır
En uzun kelimeyi bul
"""
print()
print("Task 14: Word Counter")
print()

def word_counter(sentence):
  words = sentence.split() #cümleyi kelimelere böler
  
  if not words:
    return 0, [] #eğer kelime yoksa erken bitirir fonksiyonu
  
  count = len(words)
  max_length = max(len(word) for word in words)
  longest_words = [word for word in words if len(word) == max_length]
  
  return count, longest_words

def main():
  sentence = input("Enter a sentence: ")
  if not sentence.strip(): #cümledeki baştaki ve sondaki gereksiz boşlukları silince ortada bişey kalmıyosa kullanıcı sadece boşluk girmiş oluyor uyarı gönderiyoruz
    print("Please enter a valid sentence")
    return #cümle yoksa uzatmaya gerek yok 
  
  # Noktalama işaretlerini sil
  punctuation = ".,!?;:-'\""
  for char in punctuation:
    sentence = sentence.replace(char, "") 
  
  count, longest_words = word_counter(sentence)
  print(f"There are {count} words in the sentence.")
  
  if longest_words:
    if len(longest_words) == 1:
      print(f"Longest word is '{longest_words[0]}' ({len(longest_words[0])} characters).")
    else:
      words_str = ", ".join(longest_words) #birden fazla longest word varsa bunları virgül ile birleştirip yan yana yazıyor
      print(f"Longest words are: {words_str} ({len(longest_words[0])} characters each).")

main()
 
