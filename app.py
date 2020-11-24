#!/usr/bin/python3

# importing files
from docker.docker_script import *
from aws.aws_script import *
from ansible.ansible_script import *
from hadoop.hadoop_script import *
from linux.linux_script import *

import os

msg = "Ninja3"
print(os.system("figlet {}".format(msg)))


# status of docker
status_docker()
