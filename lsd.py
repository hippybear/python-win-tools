#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a simple pythonic replacement for the windows 'dir' command. 


   Once added to the Windows PATH environmental variable
   And added to the PATHEXT environmental variable this
   tool can be used in any directory 'lsd' and look! Otherwise
   run in the same directory as this script as 'python lsd.py'
   This assumes Python3 and the time is not correct yet."""

import os 
import win32api
import time
from colorama import init
from termcolor import colored

__author__ = "hippybear"
__license__ = "MIT"
__email__ = "yosi@codeblind.org"
__copyright__ = "Copyright 2017, Code Blind"
__status__ = "Development"


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
