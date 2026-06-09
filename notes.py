from cryptography.fernet import Fernet
import os

# -----------------------------
# Generate Key
# -----------------------------
def generate_key():

    key = Fernet.generate_key()

    with open(
        "key.key",
        "wb"
    ) as key_file:

        key_file.write(key)


# -----------------------------
# Load Key
# -----------------------------
def load_key():

    with open(
        "key.key",
        "rb"
    ) as key_file:

        return key_file.read()


# Generate key if not exists
if not os.path.exists(
    "key.key"
):

    generate_key()


# Encryption Object
key = load_key()

cipher = Fernet(key)


# -----------------------------
# Add Note
# -----------------------------
def add_note():

    note = input(
        "\nEnter note: "
    )

    encrypted_note = cipher.encrypt(
        note.encode()
    )

    with open(
        "notes.dat",
        "ab"
    ) as file:

        file.write(
            encrypted_note + b"\n"
        )

    print(
        "Note saved securely!"
    )


# -----------------------------
# View Notes
# -----------------------------
def view_notes():

    if not os.path.exists(
        "notes.dat"
    ):

        print(
            "\nNo notes found."
        )

        return

    print("\nSecure Notes:")

    with open(
        "notes.dat",
        "rb"
    ) as file:

        lines = file.readlines()

        for i, line in enumerate(
            lines,
            start=1
        ):

            decrypted_note = cipher.decrypt(
                line.strip()
            ).decode()

            print(
                f"{i}. {decrypted_note}"
            )


# -----------------------------
# Main Menu
# -----------------------------
while True:

    print(
        "\n===== Secure Notes App ====="
    )

    print(
        "1. Add Note"
    )

    print(
        "2. View Notes"
    )

    print(
        "3. Exit"
    )

    choice = input(
        "Enter choice: "
    )

    if choice == "1":

        add_note()

    elif choice == "2":

        view_notes()

    elif choice == "3":

        print(
            "Goodbye!"
        )

        break

    else:

        print(
            "Invalid choice!"
        )
