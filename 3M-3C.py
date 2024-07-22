
print("\tGame Start\nNow the task is to move all of them to the right side of the river") 
print("Rules:\n1. The boat can carry at most two people\n2. If cannibals outnumber missionaries, the missionaries will be eaten\n3. The boat cannot cross the river empty") 

left_missionaries = 3
left_cannibals = 3
right_missionaries = 0
right_cannibals = 0
attempts = 0

print("\nM M M C C C |  --- | \n")

try: 
    while True: 
        while True: 
            print("Left side -> right side river travel") 
            move_missionaries = int(input("Enter number of Missionaries traveling => "))	 
            move_cannibals = int(input("Enter number of Cannibals traveling => ")) 

            if move_missionaries == 0 and move_cannibals == 0: 
                print("Empty travel not possible. Re-enter: ") 
            elif (move_missionaries + move_cannibals) <= 2 and (left_missionaries - move_missionaries) >= 0 and (left_cannibals - move_cannibals) >= 0: 
                break
            else: 
                print("Invalid input. Re-enter: ") 

        left_missionaries -= move_missionaries 
        left_cannibals -= move_cannibals 
        right_missionaries += move_missionaries 
        right_cannibals += move_cannibals 

        print("\n") 
        print("M " * left_missionaries + "C " * left_cannibals + "| --> | " + "M " * right_missionaries + "C " * right_cannibals + "\n") 

        attempts += 1

        if (left_cannibals > left_missionaries > 0) or (right_cannibals > right_missionaries > 0): 
            print("Cannibals eat missionaries:\nYou lost the game") 
            break

        if (right_missionaries + right_cannibals) == 6: 
            print("You won the game! \n\tCongratulations") 
            print("Total attempts: ", attempts) 
            break

        while True: 
            print("Right side -> Left side river travel") 
            return_missionaries = int(input("Enter number of Missionaries traveling => ")) 
            return_cannibals = int(input("Enter number of Cannibals traveling => ")) 
            
            if return_missionaries == 0 and return_cannibals == 0: 
                print("Empty travel not possible. Re-enter: ") 
            elif (return_missionaries + return_cannibals) <= 2 and (right_missionaries - return_missionaries) >= 0 and (right_cannibals - return_cannibals) >= 0: 
                break
            else: 
                print("Invalid input. Re-enter: ") 

        left_missionaries += return_missionaries 
        left_cannibals += return_cannibals 
        right_missionaries -= return_missionaries 
        right_cannibals -= return_cannibals 

        attempts += 1

        print("\n") 
        print("M " * left_missionaries + "C " * left_cannibals + "| <-- | " + "M " * right_missionaries + "C " * right_cannibals + "\n") 

        if (left_cannibals > left_missionaries > 0) or (right_cannibals > right_missionaries > 0): 
            print("Cannibals eat missionaries:\nYou lost the game") 
            break
except EOFError as e: 
    print("\nInvalid input. Please retry!")
