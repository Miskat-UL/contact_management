contact_lists = []

# update some codes


# tofayel please add other functions!

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


#delete function updated.. # tofayel please check

def delete(name):
    global contact_lists
    contact_lists = [_ for _ in contact_lists if _['name'] != name]
    print(f'Contact name: {name} is successfully deleted')


