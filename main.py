import os
import platform
import colorama
from colorama import Fore, Style
colorama.init()

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def start():
    print(Fore.CYAN + 'Welcome to the Calculator Navigation Wizard. ' + Fore.WHITE + '(Developed by Bedanta Dey)')
    print('Type ' + Fore.GREEN + 'r ' + Fore.WHITE + 'to run the program, ' + Fore.GREEN + 'h ' + Fore.WHITE + 'for help, or ' + Fore.GREEN + 'q ' + Fore.WHITE + 'to exit.')

    run = input()
    
    if run == 'r':
        clear()
        main()
    elif run == 'q':
        clear()
        exit() 
    elif run == 'h':
        clear()
        print(Fore.YELLOW + "Welcome to the help section." + Fore.WHITE)
        print("1. Always use lowercase letters for input.")
        print("2. If your program exits with 'Exit Code: 1', then your input was invalid. Choose a valid input.")
        print("3. For calculations that involve more than 2 numbers, try calculating the value of them first, then involve")
        print("them with the final calculation. This is done to prevent invalid results like 'Can't divide by zero'.")
    
    cont = input('Press ' + Fore.GREEN + 'c ' + Fore.WHITE + 'to continue to the program. ')

    if cont == 'c':
        clear()
        start()

def main():

    print (Fore.YELLOW + "Welcome to the calculator.")

    

    print(Fore.BLUE + "Enter your first number: "+ Fore.WHITE)

    num1 = int(input())

    print(Fore.BLUE + "Enter your second number: "+ Fore.WHITE)

    num2 = int(input())

    print(Fore.BLUE + "Choose your operator:")
    print(Fore.GREEN + "a " + Fore.WHITE+ 'for Addition (+)')
    print(Fore.GREEN + "s " + Fore.WHITE+ "for Subtraction (-)")
    print(Fore.GREEN + "m " + Fore.WHITE+ "Multiplication (*)")
    print(Fore.GREEN + "d " + Fore.WHITE+ "for Division (/)")
    print(Fore.GREEN + "mo " + Fore.WHITE+ "for Modulus (%)")
    print(Fore.GREEN + "e " + Fore.WHITE+ "for Exponentiation (^)")
    print(Fore.GREEN + "fd " + Fore.WHITE+ "for Floor Division (//)")

    oper = input()

    if oper == 'a':
        add = num1 + num2
        print(Fore.BLUE + "The sum is: " + Fore.WHITE+ str(add))

    elif oper == 's':
        sub = num1 - num2
        print(Fore.BLUE + "The difference is: " + Fore.WHITE+ str(sub))

    elif oper == 'm':
        times = num1 * num2
        print(Fore.BLUE + "The product is: " + Fore.WHITE+ str(times))

    elif oper == 'd':
        quot = num1 / num2
        print(Fore.BLUE + "The quotient is: " + Fore.WHITE+ str(quot))

    elif oper == 'mo':
        mod = num1 % num2
        print(Fore.BLUE + "The answer is: " + Fore.WHITE+ str(mod))

    elif oper == 'e':
        exp = num1 ** num2
        print(Fore.BLUE + "The answer is: " + Fore.WHITE+ str(exp))

    elif oper == 'fd':
        fdr = num1 // num2
        print(Fore.BLUE + "The answer is: " + Fore.WHITE+ str(fdr))

    else:
        print(Fore.RED + "Encountered an error. Try again. (Exit Code: 1)")

    restart = input(Fore.WHITE +'Do you want to run the wizard again? [' + Fore.GREEN + 'y ' + Fore.WHITE + 'for Yes.] ' + Fore.WHITE)

    if restart == 'y':
        clear()
        start()

    else:
        print(Fore.RED + "Encountered an error. Try again. (Exit Code: 1)")
        exit()

start()
