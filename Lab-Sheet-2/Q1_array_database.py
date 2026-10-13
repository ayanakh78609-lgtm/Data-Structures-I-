def display(arr):
    print("Array:", arr)

def insert_at(arr, index, value):
    if index < 0 or index > len(arr):
        print("Invalid insertion index")
        return
    arr.insert(index, value)
    print("Inserted successfully")

def delete_at(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid deletion index")
        return
    print("Deleted:", arr.pop(index))

def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr = [10, 20, 30, 40, 50]
while True:
    print("\n1.Display  2.Insert  3.Delete by index  4.Search  5.Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        display(arr)
    elif choice == "2":
        try:
            index = int(input("Index to insert at: "))
            value = int(input("Numeric value: "))
            insert_at(arr, index, value)
        except ValueError:
            print("Enter integers only")
    elif choice == "3":
        try:
            delete_at(arr, int(input("Index to delete: ")))
        except ValueError:
            print("Enter an integer index")
    elif choice == "4":
        try:
            target = int(input("Value to search: "))
            index = sequential_search(arr, target)
            print(f"Found at index {index}" if index != -1 else "Value not found")
        except ValueError:
            print("Enter an integer")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
