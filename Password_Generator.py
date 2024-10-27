# Importing necessary libraries
import random as re  # Used for random sampling of characters for password generation
import time  # Used for delay in exit message display
import sys  # Used for system exit
from colorama import Fore, Back, Style, init  # Used for colored text output in the terminal

# Initialize colorama for colored output in the terminal
init(convert=True)

# Program starts
try:
    # Displaying welcome message in styled text
    print(Back.WHITE + "", end="")
    print(Fore.LIGHTMAGENTA_EX + "  Welcome  ")
    print(Style.RESET_ALL)

    # Function to initiate the password generation process
    def Loop1():
        try:
            while True:
                # Asking the user for desired password length
                print(Fore.LIGHTBLUE_EX + "")
                L = int(input("Enter the Length of Password: "))
                print(Style.RESET_ALL)

                # Character sets for password creation
                A = "qwertyuiopasdfghjklzxcvbnm"  # Lowercase letters
                B = "QWERTYUIOPASDFGHJKLZXCVBNM"  # Uppercase letters
                C = "123456890"  # Numbers
                D = "~!@#$%^&*()_:></*-"  # Special characters
                
                # Combining all character sets
                E = []
                E.extend(A)
                E.extend(B)
                E.extend(C)
                E.extend(D)

                # Generate a password of length L from the combined character set
                F = re.sample(E, L)

                # Check for valid password length
                if L < 6:
                    print(Fore.RED + "Please Enter the Length greater than 6")
                    Loop1()  # Restart if length is invalid

                elif L > 32:
                    print(Fore.RED + "Please Enter the Length Less than 32")
                    Loop1()  # Restart if length is invalid

                else:
                    # Display generated password
                    print(Fore.GREEN + "Your Password is: ", Fore.YELLOW + "".join(F))

                # Function for user choice after password generation
                def Loop3():
                    print(Fore.CYAN + "\nPress e to exit Or Press c to generate a new password")
                    
                    # User input to continue or exit
                    inp = input("Enter Your Choice: ")
                    
                    if inp == "e":
                        # Display exit message and close the program
                        print(Fore.LIGHTMAGENTA_EX + '''\n->Thanks For Using<-\n ->Have a nice Day<-\n->Created By Shivam Pathak<-''')
                        time.sleep(3.5)
                        sys.exit()
                    elif inp == "c":
                        # Restart password generation
                        Loop1()
                    else:
                        # Invalid input handling
                        print(Fore.RED + "Error 234:\nWrong input")
                        Loop3()

                # Call Loop3 for user input after generating a password
                Loop3()

        # Catch exceptions during password generation or user input
        except Exception as e:
            print(Fore.RED + "", end="")
            print(f"Please Try Again\nError: {e}")
            Loop1()  # Restart process on error

    # Initial function call to start the password generation process
    Loop1()

# Catch any exception during the initial setup or welcome message display
except Exception as e:
    print(Fore.RED + "", end="")
    print(Fore.RED + f"Please Try Again\nError: {e}")
    Loop1()
