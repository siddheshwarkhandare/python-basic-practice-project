
def view():
     with open("passwaord_manager.txt","r")as f:
         for line in f.readlines():
             print(line.rstrip())
             



def add():
    account=input("enter your user name! ")
    pwd=input("enter your password! ")

    with open("passwaord_manager.txt","a") as f:
        print(account,"|",pwd,"\n",file=f)



while True:
    user_choice=input("wolude you like to add the password "
"or view the password or press q for quite! ").lower()
    if user_choice=="q":
        break
    if user_choice=="add":
        add()
    elif user_choice=="view":
        view()





