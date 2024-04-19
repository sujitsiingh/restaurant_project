import items
def validate(password):
    dgt = 0
    uc = 0
    lc =0
    sc =0
    if len(password) >= 6:
        for i in password:
            if i.isdigit():
                dgt += 1
            elif i.islower():
                lc += 1
            elif i.isupper():
                uc += 1
            elif i == '@' or i == '#' or i == '$' or i == '&' or i == '!' or i == '%' or i == '^' or i == '*':
                sc += 1
        if dgt >= 1 and lc >= 1 and uc >= 1 and sc >= 1:
            return 'valid'
        else:
            if dgt == 0:
                print("Password Must contain a Digit")
            if lc == 0:
                print("Password must contain a lower case")
            if uc == 0:
                print("Password Must contain a upper case")
            if sc == 0:
                print("Password Must contain a special character")
            return 'invalid'
    else:
        print("Length must be equal or more than six")
        return 'invalid'
                
def login():
    print("\n\t\t\t\t-----Customer Page-----")
    print("1: New User\n2: Existing User")
    ch=input("Enter (1/2):")
    if ch == '1':
        fp = open("Customer.txt",'r')
        L1 = fp.readlines()
        fp.close()
        List = []
        for i in L1:
            i = i.rstrip().split(",")
            List.append(i[0])  
        while True:
            name = input("Enter a unique Name:")
            if name in List:
                print("Name Exist!!")
                continue
            else:
                break
        p = input("Enter Password which Must be atleast 6 character Long,atleast one uppercase,one lowercase,one number and one special Character:")
        c = validate(p)
        while c != 'valid':
            p = input("Enter Password:")
            c = validate(p)
        detail = name+","+p+"\n"
        print("^^^^^*Account Created Successfully*^^^^^")
        fp = open("customer.txt",'a')
        fp.write(detail)
        fp.close()
        items.itemlist()
    elif ch == '2':
        name=input("Enter name:")
        p = input("Password:")
        fp = open("Customer.txt",'r')
        c1 = 0
        L = fp.readlines()
        fp.close()
        for i in L:
            i = i.rstrip().split(",")
            if i[0] == name:
                c1 = 1
                
                while i[1] != p:
                    print("Wrong Password!!!")
                    p = input("password:")
                if i[1] == p:
                    print("--Logged in successful--")
                    items.itemlist()
        if c1==0:
            print("User Doesn't Exist")
            print("Re-Enter To Restaurant And create An Account")
            login()

