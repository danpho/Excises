#!/usr/bin/python

import sys    # import sys module

import subprocess

import colored	# import colored module to control colors of output

#user default settings
PROGRAM_NAME="excercise1.py"
DFT_LOG="command"
DFT_FLAG=1

#variable settings
log=DFT_LOG
flag=DFT_FLAG

if flag == 1:
  #write command into log file
  com=open(log,'w')
  com.write(PROGRAM_NAME)
  com.close()
  
  #main body
  
else:
  # error message
  print "Something wrong. Quit.\n"
#end else of if flag ==1: 

#user defined functions
# print hello world
def print_func( par ):
  print "Hello : ", par
  return
