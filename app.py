#!/usr/bin/python3

# importing files
from docker import docker_script
from aws import aws_script
from ansible import ansible_script
from hadoop import hadoop_script
from linux import linux_script

import os

msg = "Ninja3"
print(os.system("figlet {}".format(msg)))

