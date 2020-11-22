print("Roll number = IC-010")

# make a table of number that user entered

number = int(input("Enter a number: "))

print("TABLE OF" , number )

for i in range(1,11):
    print(number, "*" , i , "=" , number*i)