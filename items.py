import random
def itemlist():
    order_num = random.randint(100,500) + random.randint(600,1000)
    print("="*100)
    print("="*100)
    print("\t\t\t\t-----Item List-----")
    fp = open('items.txt','r')
    print(fp.read())
    fp.close()
    
    fp = open('items.txt','r')
    l2 = fp.readlines()
    fp.close()
    d = {}
    total = 0
    while True:
        num = input("Choose Your Dish Number:")
        q = int(input("Enter Quantity:"))
        flag =0
        for i in l2:
            i = i.rstrip().split(',')
            if num == i[0]:
                flag = 1
                if i[1] not in d.keys():
                    d[i[1]] = q
                else:
                    d[i[1]] += q
                total += d[i[1]] * int(i[2])
        if flag == 0:
            print("invalid Dish Number:")
        ch = input("\nEnter 'y' to choose another Dish:").upper()
        if ch == 'Y':
            continue
        else:
            break
    detail = '->'
    print("="*100)
    print("\n-------Your Order-------\n")
    print(f"Order Number: {order_num}\n")
    [print(key,":",value) for key,value in d.items()]
    print(f"\n------>","\U0001F4B0","Total Amount: Rs", {total},"<------")

    for i in d:
        detail=detail + i + "- " + str(d[i]) +','
    detail = str(order_num) + detail
    print(detail)    

    ch1 = input("\nEnter 'y' To confirm Your Order:").upper()
    if ch1 == 'Y':
        fp = open("Order List.txt",'a')
        fp.write(detail)
        fp.close()
        print("-"*60)
        print(" "*10,"Your Order Has Been Recieved! Visit Again"," "*10)
        print("-"*60)
    else:
        print("*"*30,end='')
        print("Thank You! ReLogin For a new Order")
        print("*"*35,end='')
    
def update():
    print("\n----What Do You Want To change in Item List----\n")
    print("1:Add an item to List\n2:Delete an Existing Item from List\n3:Update The price of an Item in the List\n")
    ch = input("Enter Your Choice(1/2/3/4): ")
    c = 0
    detail = ''
    fp = open("items.txt",'r')
    list_ = fp.readlines()
    fp.close()
    if ch == '1':
        unique_num = input("Enter Unique Item Number: ")
        item_name = input("Enter Name Of Item To be Added: ")
        price = input("Enter Price Of the The Item: ")
        for i in list_:
            i = i.rstrip().split(',')
            if unique_num == i[0]:
                break
            else:
                c += 1
        if c == len(list_):
            detail = unique_num+','+item_name+','+price+'\n'
            print("\n---^^^---Item Successfully Added---^^^---")
        else:
            print(" Item Already Present In The Item List")
        
        fp = open("items.txt",'a')
        fp.write(detail)
        fp.close()
    elif ch == '2':
        c = 0
        l1 = []
        delete_num = input("Enter The Item Number To be Deleted:")
        for i in list_:
            if delete_num == i.rstrip().split(',')[0]:
                c = 1
                continue
            else:
                l1.append(i)
        if c == 1:
            print("\n---##---Item Deleted Successfully---##---")   
            fp = open("items.txt",'w')
            fp.writelines(l1)
            fp.close()
        else:
            print("\n------Item Not Present in The List------")
    elif ch == '3':
        num = input("Enter Item Number:")
        udt_p = input("Enter Updated Price:")
        d = udt_p.isdigit()
        if d == True:
            for i in range(len(list_)):
                if num in list_[i]:
                    s = list_[i].rstrip().split(',')
                    list_[i]=num+','+s[1]+','+udt_p+'\n'
                    print("\n------Price Was Updated------")
                    break

            else:
                 print("\n------Item Not Present in The List------")
            fp = open("items.txt",'w')
            fp.writelines(list_)
            fp.close()
        else:
            print("Invalid Type Of Price!!")
    else:
        print("Invalid Choice!!")