#! /cygdrive/c/Users/a_user/AppData/Local/Programs/Python/Python38

##########################################################
# This code launches 2 instances of Reflection Workspace #
##########################################################

# Future ideas:
#   Ask how many instances and open accordingly
#   Check if instance is open, and if so open the next one
#   On except ask if user would like to try again or exit

#######################
# Import Dependencies #
#######################

import subprocess
from subprocess import Popen
import psutil
import time
import os
from pathlib import Path
import psutil
import time


def checkIfProcessRunning(processName):
# Check if there is any running process that contains the given name processName.

#Iterate over the all the running process

    for proc in psutil.process_iter():
        try:
# Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return False;

def findProcessIdByName(processName):

#Get a list of all the PIDs of a all the running process whose name contains the given string processName

    listOfProcessObjects = []
#Iterate over the all the running process

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
# Check if process name contains the given name string.

            if processName.lower() in pinfo['name'].lower() :
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            pass
        return listOfProcessObjects;

def main():
    print("*** Check if a process is running or not ***")

# Check if any chrome process was running or not.

    if checkIfProcessRunning('Emulation.exe'):
        print('Yes an Attachmate process was running')
    else:
        print('No Attachmate process was running')

    print("*** Find PIDs of a running process by Name ***")

# Find PIDs od all the running instances of process that contains 'chrome' in it's name
    listOfProcessIds = findProcessIdByName('Emulation')

    if len(listOfProcessIds) > 0:
        print('Process Exists | PID and other details are')

        for elem in listOfProcessIds:
            processID = elem['pid']
            processName = elem['name']
            processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
            print((processID ,processName,processCreationTime ))
        else :
            print('No Running Process found with given text')

            print('** Find running process by name using List comprehension **')

# Find PIDs od all the running instances of process that contains 'chrome' in it's name

        procObjList = [procObj for procObj in psutil.process_iter() if 'Emulation' in procObj.name().lower() ]
        for elem in procObjList:
            print (elem)

if __name__ == '__main__':
    main()



############################################
# Open 2 instances of Reflection Workspace #
############################################


expo1 = Path(r"C:\Users\a_user\Documents\Micro Focus\Reflection\EXPO1 DMA MFR 2020.rd3x")
expo2 = Path(r"C:\Users\a_user\Documents\Micro Focus\Reflection\EXPO2 DMA MFR 2020.rd3x")

try:
    os.system('start "C:\\Program Files (x86)\\Micro Focus\\Reflection\\Attachmate.Emulation.Frame.exe" "C:\\Users\\a_user\\Documents\\Micro Focus\\Reflection\\EXPO1 DMA MFR 2020.rd3x"')

    os.system('start "C:\\Program Files (x86)\\Micro Focus\\Reflection\\Attachmate.Emulation.Frame.exe" "C:\\Users\\a_user\\Documents\\Micro Focus\\Reflection\\EXPO2 DMA MFR 2020.rd3x"')

    print ("Expo Launched. Continue to login.")

except: print("Unable to launch application.") 
