from tabulate import tabulate
Test=True
item_test=False
shop_list=[]
shop_table = [
    ["","Nikhil", "Delhi"],
    ["a","Ravi", "Kanpur"],
    ["b","Manish", "Ahmedabad"],
    ["c","Prince", "Bangalore"]
]
headers = ["Items", "number",]
while Test :
    item_test = False
    print("------------------------------------")
    print("• Add an item")
    print("• Remove an item")
    print("• Search for an item")
    print("• Show inventory")
    print("• Exit")
    print("------------------------------------")
    choice=int(input("Choose an Option (pick a number/ ex;Add an item is 1) : "))
    shop_table = [
        [choice,item , "Delhi"],

    if choice == 1 :
        while item_test == False :
             Item=input("Type an item to add to your shop list : ")
             if Item != "":
                shop_list.append(Item)
                print(Item,"is added")
             item_test=Item!=""
    if choice == 2 :
        Item_remove = input("Type an item to remove from your shop list : ")
        if Item_remove in shop_list :
            shop_list.remove(Item_remove)
            print("Item ",Item_remove ," Has been removed")
        else :
            print("Item ",Item_remove ," not Found !")
    if choice == 3:
        Item_search = input("Type an item to Search in your shop list : ")
        if Item_search in shop_list :
            print("the Item is in the shop list")
        else :
            print("The Item is not in the shop list")
    if choice == 4 :
        if not shop_list:
            print("the shop list is empty")
        else:
            print(shop_list)
    if choice == 5 :
        Test=False





