def dispatch():
    print("-------Live Orders------\n")
    fp = open("Order List.txt",'r')
    print(fp.read())
    fp.close()
    disp_num = input("Enter Order Number To be Dispatched:")
    fp = open("Order List.txt",'r')
    f1 = fp.readlines()
    fp.close()
    list1 = []
    c = 0
    for i in f1:
        if disp_num == i.rstrip().split("->")[0]:
            c = 1
            continue
        else:
            list1.append(i)
    if c == 1:
        fp = open("Order List.txt",'w')
        fp.writelines(list1)
        fp.close()
        print("\n------Order Dispatched Successfully------")
    else:
        print("\nOrder Number Entered Not In Order List")
        
