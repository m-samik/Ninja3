#!/usr/bin/python3

# importing files
from application.header import *
from docker.docker_script import *
from aws.aws_script import *
from ansible.ansible_script import *
from hadoop.hadoop_script import *
from linux.linux_script import *

import subprocess
import os

# header
option = header()
print(option)

# status of docker
#status_docker()
