data={"Spain":"Real Madrid","USA":"Inter-Miamy","India":"Blasters"}
print(data["India"])#india is the key here blasters is the value
for country in data:
    print(country)# to print the key values from the dictionary (default method)
    print(country,data[country])# printing key and values together.In the for loop variable "country" has the key data from dictionary
    