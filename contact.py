# Simple Contact Book Program

def display_contacts(contacts):
    """Display all contacts in the contact book."""
    if contacts:
        print("\nContact Book:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
        print()
    else:
        print("\nNo contacts found.\n")

def add_contact(contacts):
    """Add a new contact to the contact book."""
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"Contact '{name}' already exists.")
    else:
        number = input("Enter contact number: ")
        contacts[name] = number
        print(f"Contact '{name}' has been added.")

def delete_contact(contacts):
    """Delete a contact from the contact book."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' has been deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    """Main function to run the contact book program."""
    contacts = {}
    while True:
        print("Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
