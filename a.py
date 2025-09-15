from cryptography.fernet import Fernet

# Uncomment this to generate a key once, then keep the generated "key.key" safe.
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()
                if '|' not in data:
                    continue  # Skip invalid lines
                user, passw = data.split("|")
                try:
                    decrypted_pwd = fer.decrypt(passw.encode()).decode()
                except Exception as e:
                    decrypted_pwd = "[Decryption Failed]"
                print("User:", user, "| Password:", decrypted_pwd)
    except FileNotFoundError:
        print("No passwords stored yet.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
