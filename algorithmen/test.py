print("test")
print("willkommen")

from scheduling import first_come_first, unbekannt, test

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 zu first come first function!.")
    print("[2] Enter 2 zu andere Verfahren.")
    print("[3] Enter 3 zu andere Verfahren.")
    print("[q] Enter q zu beenden.")

    # Ask for the user's choice.
    choice = input("\nWas haben Sie Vor? ")
    n= input("Enter the nummber of processes:\n")
    bt= []

    print("Enter the burst time of the processes: \n")
    bt=list(map(int, raw_input().split()))




    # Respond to the user's choice.
    if choice == '1':
        first_come_first(n, bt)
    elif choice == '2':
        output, t= first_come_first_fun(n, bt)
        print(output,t)

    elif choice == '3':
        unbekannt(n,bt)
    elif choice == '4':
        test(n,bt)
    elif choice == 'q':
        print("\nVielen Danke.\n")
    else:
        print("\nVersuchen es nochmal.\n")

# Print a message that we are all finished.
print("Thanks again, bye now.")
