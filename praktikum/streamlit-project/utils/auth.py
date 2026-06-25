import os

FILE_USER = "data/users.txt"

def login_user(username, password):
    try:
        with open(FILE_USER, "r") as file:
            for line in file:
                u, p = line.strip().split(",")
                if u == username and p == password:
                    return True
        return False
    except FileNotFoundError:
        return False

def register_user(username, password):
    os.makedirs("data", exist_ok=True)
    with open(FILE_USER, "a") as file:
        file.write(f"{username},{password}\n")
    return True

