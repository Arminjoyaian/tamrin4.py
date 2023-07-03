a = input()
b = int(input())
username = str(input("Enter user?"))
password = int(input("Enter pass?"))
if username == a:
    if password == b:
        print("It is transitive")
else:
    print ("is invalid")    
