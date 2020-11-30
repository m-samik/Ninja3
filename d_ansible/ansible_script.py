try:
    import subprocess
    import os
    import pyfiglet
    import getpass
except Exception as e:
    print("Some modules are missing {}".format(e))
    input("Close Program >>>")
    os.system("reset")
    exit()

def ansible_menu():
 
    os.system("clear")
    os.system("tput setaf 3")
    result = pyfiglet.figlet_format("Ninja3 Ansible") 
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

    # Ansible Menu
    os.system("tput setaf 2")
    print("\t[ 1 ]", end="   ")
    print ("List Available Hosts")
    print("\t[ 2 ]", end="   ")
    print ("Add New Hosts")
    print("\t[ 3 ]", end="   ")
    print ("Run Ansible to Configure Web Server on Available Hosts")
    print("\t[ 4 ]", end="   ")
    print ("Set New Host")
        # print("\t[ 5 ]", end="   ")
        # print ("Start/Stop a Container")
        # print("\t[ 6 ]", end="   ")
        # print ("Get the Shell of Container")
        # print("\t[ 7 ]", end="   ")
        # print ("Delete a Container")
        # print("\t[ 8 ]", end="   ")
    # print ("Delete all Containers")
    print("\t[ 9 ]", end="   ")
    print ("Go back to main menu")
    os.system("tput setaf 1")
    print("\t[ 0 ]", end="   ")
    print ("To Exit")
    
    print("\n")
    os.system("tput setaf 7")

    while True:
        try:
            val = int(input(" Select your Option >> "))

            if val == 0:
                exit()
            elif val == 1:
                print(os.system("ansible all --list-hosts"))
            elif val == 2:
                print("Enter the Details Below  : ")
                ip=input("Enter the O.s Ip : ")
                username=input("Enter the Username : ")
                password=getpass.getpass("Enter Your PAssword : ")
                with open("/root/ansible/inventory.txt","a") as f:
                    f.write("{} ansible_user={} ansible_ssh_pass={} ansible_connection=ssh".format(ip,username,password))
                print(os.system("vim /root/ansible/inventory.txt"))
            elif val == 3:
                print(os.system("ansible-playbook d_ansible/ansible_playbooks/myplay.yml"))
            elif val == 4:
                print("")
            # elif val == 5:
            #     # not done yet
            #     print("under process")
            # elif val == 6:
            #     # not done yet
            #     print("under process")
            # elif val == 7:
            #     # not done yet
            #     print("under process")
            # elif val == 8:
            #     cmd = "docker rm -f $(docker ps -aq)"
            #     print(os.system(cmd))
            elif val == 9:
                return
            else:
                print("Wrong Option")
            
            input("\nPress Enter to Continue...")
            
        except Exception as e:
            print("Some exception occured: {}".format(e))