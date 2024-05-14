# Contact Management System

# Introduction

# Welcome to the Contact Management System project! In this project, you will apply your Python programming skills
# to create a functional command-line-based application that simplifies the management of your contacts. The Contact 
# Management System will empower you to add, edit, delete, and search for contacts with ease, all while reinforcing 
# your understanding of Python dictionaries, file handling, user interaction, and error handling.

# Project Requirements
# Your task is to develop a Contact Management System with the following features:
# 1. User Interface (UI):
#  - Create a user-friendly command-line interface (CLI) for the Contact Management System.
#  - Display a welcoming message and provide a menu with the following options:
#  '' Welcome to the Contact Management System! Menu:
#  - Add a new contact
#  - Edit an existing contact
#  - Delete a contact
#  - Search for a contact
#  - Display all contacts
#  - Export contacts to a text file
#  - Import contacts from a text file *BONUS
#  - Quit ">

# 2. Contact Data Storage:
#  - Use nested dictionaries as the main data structure for storing contact information.
#  - Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
#  - Store contact details within the inner dictionary, including:
#    - Name
#    - Phone number
#    - Email address
#    - Additional information (e.g., address, notes).

# 3. Menu Actions:
#    Implement the following actions in response to menu selections:
#  - Adding a new contact with all relevant details.
#  - Editing an existing contact's information (name, phone number, email, etc.).
#  - Deleting a contact by searching for their unique identifier.
#  - Searching for a contact by their unique identifier and displaying their details.
#  - Displaying a list of all contacts with their unique identifiers.
#  - Exporting contacts to a text file in a structured format.
#  - Importing contacts from a text file and adding them to the system. * BONUS

# 4. User Interaction:
#  - Utilize input() to enable users to select menu options and provide contact details.
#  - Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

# 5. Еггог Handling:
#  - Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during
# execution.

# 6. GitHub Repository:
#  - Create a GitHub repository for your project.
#  - Commit your code to the repository regularly.
#  - reate a clean and interactive README.md file in your GitHub repository.
#  - Include clear instructions on how to run the application and explanations of its features.
#  - Provide examples and screenshots, if possible, to enhance user understanding.
#  - Include a link to your GitHub repository in your project documentation.

# 7. Optional Bonus Points
#  - Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work).
#  - Each contact can belong to one or more categories.
#  - Contact Search (Bonus): Enhance the contact search
#  - Functionality to allow users to search for contacts by name, phone number, email address, or additional information.
#  - Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
#  - Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.

# By successfully completing this project, you will not only enhance your Python programming skills but also have a
# practical Contact Management System to streamline your contact management tasks. Get ready to create a valuable tool for yourself and others!
# Happy coding!

# Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.
# Project Submission
# Upon completion, submit your project, including all source code files and the README.md file in your GitHub repository, to your instructor or designated platform.

# contacts = {
#     "victor_5@wharton.edu": {"Name": "Victor", "Phone number": "857-926-4038", "Email address": "victor_5@gmail.com", "Address": "Philadelphia"},
#     "cait_n31@gmail.com": {"Name": "Cait", "Phone number": "215-308-2030", "Email address": "cait_n31@gmail.com", "Address": "Boston"},
#     "teresa29@gmail.com": {"Name": "Teresa", "Phone number": "267-010-2564", "Email address": "teresa29@gmail.com", "Address": "New York"},                     
# }


import re

contacts = {}  # Creating an empty dictionary to store the contact information.

# add_new_contact() function prompts the user to input information for a new contact (name, phone number, email address, and address). It validates the input 
# formats using regular expressions and ensures that the input is not blank. If all required information is provided and the contact is not already in the 
# dictionary, it adds the contact to the contacts dictionary.

