"""
Liste oluştur

Kullanıcı:

ürün ekleyebilsin
ürün silebilsin
listeyi görebilsin
"""
print()
print("Task 11: Shopping List")
print()

shopping_list = []

while True:
  print("1. Add item\n2. Remove item\n3. Look the list\n4. quit")
  choice = input("Choose: ")
  
  if choice == "1":
    item = input("Enter item name: ")
    if item:#bak bu aklına gelmemişti item girilir ise ekleme yapıyor
      shopping_list.append(item)
      print(f"'{item}' added")
    else:
      print("Item name cannot be empty!")

  elif choice == "2":
    item = input("Enter the item name to remove: ")
    if item in shopping_list: #sen for yapmıştın fora gerek yokmuş
      shopping_list.remove(item)
      print(f"'{item}' removed.")
    else:
      print(f"'{item}' is not in list")

  elif choice == "3":
    if shopping_list: # bak bu da aklına gelmemişti
      print()
      print("Shopping List:")
      for idx, item in enumerate(shopping_list, 1): #bu şekilde yazmak zorunda değilsin ama daha şık duruyor hem enumerate kullanmış oldun 
        print(f"{idx}. {item}")
    else:
      print("List is empty!")

  elif choice == "4":
    print("Goodbye:)")
    break

  else:
    print("Invalid choice.")
  
      

  