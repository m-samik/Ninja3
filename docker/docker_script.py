try :
    import os   
    import pyfiglet 
    import subprocess as sp
except Exception as e:
    print("Some modules are missing {}".format(e))

def launch_con():
    try:
        print("Enter the following specs: ")
        name = input("Contanier Name: ")

        port_for = input("Do you want to enable port forwarding (y/n)")
        if (port_for == 'y'):
            int_port = input("Enter Internal Port: ")
            ext_port = input("Enter External Port: ")
        
        attach_vol = input("Do you want to attach volume (y/n)")
        if (attach_vol == 'y'):
            base_vol = input("Enter mount point of BaseOS: ")
            con_vol = input("Enter mount point of Container: ")

        image = input("Container Image: ")
        ver = input("Enter Version: ")

        if (port_for == 'y' and attach_vol == 'y'):
            cmd = "docker run -dit --name {} -v {}:{} -p {}:{} {}:{} ".format(name,base_vol,con_vol,ext_port,int_port,image,ver)
        elif (port_for == 'y' and attach_vol == 'n'):
            cmd = "docker run -dit --name {} -p {}:{} {}:{} ".format(name,ext_port,int_port,image,ver)
        elif (port_for == 'n' and attach_vol == 'y'):
            cmd = "docker run -dit --name {} -v {}:{} {}:{} ".format(name,base_vol,con_vol,image,ver)
        else:
            cmd = "docker run -dit --name {}  {}:{} ".format(name,image,ver)
        
        print(sp.getoutput(cmd))
        return 
    
    except Exception as e:
        print("Some exception occured: {}".format(e))
        return False


def docker_menu():
    try:
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
        print ("Delete a Container")
        print("\t[ 8 ]", end="   ")
        print ("Delete all Containers")
        print("\t[ 9 ]", end="   ")
        print ("Go back to main menu")
        os.system("tput setaf 1")
        print("\t[ 0 ]", end="   ")
        print ("To Exit")
        
        print("\n")
        os.system("tput setaf 7")

    except Exception as e:
        print("Some exception occured: {}".format(e))
        input("Close Program >>>")
        os.system("reset")
        exit()
    
    while True:
        try:
            val = int(input(" Select your Option >> "))

            if val == 0:
                exit()
            elif val == 1:
                print(sp.getoutput("docker --version"))
            elif val == 2:
                launch_con()
            elif val == 3:
                print(sp.getoutput("docker ps"))
            elif val == 4:
                print(sp.getoutput("docker ps -a"))
            elif val == 5:
                # not done yet
                print("under process")
            elif val == 6:
                # not done yet
                print("under process")
            elif val == 7:
                # not done yet
                print("under process")
            elif val == 8:
                cmd = "docker rm -f $(docker ps -aq)"
                print(sp.getoutput(cmd))
            elif val == 9:
                return
            else:
                print("Wrong Option")
            
            input("\nContinue...")
            
        except Exception as e:
            print("Some exception occured: {}".format(e))
            

        
    
