def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    name, phone = args

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: list[str], contacts: dict) -> str:
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts found."

    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)

def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("Invalid command.")
            continue

        try:
            command, args = parse_input(user_input)

            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break

                case "hello":
                    print("How can I help you?")

                case "add":
                    print(add_contact(args, contacts))

                case  "change":
                    print(change_contact(args, contacts))

                case "phone":
                    print(show_phone(args, contacts))

                case "all":
                    print(show_all(contacts))

                case _:
                    print("Invalid command.")

        except (ValueError, IndexError):
            print("Invalid command.")


if __name__ == "__main__":
    main()