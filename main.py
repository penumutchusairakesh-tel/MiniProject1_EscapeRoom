inventory = []
lifes = 5
main_door_password = "3724051"
main_door_unlocked = False
def main_door():
    global main_door_unlocked
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
    
print("YOU ARE IN A ROOM WHICH U HAVE TO ESCAPE : YOU HAVE 5 LIFES PLAY WISELY ")
while not(main_door_unlocked) and lifes != 0: #even if one is false game ends
    print("""
          PRESS:
          1. ENTER THE MAIN DOOR PASSWORD
          2. CHECK INSIDE THE HOUSE DRAWER
          3. CHECK INDISE THE HOUSE CUPBOARD
          4. CHECK UNDER THE COUCH
          4. ENTER THE KITCHEN
          5. ENTER THE BEDROOM
          6. ENTER THE BATHROOM
          """)
     
    