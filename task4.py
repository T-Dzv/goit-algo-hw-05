from functools import wraps
import re 

def main():
    contact_book = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contact_book))
        elif command == "change":
            print(change_contact(args, contact_book))
        elif command == "phone":
            print(show_phone(args, contact_book))
        elif command == "all":
            print(show_all(contact_book))
        else:
            print("Invalid command.")
        
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error_add(func): # decorator to work with Errors in add command
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError: 
            return "Please provide correct phone" # if phone is provided in wrong format
        except IndexError:
            return "Give me name and phone please." # if user didn't provide needed arguments with a command 
    return inner

@input_error_add
def add_contact(args: list, contact_book: dict):
    phone = int(re.sub(r"\+?", "", args[1])) # checking if phone is in correct format (only + and dygits)
    if args[0] in contact_book:
        return f"{args[0]} is already in contact book"
    else:
        contact_book[args[0]] = args[1]
        return "Contact added."

def input_error_change(func): # decorator to work with Errors in change command
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide correct phone" # if phone is provided in wrong format
        except IndexError:
            return "Give me name and phone please." # if user didn't provide needed arguments with a command 
        except KeyError:
            return f"There is no such contact in contact book" # if user tries to change phone for name that was't added yet
    return inner

@input_error_change
def change_contact(args: list, contact_book: dict):
    phone = int(re.sub(r"\+?", "", args[1])) # checking if phone is in correct format (only + and dygits)
    print(f"old {args[0]} phone was {contact_book[args[0]]}") # informing a user old phone of the contact
    contact_book[args[0]] = args[1]
    return "Contact updated."

def input_error_show(func): # decorator to work with Errors in phone command
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me name please." # if user didn't provide needed arguments with a command 
        except KeyError:
            return f"There is no such contact in contact book" # if user asks to show phone for non-exhisting contact
    return inner

@input_error_show
def show_phone(args: list, contact_book: dict):
    return contact_book[args[0]]

# in show_all function we don't need decorator, since typically no Errors are possible
def show_all(contact_book):
    if contact_book: 
        contact_book_str = ""
        for name, phone in contact_book.items():
            contact_book_str += f"{name}: {phone}\n"
        return contact_book_str
    else:
        return "Contact book is empty"

if __name__ == "__main__":
    main()
