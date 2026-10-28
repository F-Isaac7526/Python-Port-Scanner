def length_Check(password):
    while len(password)<8:
        print("Weak, Password too short")
        password = str(input("Re-enter Your Password: "))
    if len(password)<12 and len(password)>=8:
        return int(1)
    else:
        return int(2)

def variety_check(password):
    with open("./10k-most-common.txt", 'r', encoding='utf-8') as file:
        for passwd in file:
            if password==password:
                return int(0)
            special_chars = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
    '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
    '}', '~']
            for char in password:
                if char in special_chars:
                    return int(1)
                else:
                    return int(0)

def common_Passwords(password):
    with open("10k-most-common.txt", "r", encoding="utf-8") as file:
        if password in file.read():
            return int(0)
        else:
            return int(1)

def main():
    password = str(input("Enter Your Password: "))
    score = variety_check(password) + common_Passwords(password) + length_Check(password)
    if score==4:
        return "Very Strong Password"
    elif score==3:
        return "Strong password"
    elif score==2:
        return "Medium Password"
    elif score==1:
        return "Weak Password"
    else: 
        return "Very Weak password"


print(main()) 