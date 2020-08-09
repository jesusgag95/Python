import random

def generate_password():
    upper = ['A','B','C','D','E','F','G']
    lower = ['a','b','c','d','e','f','g']
    symbols = ['!','?','#','/','(',')']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    characters = upper + lower + symbols + numbers
    password = []

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)
    
    password = ''.join(password)
    return password



def run():
    password = generate_password()
    print("Your password is: " + password)


if __name__ == "__main__":
    run()