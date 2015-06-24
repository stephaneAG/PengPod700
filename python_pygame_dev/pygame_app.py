#!/usr/bin/env python
#
# this is my first pygame program
# for the moment, it will consist of a bunch of tests of what can be possibly done
# then, I amm willing to try to deploy it after the boot seauence, without running X (..)

#### PROGRAM CODE START ####

## necessary modules imports ##
import pygame, sys # import the sys and pygame modules
from pygame.locals import * # import all the constants already defined by pygame

pygame.init() # init all the pygame modules at once


## window captions and icons setup ( icons must be set BEFORE setting the mode (..)  ) ##
# note : it seems that on Linaro Alip on the pengPod700
#  the same image is used as as top-left icon & task/menu bar icon  and is auto resized(..) 

# passing an icon to use in the task/menu bar
pygame.display.set_caption('Appname', "appicon48.png")
# specify the image to use
appicon = pygame.image.load('appicon48.png')
# set the top-left corner icon of the window (if one is used)
pygame.display.set_icon( appicon ) 



## View display modes examples##
# fullscreen enable window, launching in fullscreen
#mainView = pygame.display.set_mode( (800, 480), FULLSCREEN ) # set a window and its w/h tuple
# hardware accelerated window (fullscreen only) using a doubled buffer
#mainView = pygame.display.set_mode( (800, 480), DOUBLEBUF|HWSURFACE|FULLSCREEN )
# opengl renderable display handling fullscreen and using a doubled buffer
#mainView = pygame.display.set_mode( (800, 480), DOUBLEBUF|OPENGL|FULLSCREEN )
# fullscreen enable and resizable winfow, launching in fullscreen
#mainView = pygame.display.set_mode( (800, 480), RESIZABLE|FULLSCREEN ) # handy ( 'F' toggle )
# fullscreen enable resizable window, launching windowed
#mainView = pygame.display.set_mode( (800, 480), RESIZABLE)
# fullscreen enable window, launching in fullscreen, that can be toggled to a frameless window
#mainView = pygame.display.set_mode( (800, 480), NOFRAME|FULLSCREEN ) # no brdr/ctrls for view
# window with no borders nor controls (lookslike fullscreen but allowing app switching )
#mainView = pygame.display.set_mode( (800, 480), NOFRAME) 

# a debug one, practical above all as getting the native resolution of the screen (..)
mainView = pygame.display.set_mode( (800, 480), RESIZABLE)


## test code (.. ) ##

# draw a background without images
background = pygame.Surface( mainView.get_size() )
background = background.convert() # make it usable within pygame (..)
background.fill( (250, 250, 250) )


# to draw text in pygame
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render("Some text Dude !", 1, ( 255,255,0 ))
mainView.blit( label, (100, 100) )  # append it to the screen

## handle the maintained keys ##
pygame.key.set_repeat( 400, 300 )

# main loop
loopAgain = 1
while loopAgain:
	for event in pygame.event.get(): # handle the events
		if event.type == QUIT: # handle the 'QUIT' event
			loopAgain = 0 # exit the loop
			pygame.quit() # desactivate the pygame library
			sys.exit() # terminate the program		
		
		# handle arbitrary key constants
		if event.type == KEYDOWN: # if a key is down
			if event.key == K_SPACE: # if the spacebar is hit
				print 'Space bar hit !'
			if event.key == K_RETURN: #if Enter is hit
				print 'Entering the void againnnnnn !!! ..'
			# code to exit while in fullscreen using the escape key
			if event.key == K_ESCAPE: # quit the app
				print 'User hit Escape key: quitting app ..'
				pygame.quit()
				sys.exit(1) # 'forced' exit ?
			if event.key == K_f: # toggle fullscreen mode
				print 'toggling fullscreen ..'
				pygame.display.toggle_fullscreen()			
	
	# code doing stg else than listening for events (..)
	mainView.blit( background, (0, 0) ) # draw the background to the mainView
	mainView.blit( label, ( 100, 100) )
	pygame.display.update() # update pygame.displax to append the changes that were made
	
	
#### PROGRAM CODE END ####
