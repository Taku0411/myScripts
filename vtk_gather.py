import sys
import os
import glob
import re
import shutil
from collections import Counter
# TODO if computation is exit without success full number of newest file is smaller than timestep
"""
!DESCRIPTION!
    this program makes vtk sets to visualize the change of design value for topology optimization
    In dynamic topology opitmization, generated vtk file gets too much. This program makes 3 vtk sets as
    1. first iteration dynamic analysis
    2. last iteration dynamic analysis
    3. change of design value(vtk is used at last time step data).

!HOW TO USE!
1. change directory where vtk file exists (all vtk files should be in the same directory)
2. run $ python vtk_gather.py

!NOTICE!
    file name is assumed to be
    res***step***.vtk.
    res*** is the optimization iteration
    step*** is the time step in dynamic analysis

    OTHER file name rule, this program might not work properly

!AUTHOR!
Takumi SUGIURA
"""


# get all vtk files
WholeList = glob.glob("./*.vtk")
print("number of file is: " + str(len(WholeList)))

# check file name format from 1 st list

# count strings
target = WholeList[0]

# check strings
StrCheck = re.split(r"\d+", target)
print(StrCheck)
# check number of digit
DigitCheck = re.findall(r"\d+", target)
if(len(DigitCheck) != 2):
    print("File name format is invalid")
    sys.exit(-1)

# make digit list
DigitList = []
for i in range(len(WholeList)):
    DigitList.append(re.findall(r"\d+", WholeList[i]))


NumIter = max(int(i[0]) for i in DigitList)
NumStep = max(int(i[1]) for i in DigitList)
print("number of optimization iteration: {}\nnumber of analysis step: {}".format(NumIter, NumStep))

# input
print("please enter the number for the optimization flow files")
id = input()
id = int(id)
if id > NumStep:
    print("input value: index out of range")
    sys.exit(1)

# make list of export
first_list = glob.glob("{}{}{}*{}".format(StrCheck[0], 1, StrCheck[1], StrCheck[2]))
last_list = glob.glob("{}{}{}*{}".format(StrCheck[0],NumIter, StrCheck[1], StrCheck[2]))
flow_list = glob.glob("{}*{}{}{}".format(StrCheck[0], StrCheck[1], id, StrCheck[2]))

# make directory
if(os.path.isdir("../output") != True):
    os.mkdir("../output")


for i in first_list:
    digit = re.findall("\d+", i)
    output = "../output/first{}.vtk".format(digit[1])
    shutil.copyfile(i, output)



for i in last_list:
    digit = re.findall("\d+", i)
    output = "../output/last{}.vtk".format(digit[1])
    shutil.copyfile(i, output)



for i in flow_list:
    digit = re.findall("\d+", i)
    output = "../output/flow{}.vtk".format(digit[0])
    shutil.copyfile(i, output)
