cars = ["BMW", "AMG", "BYD", "FORD", "KTM"]

if "bmw".upper() in cars:
    print("hello world")

a = 2
if a == 1:
    print("yes 1")
elif a == 2:
    print("yes 2")
else:
    print("yes 3")

alien = input("please input alien color:\n")
alien_color = ["green", "red", "yellow"]
if alien == "green":
    print("you get 5 point")
else:
    print("you lose")

users = ["admin", "lange", "stone"]

for user in users:
    if user == "admin":
        print("welcome " + user + ",would you like to see a status report")
    else:
        print("welcome back " + user)
