number=input("Please enter a non-zero number:")

def prime_number_check (num):
    if int(num)==1:
        print("1 is not a prime number")
    elif int(num)%2==1: #to find the reminder of entered number
        print("Entered number is a prime number")
    else:
        print("Entered number is not a prime number")

prime_number_check(number)