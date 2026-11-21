# holiday activity planner
# lesson: nested conditional statements
 
print("====================================")
print("    welcome to holiday planner!     ")
print("====================================")
print()
 
print("step 1: pick your holiday type")
print("  1 - beach holiday")
print("  2 - mountain holiday")
print()
 
choice = int(input("enter 1 or 2: "))
print()
 
if choice == 1:
    # nested if-else - runs only when choice is 1
    print("step 2: pick your beach activity")
    print("  1 - swimming")
    print("  2 - sandcastle building")
    print()
 
    beach_activity = int(input("enter 1 or 2: "))
    print()
 
    if beach_activity == 1:
        print("you picked  : swimming")
        print("best time   : morning")
        print("remember    : carry sunscreen and water")
    else:
        print("you picked  : sandcastle building")
        print("best time   : evening")
        print("remember    : carry a bucket and spade")
 
elif choice == 2:
    # nested if-else - runs only when choice is 2
    print("step 2: pick your mountain activity")
    print("  1 - hiking")
    print("  2 - camping")
    print()
 
    mountain_activity = int(input("enter 1 or 2: "))
    print()
 
    if mountain_activity == 1:
        print("you picked  : hiking")
        print("best for    : exploring trails")
        print("remember    : wear comfortable shoes")
    else:
        print("you picked  : camping")
        print("best for    : staying close to nature")
        print("remember    : carry a tent and flashlight")
 
else:
    print("that was not a valid choice.")
    print("please enter 1 for beach holiday or 2 for mountain holiday.")
 
print()
print("====================================")
print("   your holiday plan is ready!      ")
print("   enjoy your trip!                 ")
print("====================================")
