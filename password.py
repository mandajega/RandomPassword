import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvxyz!@#$%^&*()_+}{:"
length_password = int(input("Enter the length of the password : "))
a = "".join(random.sample(password, length_password))
print(f"Your password is {a}")
