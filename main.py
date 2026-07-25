import secrets


LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

def main():
    length = get_length()
    flags = get_flags()
    password = generate_password(length, flags)
    print(f"=============\nGenerated password: {password}\n=============")

def get_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            elif length > 128:
                print("Password length must not exceed 128.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")



def get_flags():
    while True:
        nums = input("Include numbers? (y/n): ").lower()
        letters = input("Include capital letters? (y/n): ").lower()
        special = input("Include special characters? (y/n): ").lower()
        if nums not in ['y', 'n'] or letters not in ['y', 'n'] or special not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        if nums == 'n' and letters == 'n' and special == 'n':
            print("At least one character type must be selected.")
            continue
        break
    return (nums == 'y', letters == 'y', special == 'y')

def generate_password(length, flags):
    nums, letters, special = flags
    available_characters = LOWERCASE
    password = []

    if nums:
        available_characters += DIGITS
        password.append(secrets.choice(DIGITS))
    if letters:
        available_characters += UPPERCASE
        password.append(secrets.choice(UPPERCASE))
    if special:
        available_characters += SPECIAL
        password.append(secrets.choice(SPECIAL))

    for _ in range(length - len(password)):
        password.append(secrets.choice(available_characters))
    secrets.SystemRandom().shuffle(password)
    password = ''.join(password)
    
    return password

main()