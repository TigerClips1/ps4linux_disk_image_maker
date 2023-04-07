#!/bin/python

import os #this is the os mudule from cpython

#Main script class
class SetupLinux:
        #variables
        username = input("Enter your Linux username: ") #get input from user
        #Main commands for linux Windows coming soon
        alert = f"Make sure your diskimage file is in the /home/{username}/psxitarch.tar.xz or tar.gz and /home/{username}/linux.img \n"
        #text that display when it's called
        install =  "Installing\n"
        #set everything up 
        requirement_Arch = "sudo pacman -Syyu && sudo pacman -S wget"
        #errors
        error =  "we can't find your linux.img make sure to move it from your ps4 oru usb in to  your home directory"
        error2 = " you don't have a tar.gz file or cant be found"
        error3 = "you don't have an arch base distro Please run the .sh version for other os " 
        #setup the diskimage file
        enable = (f"sudo losetup /dev/loop5 /home/{username}/linux.img")
        EX2 =  "sudo mkfs.ext2 /dev/loop5"
        mount =  "sudo mount /dev/loop5 /PS4"
        make = "sudo mkdir /PS4"
        #change working directory
        change2 = "/PS4"
        change = f"/home/{username}/"
        remove = "sudo rm -rf /PS4"
        #extract everything
        tar_xz = f"sudo tar -xvf /home/{username}/psxitarch.tar.xz"
        tar_gz = f'sudo tar -xvzf /home/{username}/psxitarch.tar.gz'
        #let the USer know that it done
        done = "sudo  umount /dev/loop5"
        #install winrar windows gui for linux if you have wine install
        rar_link = "wget https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe"
        rename = "sudo mv winrar-x64-621.exe winrar.exe"
        open = "wine winrar.exe"
#credit the author
ends = "Done"
author = "scripts by TigerClips 2 \n"
promo =  "ps4linux.com \n"
#function
def failsafe():
    if os.geteuid() != 0:
        print("Please run this script as root if you don't want to keep on entering your password")
        exit()
    else:
        print("setting up")

def main_os():
    #run all the commands that in the variables aka class
    if main_os: 
        #print the class text on screen
        print(SetupLinux.alert)
        print(SetupLinux.install)
        os.system(SetupLinux.remove)
        #run all the Commands 
        os.system(SetupLinux.requirement_Arch)
        os.system(SetupLinux.enable)
        os.system(SetupLinux.EX2)
        os.system(SetupLinux.make)
        os.system(SetupLinux.mount)
        os.chdir(SetupLinux.change2)
        os.system(SetupLinux.tar_xz)
        os.system(SetupLinux.done)
        os.chdir(SetupLinux.change)
        os.system(SetupLinux.rar_link)
        os.system(SetupLinux.rename)
        os.system(SetupLinux.open)
    else:
        #print error on the screen if it cant find the diskimage file or tar.xz, tar.gz
        print(SetupLinux.error)
#function
def end():
    #print the credits
    print(ends)
    print(author)
    print(promo)
#call all the functions
failsafe()
main_os()
end()