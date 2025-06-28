from termcolor import colored

def print_menu():
    colored_menu_text = colored("""
========= MENU =========
1. Add Contact 
2. Show Contacts
3. Search Contact
4. Delete Contact
5. Update Contact
6. Exit
========================
""", "green")
    print(colored_menu_text)

def print_status(status: str):
    status_data = {
        'error': colored("Xatolik yuz berdi", 'red'),
        'success': colored("Muvaffaqiyatli bajarildi", 'green'),
        'not_found': colored("Kontakt topilmadi", 'yellow'),
        'deleted': colored("Kontakt o'chirildi", 'cyan'),
        'updated': colored("Kontakt yangilandi", 'blue'),
    }

    print(status_data.get(status, colored("Noma'lum status", 'magenta')))

def print_contact(contact: dict):
    print(colored(
        f"{contact['first_name']} {contact['last_name']} | {contact['phone']} |  {contact['group']}",
        'white'))

def print_all_contact(contacts: list[dict]):
    print(colored("Barcha kontaktlar:", 'cyan'))
    for contact in contacts:
        print_contact(contact)
