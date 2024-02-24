from classes import AddressBook, Record


def parse_input(user_input: str) -> tuple:
    """Command recognition"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    """Error handling ValueError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter correct data."

    return inner


@input_error
def add_contact(args, book: AddressBook):
    """Adding a contact."""
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return "Contact added."


def change_error(func):
    """Error handling ValueError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter correct data in the format (Change 'name' 'old contact' 'new contact')"

    return inner


@change_error
def change_contact(args, book: AddressBook) -> str:
    """Overwriting a contact"""
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Name not found."
    else:
        record.edit_phone(old_phone, new_phone)
        return "Contact changed."


def phone_error(func):
    """Error handling IndexError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Contact not found!"

    return inner


def phone_key_error(func):
    """Error handling KeyError"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found!"

    return inner


@phone_key_error
@phone_error
def show_phone(args, book) -> str:
    """Contact output by given name."""
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    else:
        return ", ".join(str(phone) for phone in record.phones)


def show_all(book: AddressBook) -> str:
    """Output of all contacts!"""
    if book:
        return book
    else:
        return "There is no contact!"


@input_error
def add_birthday(args, book: AddressBook):
    """Adding a birthday."""
    name, birthday = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    """Date of birth by contact."""
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    else:
        return record.birthday


@input_error
def birthdays(book: AddressBook):
    """Bringing birthdays forward by 7 days."""
    return book.get_upcoming_birthdays()


def main():
    """'The main program."""
    book = AddressBook()
    print("""Welcome to the assistant bot!""")
    while True:
        while True:
            user_input = input("Enter a command: ")
            if user_input:
                break
            else:
                print("You have not provided a command!")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
