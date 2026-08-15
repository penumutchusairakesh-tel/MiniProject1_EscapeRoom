inventory = []
papers = []
lifes = 5
main_door_password = 3724
main_door_unlocked = False
kitchen_locker_password = False #found or not
bedroom_locker_password = False #found or not
found_digits = []
fridge_open = False
closet_open = False
drawer_open = False
couch_under = False
#_________________________________________________________
def main_door():
    global main_door_unlocked , lifes
    print("The main door has a 4 digit Lock\n_ _ _ _\nNOTE: YOU NEED ALL THE & DIGITS TOGETHER TO ESCAPE!!")
    print("Enter 1. to enter the password 2.Exit searching password")
    PASSWORD_ENTER_CHOICE = int(input())
    if PASSWORD_ENTER_CHOICE == 1:
        USER_MAIN_DOOR_PASSWORD = int(input("ENTER THE PASSWORD : "))
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
    global drawer_open
    if drawer_open:
        print("ALREADY OPENED!!")
        return
    # global inventory (not needed since i am just modifying)
    if "drawer_key" not in inventory: #if drawer key is not there
        print("You need a key to open the drawer")
        return
    else: #if key is there
        drawer_open = True
        print("Drawer Key USED!")
        inventory.remove("drawer_key")
        print("FOUND A PAPER it says -> \"7\"")
        found_digits.insert(1,7)
        print("FOUND A GAS LIGHTER! (ADDED TO INVENTORY)")
        inventory.append("gas_lighter")
#_________________________________________________________
def under_couch():
    global couch_under
    if couch_under:
        print("ALREADY CHECKED!!!")
        return
    print("Found a drawer key!! ADDED TO INVENTORY")
    couch_under = True
    inventory.append("drawer_key")
    print("FOUND A PAPER -> paper1 added to inventory")
    inventory.append("paper1")
    papers.append("paper1->Found under couch")
#_________________________________________________________
def open_paper(paper_number:int):
    global kitchen_locker_password, bedroom_locker_password
    if paper_number == 1:
        kitchen_locker_password = True #found
        inventory.remove("paper1")
        papers.remove("paper1->Found under couch")
        print("Kitchen LOCKER code : 9898")
    elif paper_number == 2:
        bedroom_locker_password = True
        inventory.remove("paper2")
        papers.remove("paper2 -> FOUND IN KITCHEN LOCKER")
        print("Bedroom Locker code : 2307")
    elif paper_number == 3:
        inventory.remove("paper3")
        papers.remove("paper3 -> FOUND IN BEDROOM CLOSET")
        print("NUMBER : 3")
        found_digits.insert(0,3)
    elif paper_number == 4:
        inventory.remove("paper4")
        papers.remove("paper4 -> FOUND IN THE CLOSET")
        print("NUMBER : 2")
        found_digits.insert(2,2)
        
    else:
        print("Try Again!")
            
            
#_________________________________________________________
def enter_kitchen():
    global lifes , fridge_open
    locker_check = False
    got_password = False
    
    print("entered KITCHEN!!")
    while not got_password:
        print("There is a fridge , stove and a locker in the kitchen\n1.Open Fridge 2.Open Locker 3.use stove 4.Exit Kitchen")
        kitchen_choice = int(input())
        if kitchen_choice == 1:
            if fridge_open:
                print("ALREADY OPENED!!")
                return
            print("WATER BOTTLE FOUND IN THE FRIDGE : ADDED TO INVENTORY")
            fridge_open = True
            inventory.append("water_bottle")
        elif kitchen_choice == 2:
            if kitchen_locker_password: #if kitchen_locker_password is true then try the password
                while not locker_check and lifes !=0:
                    print("Enter locker password")
                    kitchen_password = int(input())
                    if kitchen_password == 9898:
                        locker_check = True
                        print("FOUND A THERMAL PLATE : ADDED TO INVENTORY ")
                        inventory.append("thermal_plate")
                        print("hint : NEEDS HEAT TO REVEAL ITS CONTENT ")
                        print("Found a paper -> paper2 added to inventory")
                        inventory.append("paper2")
                        papers.append("paper2 -> FOUND IN KITCHEN LOCKER")
                    else:
                        print("TRY AGAIN:")
                        lifes -= 1
            else:
                print("FIND THE PASSWORD FIRST!!")
                return
        elif kitchen_choice == 3:
            if "gas_lighter" not in inventory:
                print("You need a gas lighter to use this")
                return
            else:
                if "water_bottle" not in inventory or "thermal_plate" not in inventory: #user must have both
                    print("YOU NEED WATER BOTTLE AND THERMAL PLATE")
                else:
                    print("press 'e' to light the stove")
                    temp_cmd = input()
                    if temp_cmd.lower() == 'e':
                        print("stove is now lit")
                        inventory.remove("gas_lighter")
                        temp_cmd = input("Press 'f' PUT WATER IN THE POT ").lower()
                        if temp_cmd == 'f':
                            print("water has been poured and its boiling")
                            inventory.remove("water_bottle")
                            print("USING THE THERMAL PLATE!!")
                            inventory.remove("thermal_plate")
                            print("THE THERMAL PLATE SAYS : 4")
                            found_digits.insert(3,4)
                            got_password = True
                        else:
                            #HEAVY 'WANTED' PUNISHMENT -> for carelessness
                            print("CANT PRESS A LETTER , YOU CANT ESCAPE THIS ENDING THE GAME!!")
                            lifes = 0
                            return
                    else:
                        print("CANT PRESS A LETTER , YOU CANT ESCAPE THIS ENDING THE GAME!!")
                        lifes = 0
                        return
        else:
            print("EXITING KITCHEN!!")
            return
