from printer import print_status, print_all_contact

def add_contact(contacts: list[dict]):
    first_name = input("first name: ")
    last_name = input("last name: ")
    phone = input("phone: ")
    group = input("group (family, friend, work, other): ")

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })

    print_status('success')

def show_all_contact(contacts: list[dict]):

    if contacts:
        print_all_contact(contacts)
    else:
        print_status('error')

def search_contact(contacts: list[dict]):
    keyword = input("Search by name or phone: ").lower()
    results = [c for c in contacts if keyword in c['first_name'].lower() or
                                     keyword in c['last_name'].lower() or
                                     keyword in c['phone']]
    if results:
        print_all_contact(results)
    else:
        print_status('not_found')

def delete_contact(contacts: list[dict]):
    phone = input("Enter phone to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print_status('deleted')
            return
        
    print_status('not_found')  

def update_contact(contacts: list[dict]):
    phone = input("Enter phone to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contact['first_name'] = input("new first name: ")
            contact['last_name'] = input("new last name: ")
            contact['group'] = input("new group: ")
            print_status('updated')
            return
    print_status('not_found')

