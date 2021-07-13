contact_lists = []

# update some codes


def create():
    name = input('Enter his/her name: ')
    number = input(f"Enter {name}'s number: ")
    email = input(f"Enter {name}'s email: ")

    contact_lists.append(
        {
            'name': name,
            'number': number,
            'email': email,

            "email2":None,
           " contact2":None,

            'extra number': None

        }
    )


def show():
    return contact_lists


def delete(name):
    global contact_lists
    contact_lists = [_ for _ in contact_lists if _['name'] != name]
    print(f'Contact name: {name} is successfully deleted')


# Tofayel, Please check this section EDIT function. Add something to this function so that user can edit all information of a contact

def edit(name):
    for _ in contact_lists:
        if name in _['name']:
            print('found the contact. retriving full information: ')
            print(
                f"Name: {_['name']}, Number:{_['number']}, Email:{_['email']}")
            edit_choice = input("""
            which field do you want to edit
            press 1 - For Edit Name
            Press 2 = For Edit Number
            Press 3 - For Edit Email
            """)
            if edit_choice == '1':
                re_name = input("Rename the contact: ")
                _['name'] = re_name

            elif edit_choice == '2':
                re_number = input("Renumber the contact: ")
                _['number'] = re_number

            elif edit_choice == '3':
                re_mail = input("Edit Mail with: ")
                _['email'] = re_mail
            print(f"After edit {_['name']}, {_['number']},{_['email']}")
            break
    else:
        print("contact not found")


def search(name):
    for _ in contact_lists:
        if name in _['name']:
            print('found the contact. retriving full information: ')
            print(
                f"Name: {_['name']}, \nNumber:{_['number']}, \nEmail:{_['email']}")





def multiplecontact(name):
    for _ in contact_lists:
        if name in _['name']:
            print('found the contact. retriving full information: ')
            print(
                f"Name: {_['name']}, Number:{_['number']}, Email:{_['email']}")
            edit_choice = input("""
            which field do you want to edit
            
            Press 1 = For Edit Number
            Press 2 - For Edit Email
            """)
            if edit_choice == '1':
                re_contact = input("Rename the contact: ")
                _['contact2']=re_contact


            elif edit_choice == '2':
                re_number = input("Renumber the mail: ")
                _['email'] = re_number


            print(f"After edit {_['name']}, {_['number']},{_['contact2']},{_['email']}")
        else:
            print("contact not found")

def multiple_number(name):
    for _ in contact_lists:
        if _['name'] == name:
            print(f"Contact Found! Name: {_['name']}")
            add_number = input('Add Extra number: ')
            _["extra number"] = add_number
            break

    else:
        print('contact not found! ')



