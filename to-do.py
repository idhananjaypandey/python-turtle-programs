# Simple To-Do List Program
def display_todo_list(todo_list):
    print("\nTo-Do List:")
    for idx, item in enumerate(todo_list, 1):
        print(f"{idx}. {item}")
    print()

def add_todo_item(todo_list):
    item = input("Enter a new to-do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

def main():
    todo_list = []
    while True:
        print("Menu:")
        print("1. View To-Do List")
        print("2. Add To-Do Item")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_todo_item(todo_list)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
