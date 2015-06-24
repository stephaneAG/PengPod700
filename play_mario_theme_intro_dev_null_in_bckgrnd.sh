#!/bin/sh
#
# simple script to play a wav file
aplay /home/linaro/Desktop/StephaneAG_dev/mario_boot_stuff/mario8bit_boot.wav >/dev/null 2>&1 &

# get back to the command prompt
echo $'\cc' # aka Ctrl+C or ^C
