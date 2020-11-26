#!/usr/bin/python3

# importing files
try :
    from application.header import header
    from docker.docker_script import docker_menu
    #from aws.aws_script import 
    #from ansible.ansible_script import 
    #from hadoop.hadoop_script import 
    #from linux.linux_script import 
except Exception as e:
    print("Some modules are missing {}".format(e))


# Header
def main_menu():
    while (True):
        header()
        option = int(input(" Select your Option >> "))
        if option == 0:
            exit()
        try:
            if option == 1:
                docker_menu()
            else:
                print(option)
        except Exception as e:
            print("Some exception occured: {}".format(e))

main_menu()

# status of docker
#status_docker()
