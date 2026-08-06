file=open("inventory.txt","a")
while True:
    item=input("Enter item name (or type 'exit' to quit): ")
    if item=="exit":
        break;
    file.write(item+"\n")
file.close()