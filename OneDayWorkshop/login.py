VALID_USERNAME = "johndoe"
VALID_PASSWORD = "secret1234"

def main():
    check = 'invalid'
    while check == 'invalid':
        username_input = input("username: ")
        password_input = input("password: ")
        if username_input == VALID_USERNAME:
            if password_input == VALID_PASSWORD:
                check = 'valid'
            else:
                print("try again")
        else:
            print("try again")

    print("You entered the system correctly")

main()
