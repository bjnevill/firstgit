correct_pin = "12345"
attempts = 0

while attempts < 3:
    pin = input("Enter pin: ")
    
    if pin == correct_pin:
        print("Correct pin entered.")
        break  
    else:
        attempts += 1
        tries_left = 3 - attempts

        if tries_left > 0:
            print("Invalid pin. Please try again.")
            print("You have {} tries left.".format(tries_left))
        else:
            print("Invalid pin. You have no more tries.")
            print("Your account is locked.")
