import items
import orders

def work():
    while True:
        print("-------What do you want to do?-------")
        print("\t1:Update Item List\n\t2:Dispatch Order\n\t3:View the item List\n\t4:close")
        ch = input("Enter:")
        if ch == '1':
            items.update()
        elif ch == '2':
            orders.dispatch()
        elif ch == '3':
            fp = open("items.txt",'r')
            print(fp.read())
            fp.close()
        elif ch == '4':
            print("="*60)
            print(" "*10,"-----^^^Thank You!^^^-----"," "*10)
            print("#"*60)
            break