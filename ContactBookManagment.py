import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("\nContact List is empty.")
            return

        # Display heading
        heading = "{:<20} {:<15} {:<30}".format("Name", "Phone", "Email")
        print(heading)
        print("-" * len(heading))

        # Display contact information
        for contact in self.contacts:
            contact_info = "{:<20} {:<15} {:<30}".format(contact.name, contact.phone, contact.email)
            print(contact_info)

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, contact_id, updated_contact):
        if 0 < contact_id <= len(self.contacts):
            self.contacts[contact_id - 1] = updated_contact
            print(f"Contact '{updated_contact.name}' updated successfully.")
        else:
            print("Invalid contact ID. Update failed.")

    def delete_contact(self, contact_id):
        if 0 < contact_id <= len(self.contacts):
            deleted_contact = self.contacts.pop(contact_id - 1)
            print(f"Contact '{deleted_contact.name}' deleted successfully.")
        else:
            print("Invalid contact ID. Deletion failed.")

def display_menu(contact_book):
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    user_input = input("Enter your choice (1-6): ")
    return user_input

def add_contact_prompt():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    return Contact(name, phone, email, address)

def search_contact_prompt():
    keyword = input("Enter the search keyword: ")
    return keyword

def update_contact_prompt():
    contact_id = int(input("Enter the contact ID to update: "))
    return contact_id, add_contact_prompt()

def delete_contact_prompt():
    contact_id = int(input("Enter the contact ID to delete: "))
    return contact_id

def main():
    contact_book = ContactBook()

    while True:
        user_input = display_menu(contact_book)

        if user_input == "1":
            new_contact = add_contact_prompt()
            contact_book.add_contact(new_contact)

        elif user_input == "2":
            contact_book.view_contact_list()

        elif user_input == "3":
            keyword = search_contact_prompt()
            search_results = contact_book.search_contact(keyword)

            if not search_results:
                print("No matching contacts found.")
            else:
                print("\nSearch Results:")
                for idx, contact in enumerate(search_results, start=1):
                    print(f"{idx}. {contact.name} - {contact.phone} - {contact.email}")

        elif user_input == "4":
            contact_id, updated_contact = update_contact_prompt()
            contact_book.update_contact(contact_id, updated_contact)

        elif user_input == "5":
            contact_id = delete_contact_prompt()
            contact_book.delete_contact(contact_id)

        elif user_input == "6":
            print("Exiting...")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
