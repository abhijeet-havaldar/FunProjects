def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    
    name = input("Enter your name:")
    

    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Enter your phone No:")
    email = input("Enter your email ID:")
    address = input("Enter your address:")
    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
        }
    print("Contact added successfully!")


def view_contact(contact_book):
    name = input("Enter a name:")
    if name in contact_book:
        contact = contact_book[name]
        print("Name:", name)
        print("Phone:", contact_book[name]["phone"])
        print("Email:", contact_book[name]["email"])
        print("Address:", contact_book[name]["address"])
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Enter a name:")
    if name in contact_book:
        phone = input("Enter a new phone NO:")
        email = input("Enter new email :")
        address = input("Enter new address:")
        
        if phone == '':
            phone = contact_book[name]['phone']
        if email == '':
            email = contact_book[name]['email']
        if address == '':
            address = contact_book[name]['address']
        
        contact_book[name] = {"phone": phone, "email": email, "address": address}

        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input("Enter a name:")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()  # Blank line between contacts for readability

contact_book = {}


while True:
    display_menu()
    choice = input()
    
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        break
    else:
        print("Invalid choice. please try again.")