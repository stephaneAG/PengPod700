#!/bin/bash
# Script toallow launching a python script from a menu launcher

# launch the script from the current directory
cd /home/linaro/Desktop/StephaneAG_dev/python_pygame_dev/
./pygame_test.py
# using full path for when launched using a menu launcher (..)
#/home/linaro/Desktop/StephaneAG_dev/python_pygame_dev/pygame_test.py

# prevent terminal auto closing nb: as expected the $SHELL restart a term after quitting the python script when launched directly from a terminal ..
# the following seems not need when executing a python script (> currentlym not a so generic python script: pygame stuff .. )
#$SHELL
