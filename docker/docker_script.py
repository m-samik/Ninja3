import os
# status docker
def status_docker():
    cmd = os.system("systemctl status docker")
    print(cmd)
