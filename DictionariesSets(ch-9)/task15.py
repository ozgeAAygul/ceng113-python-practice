"""
phonebook = {
    "Ali": "0532...",
    "Ayse": "0543..."
}
ekleme
silme
arama
"""
print()
print("Task 15: Phone Book")
print()

def show_menu():
  print("\nPhone Book Menu")  
  print("1-Add")
  print("2-Remove")
  print("3-Search")
  print("4-Quit")

def add(phonebook):
  name = input("Enter the name: ")
  number = input("Enter the number: ")
  if name in phonebook:
    if phonebook[name] == number:
      print(f"{name} already exists.")
    else:
      phonebook[name] = number
      print(f"{name} has been updated")
  else:
    phonebook[name] = number
    print(f"{name} added!")

def remove(phonebook):
  name = input("Enter the name: ")
  if name in phonebook:
    del phonebook[name]
    print(f"{name} removed!")
  else:
    print(f"{name} is not found!")

def search(phonebook):
  name = input("Enter the name: ")
  if name in phonebook:
    print(name, "-->", phonebook[name])
  else:
    print(f"{name} not found")

def main():
  phonebook = {}
  while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
      add(phonebook)
    elif choice == "2":
      remove(phonebook)  
    elif choice == "3":
      search(phonebook)  
    elif choice == "4":
      print("Goodbye:)")
      break
    else:
      print("Invalid choice!")

main()

