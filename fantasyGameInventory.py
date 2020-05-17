# This function display any inventor possible and add list to inventory 


# display inventory function
def displayInventory(inventory):

    print('Inventory: ')

    totalItem = 0

    for x,y in inventory.items():

        print(y,x)

        totalItem += y

    print()
    print('Total number of items: ', totalItem)

# Added inventory function
def addToInventory(inventory, addedItems):

    newInventory = {}

    for item in addedItems:
        newInventory.setdefault(item, 0)
        newInventory[item] = newInventory[item] + 1

    for x,y in newInventory.items():
        
        for u,v in inventory.items():
            if u == x:
                inventory[u] = inventory[u] + y
                
        inventory.setdefault(x,y)
    
        

    return inventory 

    

# test both function 

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)



