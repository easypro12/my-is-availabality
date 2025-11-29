def storage():
 store=["car","book","food","water","fruit","human","house"]


 while True:
    print("\n storage menu")
    print("1.display")
    print("2.add")
    print("3.delete")
    print("4.exit")

    select=input("select choice:")



    if select=="1":
     print("\n item in storage menu")
     for item in store:
         print("-",item)


    elif select =="2":
     new_item=input("add item:")
     store.append(new_item)
     print(f"{new_item} added successfully")


    elif select =="3":
     item_to_remove=input("enter item to remove:")
     if item_to_remove in store:
       store.remove(item_to_remove)
       print(f"{item_to_remove} removed successfully")

     else:
      print("item not in store")

    elif select=="4":
        print("exiting storage")

enter_store=input("enter storage again(yes/no):")
if enter_store!="yes":
 print("try again")
storage()