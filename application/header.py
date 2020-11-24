import os
import subprocess
# header 
def header():
    msg = "Ninja3"
    os.system("tput setaf 3")
    print(subprocess.getoutput(["figlet {}".format(msg)]), end=" ")
    print("V1.0.0")
    print("\n")

    os.system("tput setaf 6")
    print("==========================================================")
    os.system("tput setaf 3")
    print("| \t\tNinja3 Automation Tool\t\t\t |")
    os.system("tput setaf 6")
    print("==========================================================")
    print("\n")
    os.system("tput setaf 7")

    # Menu
    os.system("tput setaf 2")
    print("\t[ 1 ]", end="   ")
    print ("Docker")
    print("\t[ 2 ]", end="   ")
    print ("AWS")
    print("\t[ 3 ]", end="   ")
    print ("Linux")
    print("\t[ 4 ]", end="   ")
    print ("Big Data Hadoop")
    print("\t[ 5 ]", end="   ")
    print ("Ansible")
    os.system("tput setaf 1")
    print("\t[ 0 ]", end="   ")
    print ("To Exit")

    print("\n")
    os.system("tput setaf 7")

    option = int(input(" Select your Option >> "))
    return option

