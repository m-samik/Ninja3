# Ninja3
Open Source Python Software that will be used to integrate Docker, AWS Cloud, Linux, Ansible, BigData Hadoop, etcvim 

## To run this Python Program as a command in Linux
$ vim /etc/rc.d/rc.local

alias ninja3='python3 app.py'

![](images/ninja3.jpg)

## Create a new environment
$ python3 -m venv .venv
$ source .venv/bin/activate

## Install Figlet Package in your RedHat/Centos OS
figlet is in Fedora/EPEL, so you really don't want to get it from anywhere else.

$ yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

$ yum install figlet

![](images/ninja3_1.jpg)


## Install Python3 Requirements
$ pip install --upgrade pip
$ pip install -r requirements.txt
