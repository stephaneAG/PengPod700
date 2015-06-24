#!/bin/bash
#
# simple utility script to hide the cursor pointer using C code and the "xsetroot" command instead of using unclutter of other third-parties way of doing so ( ex -> blank pointer image on Maemo, or moving the pointer ou of the field of view )
# currently, this method allows to use any other input device as well for Xorg , without the need to disable the Xinput events received from the mouse (..)
# Nb: still WIP
#
# by StephaneAG - 2013


### ACTUAL SCRIPT ###

current_dir=`dirname $0`
blank_cursor="$current_dir/blnk_ptr.xbm"
cursor_status=`cat .cursor-status`
if [ $cursor_status = "visible" ] ;
then
	xsetroot -cursor $blank_cursor $blank_cursor
	echo "hidden" > .cursor-status
else
	xsetroot -cursor_name left_ptr
	echo "visible" > .cursor-status
fi
echo "cursor is now " `cat .cursor-status`

### END SCRIPT ###
