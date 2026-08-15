inventory = []
papers = []
lifes = 5
main_door_password = "3724"
main_door_unlocked = False
kitchen_locker_password = False #found or not
found_digits = []
#_________________________________________________________
def main_door():
    global main_door_unlocked , lifes
    print("The main door has a 4 digit Lock\n_ _ _ _\nNOTE: YOU NEED ALL THE & DIGITS TOGETHER TO ESCAPE!!")
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
        print("FOUND A PAPER it says -> \"7\"")
        found_digits.insert(1,7)
        print("FOUND A GAS LIGHTER! (ADDED TO INVENTORY)")
        inventory.append("gas_lighter")
#_________________________________________________________
def under_couch():
    print("Found a drawer key!! ADDED TO INVENTORY")
    inventory.append("drawer_key")
    print("FOUND A PAPER -> paper1 added to inventory")
    inventory.append("paper1")
    papers.append("paper1->Found under couch")
#_________________________________________________________
def open_paper(paper_number:int):
    global kitchen_locker_password
    if paper_number == 1:
        kitchen_locker_password = True #found
        inventory.remove("paper1")
        print("Kitchen LOCKER code : 9898")
    else:
        print("ee3wreb")
            
            
#_________________________________________________________
def enter_kitchen():
    global lifes
    locker_check = False
    got_password = False
    while not got_password:
        print("entered KITCHEN!!")
        print("There is a fridge , stove and a locker in the kitchen\n1.Open Fridge 2.Open Locker 3.use stove 4.Exit Kitchen")
        kitchen_choice = int(input())
        if kitchen_choice == 1:
            print("WATER BOTTLE FOUND IN THE FRIDGE : ADDED TO INVENTORY")
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
def inventory_printer():
    print("YOU HAVE FOUND")
    for index in range((len(found_digits))):
        print(index+1,".",found_digits[index],end=",")
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
          9. UNFOLD PAPERS 
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
            enter_kitchen()
        case 6:
            pass
        case 7:
            print("YOU HAVE ")
            for index in range((len(inventory))): #0 to len-1 (since range excludes the extreme end)
                print(inventory[index],end=" ")
        case 8:
            inventory_printer()
        case 9:
            print("YOU HAVE the following papers :\n",papers)
            paper_num = int(input("Enter the paper NUMBER you want to unfold"))
            open_paper(paper_num)
            
            
            
    