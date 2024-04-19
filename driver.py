import users
import owner
print("*"*100)
print("\t\t\t\t-----Welcome To Restaurant-----")
print("1: Customer\n2: Owner")
ch = input("Enter Your Choice (1/2): ")
if ch == '1':
    users.login()
elif ch == '2':
    pwd = input("Enter Your password:")
    if pwd == "Owner@123":
        owner.work()
    else:
        print("invalid Password")
else:
    print("Invalid Input!!")
    