#_________________________________________________________   
def enter_bedroom():
    global lifes
    print('Entered BEDROOM!')
    got_bedpassword = False
    bedlock_unlocked= False
    while not got_bedpassword:
        print("there is a 1. LOCKER 2. DRAWER(LOCKED) 3. SlEEP 4. Exit")
        bed_choice = int(input())
        if bed_choice == 1:
            if bedroom_locker_password:
                while not bedlock_unlocked and lifes !=0 :
                    print("Enter Password! ")
                    password = int(input())
                    if password == 2307:
                        bedlock_unlocked = True
                        print("Found Bedroom Drawer Key -> ADDED TO INVENTORY!")
                        inventory.append("bed_drawer_key")
                    else:
                        print("Try AGAIN")
                        lifes -= 1
            else:
                print("FIND THE LOCKER PASSWORD!!!")
                return
        elif bed_choice == 2:
            if not bedlock_unlocked:
                print("FIND THE KEY FIRST !!")
            else:
                print("OPENING THE DRAWER")
                inventory.remove("bed_drawer_key")  
                print("found a paper3 -> ADDED TO INVENTORY")
                inventory.append("paper3")
                papers.append("paper3 -> FOUND IN BEDROOM CLOSET")
                print("Found CLOSET KEY -> ADDED TO INVENTORY")
                inventory.append("closet_key")
                got_bedpassword = True
                
        elif bed_choice == 3:
            print("YOU ARE IN A DEEP SLUMBER .... DREAMSSSSS...... THE NUMBER IS 3")
            print("YOU WOKE UPP")
            got_bedpassword = True
            found_digits.insert(0,3)
        else:
            print("EXITING BEDROOM")
            return  
#_________________________________________________________   
def check_closet ():
    global closet_open
    if closet_open:
        print("ALREADY OPENED!!")
        return
    if "closet_key" not in inventory:
        print("FIND THE KEY FIRST!!")
        return
    else:
        closet_open = True
        print("UNLOCKED THE CLOSET!!!")
        closet_open = True
        print("FOUND paper4 -> ADDED TO INVENTORY")
        inventory.append("paper4")
        papers.append("paper4 -> FOUND IN THE CLOSET")
        return
    
#_________________________________________________________   
                 
                 
def inventory_printer():
    for index in range((len(inventory))): #0 to len-1 (since range excludes the extreme end)
        print(index+1,inventory[index],end=" ")
#_________________________________________________________ 
    
print("YOU ARE IN A ROOM WHICH U HAVE TO ESCAPE : YOU HAVE 5 LIFES PLAY WISELY ")
while not(main_door_unlocked) and lifes != 0: #even if one is false game ends
    print("""
          PRESS:
          1. ENTER THE MAIN DOOR PASSWORD
          2. CHECK INSIDE THE HOUSE DRAWER
          3. CHECK INDISE THE HOUSE CLOSET
          4. CHECK UNDER THE COUCH
          5. ENTER THE KITCHEN
          6. ENTER THE BEDROOM
          7. CHECK INVENTORY
          8. CHECK PASSWORD DIGITS FOUND
          9. UNFOLD PAPERS 
          """)
    USER_CHOICE = int(input())
    match USER_CHOICE:
        case 1:
            main_door()
        case 2:
            check_drawer()
        case 3:
            check_closet()
        case 4:
            under_couch()
        case 5:
            enter_kitchen()
        case 6:
            enter_bedroom()
        case 7:
            print("YOU HAVE ")
            inventory_printer()
            
        case 8:
            print("YOU HAVE FOUND")
            for index in range((len(found_digits))):
                print(found_digits[index],end=",")
        case 9:
            print("YOU HAVE the following papers :\n",papers)
            paper_num = int(input("Enter the paper NUMBER you want to unfold "))
            open_paper(paper_num)
#_________________________________________________________   