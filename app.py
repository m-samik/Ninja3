#!/usr/bin/python3

# importing files
try :
    from application.header import header
    from docker.docker_script import docker_menu
    #from aws.aws_script import 
    from d_ansible.ansible_script import ansible_menu
    #from hadoop.hadoop_script import 
    from linux.linux_script import linux_menu
    import os
except Exception as e:
    print("Some modules are missing {}".format(e))


# Header
def main_menu():
    while (True):
        try:
            header()
            option = int(input(" Select your Option >> "))
            if option == 0:
                exit()
            elif option == 1:
                docker_menu()
            elif option == 3:
                linux_menu()
            elif option == 5:
                ansible_menu()
            elif (option > 1 and option <= 5):
                print("option under progress...")
            else:
                print("option invalid")
        except Exception as e:
            print("Some exception occured: {}".format(e))
        input("Continue...")

# call main menu    
main_menu()

    




# status of docker
#status_docker()
