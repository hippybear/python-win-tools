#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a simple pythonic replacement for the windows 
   'dir' command. Once added to the path and made an executable 
   this can be used in any directory 'lsd' and look!"""

import os 
import win32api
import time

from colorama import init
from termcolor import colored

init()

clock = time.localtime()
dir_path = os.path.dirname(os.path.realpath(__file__))
t = win32api.GetVolumeInformation("C:\\")
localTime = str(clock.tm_hour) + ":" + str(clock.tm_min)

print(" LocalTime:              {0}".format( colored(localTime, 'white') ) )
print("\n")
print(" Volume in drive C is    {0}"    .format( colored(t[0]    , 'white') ))
print(" Volume serial number is {0}"    .format( colored(t[1]    , 'white') ))
print("\n")
print(" Directory of            {0}"    .format( colored(dir_path, 'white')))
print("\n")
print(" File(s)")
for file in os.listdir(dir_path):
    print("                         {0}" .format(colored(file, 'white')))