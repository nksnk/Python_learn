data_base={"Nidhin":"1234","Vipin":"007"}
def login(): # a function
    for chance in range(3):
        user_name=input("Please enter your user name:")
        password=input("Please enter password:")
        if user_name in data_base:
            if password==data_base[user_name]:
                print("Welcome")
                break
            else:
                print("Wrong password")

        else:
            print("Access denied")
#login() #to call the function here           
