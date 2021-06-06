def greeting(user):
    return (f"hello {user}, welcome to our system")

if __name__ == '__main__':
    user = input("Enter your username : ").capitalize()
    greeting1 = greeting(user)
    print(greeting1)
    print("Prueba")
