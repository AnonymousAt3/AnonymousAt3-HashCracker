#!/usr/bin/python

import hashlib
import os 

os.system("clear")
flag = 0

print("\033[1;32;40m   ___                                                       ___  _   _____  ")
print("\033[1;32;40m  / _ \                                                     / _ \| | |____ | ")
print("\033[1;32;40m / /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___  / /_\ \ |_    / / ")
print("\033[1;32;40m |  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __| |  _  | __|   \ \ ")
print("\033[1;32;40m | | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \ | | | | |_.___/ / ")
print("\033[1;32;40m \_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/ \_| |_/\__\____/  ")
print("\033[1;32;40m                           __/ |                                             ")
print("\033[1;32;40m                          |___/                                              \n")
print("                            This Script Was Made By Anonymous At3 (Cyber Ghosts)                         ")
print("                            youtube Anonymous At3 - https://www.youtube.com/channel/UChNoHwc5jT9YU5RtKzX_c7A  ") 
                                                                                                                                   
pass_hash = input("\033[1;36;40m Enter the md5 hash: ")
wordlist = input("\033[1;36;40m  Wordlist Location: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("\tpassword found")
        print("Password is " + word)
        flag = 1
        break

if flag ==0:
    print("\tPassword is not in the list")

#Written by Anonymous Ar3 (Cyber Ghosts)
