try:
    import os
    import pyfiglet 
except Exception as e:
    print("Some modules are missing {}".format(e))

def docker_menu():
    os.system("clear")
    os.system("tput setaf 3")
    result = pyfiglet.figlet_format("Ninja3 Docker") 
    print(result, end="V1.0.0")
    print("\n")

    os.system("tput setaf 6")
    print("==========================================================")
    os.system("tput setaf 3")
    print("| \t\tNinja3 Automation Tool\t\t\t |")
    os.system("tput setaf 6")
    print("==========================================================")
    print("\n")
    os.system("tput setaf 7")

    # Docker Menu
    os.system("tput setaf 2")
    print("\t[ 1 ]", end="   ")
    print ("Docker Version")
    print("\t[ 2 ]", end="   ")
    print ("Launch a Container")
    print("\t[ 3 ]", end="   ")
    print ("Running Containers")
    print("\t[ 4 ]", end="   ")
    print ("All Containers (running/stopped)")
    print("\t[ 5 ]", end="   ")
    print ("Start/Stop a Container")
    print("\t[ 6 ]", end="   ")
    print ("Get the Shell of Container")
    print("\t[ 7 ]", end="   ")
    print ("Go back to main menu")
    os.system("tput setaf 1")
    print("\t[ 0 ]", end="   ")
    print ("To Exit")
    
    print("\n")
    os.system("tput setaf 7")

    val = int(input(" Select your Option >> "))
    
    try:
        if val == 0:
            exit()
        elif val == 1:
            print(os.system("docker --version"))
        elif val == 2:
            # not done yet
            print("under process")
        elif val == 3:
            print(os.system("docker ps"))
        elif val == 4:
            print(os.system("docker ps -a"))
        elif val == 5:
            # not done yet
            print("under process")
        elif val == 6:
            # not done yet
            print("under process")
        elif val == 7:
            return
        
        input("\nContinue...")
        docker_menu()
    except Exception as e:
        print("Some exception occured: {}".format(e))

        
    
