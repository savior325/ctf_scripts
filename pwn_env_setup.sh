#!/bin/bash 
#
cd $HOME
sudo dpkg --add-architecture i386
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install binutils nasm
sudo apt-get -y install gcc-multilib g++-multilib
sudo apt-get -y install libc6-dev-i386
sudo apt-get -y install git
sudo apt-get -y install libc6-dbg libc6-dbg:i386
sudo apt-get -y install nmap
sudo apt-get -y install python-pip libssl-dev
sudo apt-get -y install gdb
sudo pip install --upgrade pip
sudo pip install --upgrade capstone
sudo pip install --upgrade pwntools
sudo pip install ropgadget

git clone https://github.com/scwuaptx/peda.git ~/peda 
cp ~/peda/.inputrc ~/
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
git clone https://github.com/JonathanSalwan/ROPgadget

git clone https://github.com/inaz2/roputils.git
sudo cp ~/roputils/roputils.py /usr/lib/python2.7/dist-packages/

git clone https://github.com/cloudburst/libheap.git
sudo pip3 install --user ./libheap/
echo "python from libheap import *" >> ~/.gdbinit
echo "set follow-fork-mode child" >> ~/.gdbinit

sudo apt-get -y install socat
sudo apt-get -y install xinetd

git clone https://github.com/lieanu/libc.git
cd libc
rm -rf libc-database
git clone https://github.com/niklasb/libc-database
sudo python setup.py develop
cd $HOME

#sudo pip install lief
#sudo pip install https://github.com/lief-project/packages/raw/lief-master-latest/pylief-0.9.0.dev.zip
