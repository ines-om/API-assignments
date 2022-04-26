print("--- Password validation v.2 ---")

password = "1001001"
username = "ines-037"

user = str(input("Insert username here: "))
passw = str(input("Insert password here: "))

user_l = [user]
pass_l = [passw]

for pas in pass_l:
    if (passw == password and user != username) or (passw != password and user == username):
        print("Username and password don't correspond.")
    if user != username:
        print("Username might not exist, re-check your input.")
        user = str(input("Insert username here: "))
        passw = str(input("Insert password here: "))
        user_l.append(user)
        pass_l.append(passw)
    if (passw != password and user == username):
        print("Wrong password, try again.")
        passw = str(input("Insert password here: "))
        pass_l.append(passw)

if (passw == password and user == username):
    print("Successful login.")
    print("WELCOME!")
