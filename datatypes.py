# current_age=20
# print("After 10 years age=",current_age+10)

# first_name=input("Please enter first name")
# second_name=input("Please enter second name")
# age=input("Please enter  your age")
# print(type(age))
# name=first_name+" "+second_name+" "+str(int(age)+10) #age is a string here so it has to be converted to int
# print(name)
#...................................................
# game_list=["Cricket","Football","volleyball","hockey"] # this is a list and the index is 0,1,2,3 0= cricket
# print(game_list[0:1])
# if "Football" in game_list: #if "Football" and /or "hockey" in game_list:
#     print("Biggest game in the world")
# elif "Cricket" in game_list:
#     print("second largest game in the world")
# else:
#     print("Couldn't find your choice")
# myfile=open("list_test.txt","a") #creating a list file in txt ,"a" append mode 
# for game in game_list:
#     print(game)
#     myfile.write(game)
#     myfile.write("\n")

my_name="NIDHIN"
for letter in my_name:
    #print(letter)
    if letter.isupper():
        #lower_case=letter.lower() # letter.lower is stored to a variable called lower_case
        #print(lower_case) # 1st method to convert capital letter to small letter
        print(letter.lower())# converting from capital letter to small letter
        print(letter)
