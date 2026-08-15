inventory = []
lifes = 5
main_door_password = "3724051"
main_door_unlocked = False
found_digits = []
#_________________________________________________________
def main_door():
    global main_door_unlocked , lifes
    print("The main door has a 7 digit Lock\n_ _ _ _ _ _ _\nNOTE: YOU NEED ALL THE & DIGITS TOGETHER TO ESCAPE!!")
    print("Enter 1. to enter the password 2.Exit searching password")
    PASSWORD_ENTER_CHOICE = int(input())
    if PASSWORD_ENTER_CHOICE == 1:
        USER_MAIN_DOOR_PASSWORD = input("ENTER THE PASSWORD : ")
        if USER_MAIN_DOOR_PASSWORD == main_door_password:
            main_door_unlocked = True
            print(main_door_unlocked)
            print("ESCAPE SUCCESSFULL")
            return
        else:
            print("WRONG PASSWORD LIFE -1 : TRY AGAIN")
            lifes -= 1
    else:
        print("GOING BACK TO THE ROOMS")
        return
#_________________________________________________________
def check_drawer():
    # global inventory (not needed since i am just modifying)
    if "drawer_key" not in inventory: #if drawer key is not there
        print("You need a key to open the door")
        return
    else: #if key is there
        print("Drawer Key USED!")
        inventory.remove("drawer_key")
        print("FOUND A PAPER -> \"1\"")
        found_digits.append(1) 
#_________________________________________________________
def under_couch():
    print("Found a drawer key!! ADDED TO INVENTORY")
    inventory.append("drawer_key")
#_________________________________________________________

    
print("YOU ARE IN A ROOM WHICH U HAVE TO ESCAPE : YOU HAVE 5 LIFES PLAY WISELY ")
while not(main_door_unlocked) and lifes != 0: #even if one is false game ends
    print("""
          PRESS:
          1. ENTER THE MAIN DOOR PASSWORD
          2. CHECK INSIDE THE HOUSE DRAWER
          3. CHECK INDISE THE HOUSE CUPBOARD
          4. CHECK UNDER THE COUCH
          5. ENTER THE KITCHEN
          6. ENTER THE BEDROOM
          7. CHECK INVENTORY
          8. CHECK PASSWORD DIGITS FOUND
          """)
    USER_CHOICE = int(input())
    match USER_CHOICE:
        case 1:
            main_door()
        case 2:
            check_drawer()
        case 3:
            pass
        case 4:
            under_couch()
        case 5:
            pass
        case 6:
            pass
        case 7:
            print("YOU HAVE ")
            for index in range((len(inventory))): #0 to len-1 (since range excludes the extreme end)
                print(inventory[index],end=" ")
        case 8:
            print("YOU HAVE FOUND")
            for index in range((len(found_digits))):
                print(found_digits[index],end=" ")
            
            
            
    