def add_new_contact(contacts):
    print("\nPlease enter the following information:")
    name = input("\nFull name:\n").title().strip()
    while not name.strip():
        print("\nError: The name cannot be blank")
        name = input("\nPlease enter the full name:\n").title().strip()
    phone_number = input("\nPhone number (example: 123-456-7890):\n").strip()
    while not re.match(r"^\d{3}-\d{3}-\d{4}$", phone_number):
        phone_number = input("\nPlease enter the phone number in the correct format (example: 123-456-7890):\n").strip()
    email_address = input("\nEmail address (example: user@example.com):\n").lower().strip()
    while not re.match(r"\b[A-Za-z0-9._%+-\u0300-\u036F]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email_address):
        email_address = input("\nPlease enter a valid email address (example: user@example.com):\n").lower().strip()
    if name and phone_number and email_address:
        dict_key = f"{email_address}"
        if dict_key in contacts:
            print("\nThis contact information has already been added to the Contact Management System!")
        else:
            address = input("\nAddress:\n").title().strip()
            while name and phone_number and email_address and not address.strip():
                print("\nError: The address cannot be blank")
                address = input("\nPlease enter the address:\n").title().strip()
            if name and phone_number and email_address and address:
                contacts[dict_key] = {"Name": name, "Phone number": phone_number, "Email address": email_address, "Address": address}

    return contacts

# edit_existing_contact() function allows the user to edit the information of an existing contact. It prompts the user to enter the email address of the contact 
# to be edited and then presents options to edit different fields of the contact (name, phone number, email address, and address). It validates the input formats 
# similar to the add_new_contact() function.

def edit_exisiting_contact(contacts):
    dict_key = input("\nPlease enter the email address of the contact you want to edit:\n").lower().strip()
    while not re.match(r"\b[A-Za-z0-9._%+-\u0300-\u036F]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", dict_key):
        dict_key = input("\nPlease enter a valid email address (example: user@example.com):\n").lower().strip()
    if dict_key not in contacts:
        print(f"\nThere's no contact with email {dict_key}")
        print("\n")
        print(contacts)
    elif dict_key in contacts:
        print("\n")
        print(contacts[dict_key])
        choice = input("\nWhich information would you like to change?\n"
                        "\n1. Name"
                        "\n2. Phone number"
                        "\n3. Email address"
                        "\n4. Address\n"
                       "\nEnter your choice from 1 to 4:\n").lower().strip()
        
        if choice == "1":
            name = input("\nEnter a new name:\n").title().strip()
            while not name.strip():
                print("\nError: The name cannot be blank")
                name = input("\nPlease enter the full name:\n").title().strip()
            contacts[dict_key]["Name"] = name
            print(f"\nThe information for {dict_key} has been changed:\n")
            print(contacts[dict_key])
        if choice == "2":
            phone_number = input("\nEnter a new phone number (example: 123-456-7890):\n").strip()
            while not re.match(r"^\d{3}-\d{3}-\d{4}$", phone_number):
                phone_number = input("\nPlease enter the phone number in the correct format (example: 123-456-7890):\n").strip()
            contacts[dict_key]["Phone number"] = phone_number
            print(f"\nThe information for {dict_key} has been changed:\n")
            print(contacts[dict_key])
        if choice == "3":
            email_address = input("\nEnter a new email address:\n").lower().strip()
            while not re.match(r"\b[A-Za-z0-9._%+-\u0300-\u036F]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email_address):
                email_address = input("\nPlease enter a valid email address (example: user@example.com):\n").lower().strip()
            contacts[dict_key]["Email address"] = email_address
            print(f"\nThe information for {dict_key} has been changed:\n")
            print(contacts[dict_key])
            # new_dict_key = email_address
            contacts[email_address] = contacts.pop(dict_key)
        if choice == "4":
            address = input("\nEnter a new address:\n").title().strip()
            while not address.strip():
                print("\nError: The address cannot be blank")
                address = input("\nPlease enter the address:\n").title().strip()
            contacts[dict_key]["Address"] = address
            print(f"\nThe information for {dict_key} has been changed:\n")
            print(contacts[dict_key])

# delete_contact() function allows the user to delete a contact from the contacts dictionary. It prompts the user to enter the email address of the contact 
# to be deleted and removes it from the dictionary if it exists.

def delete_contact(contacts):
    dict_key = input("\nPlease enter the email address of the contact you want to delete:\n").lower().strip()
    while not re.match(r"\b[A-Za-z0-9._%+-\u0300-\u036F]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", dict_key):
        dict_key = input("\nPlease enter a valid email address (example: user@example.com):\n").lower().strip()
    if dict_key not in contacts:
        print(f"\nThere's no contact with email {dict_key}\n")
    else:
        print(f"\nThe following contact has been deleted from the Contact Management System:\n")
        print(f"{dict_key}: {contacts[dict_key]}")
        del contacts[dict_key]

# search_contact() function allows the user to search for a contact by entering the email address. If the contact exists, it displays the contact information.

def search_contact(contacts):
    dict_key = input("\nPlease enter the email address of the contact you want to find:\n").lower().strip()
    while not re.match(r"\b[A-Za-z0-9._%+-\u0300-\u036F]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", dict_key):
        dict_key = input("\nPlease enter a valid email address (example: user@example.com):\n").lower().strip()
    if dict_key not in contacts:
        print(f"\nThere's no contact with email {dict_key}\n")
    else:
        print(f"\nHere is the information your requested:\n")
        print(f"{dict_key}: {contacts[dict_key]}")

# display_contacts() function displays all the contacts currently stored in the contacts dictionary.

def display_contacts(contacts):
    print("\nHere is the information about all the contacts currently present in our Contact Management System:\n")
    print(contacts)

# export_contacts() function exports the contacts from the contacts dictionary to a text file named "contact_list.txt". It formats the contact information 
# and writes it to the file.

def export_contacts(contacts):
    with open("contact_list.txt", "w") as file:
        file.write(f"Here is a complete contact list:\n\n")
        for dict_key, dict_subkey in contacts.items():
            file.write(f"{dict_key}: \n  - {"Name:" + " " + dict_subkey["Name"]}\n  - {"Phone number:" + " " + dict_subkey["Phone number"]}\n"  
                        f"  - {"Email address:" + " " + dict_subkey["Email address"]}\n  - {"Address:" + " " + dict_subkey["Address"]}\n\n")
    print("\nYour contacts have been successfully exported to contact_list.txt")

    # To simply export dictionaries, we can use this code:
    # with open("contact_list.txt", "w") as file:
    #     for dict_key, dict_subkey in contacts.items():
    #         file.write(f"{dict_key}: {dict_subkey}\n")

# import_contacts() function imports contacts from the "contact_list.txt" file into the contacts dictionary. It reads the file line by line and prints 
# each line to the console.

def import_contacts(contacts):
    try:
        with open("contact_list.txt", "r") as file:
            print("\n")
            for line in file:
                print(line.strip())
        print("Your contacts have been successfully imported from contact_list.txt")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please make sure the file exists!")

# contact_management_system() is the main function that runs the contact management system. It displays a menu with options for different operations (adding, 
# editing, deleting, searching, displaying, exporting, importing contacts and quitting the program). Based on the user's input, it calls the corresponding 
# function to perform the selected operation.

def contact_management_system(contacts):

    while True:
        print("\nWelcome to our Contact Management System!")
        print("\nMenu:")
        print("1. Add a new conctact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

        choice = input("\nWhat would you like to do? Enter your choice from 1 to 8: \n")
        if choice == "1".strip():
            add_new_contact(contacts)
            print(f"\n{contacts}")
        elif choice == "2".strip():
            edit_exisiting_contact(contacts)
        elif choice == "3".strip():
            delete_contact(contacts)
        elif choice == "4".strip():
            search_contact(contacts)
        elif choice == "5".strip():
            display_contacts(contacts)
        elif choice == "6".strip():
            export_contacts(contacts)
        elif choice == "7".strip():
            import_contacts(contacts)
        elif choice == "8".strip():
            print("\nThank you for using our program!\n")
            break
        else:
            print("\nPlease enter a valid response!\n")

contact_management_system(contacts)