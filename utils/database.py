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
            'email': email
        }
    )


def show():
    return contact_lists
