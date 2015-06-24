import os
import pygame
import time
import random

class tefscope:
	screen = None;
	
	de __init__ ( self ):
		"Initializing a new pygame screen using the frame buffer"
		# based on the code from Wolverine & Adafruit
		disp_no = os.getenv( "DISPLAY" )
		if disp_no:
			print "I'm running under X display = {0}".format( disp_no )
		
		# check wich frame buffer drivers are available
		drivers = [ 'fbcon', 'directfb', 'svgalib' ]
		found = False

		for driver in drivers:
			# Make sure that SDL_VIDEODRIVER is set
			if not os.getenv( 'SDL_VIDEODRIVER', driver ):
				os.putenv( 'SDL_VIDEODRIVER', driver )
			try:
				pygame.display.init()
			except pygame.error:
				print 'Driver:{0}'.format( driver )
				continue
			found = True
			break

		if not found:
			raise Exception( 'No suitable video driver found!' )

		size = ( pygame.display.Info().current_w, pygame.display.Info().current_h )
		print "FrameBuffer size: %d x %d" % ( size[0], size[1] )
		self.screen = pygame.display.set_mode( size, pygame.FULLSCREEN )
		
		# clear the screen to start
		self.screen.fill( 0, 0, 0)

		# initialise font support
		pygame.font.init()

		# render the screen
		pygame.display.update()

	def __del__ ( self ):
		"Destructor to make sure pygame shuts down, etc."

	def test ( self ):
		# fill the screen with red
		red = ( 255, 0 ,0 )
		self.screen.fill( red )
		
		# update the display
		pygame.display.update()


# actual code

# create an instance of the python class
scope = tefscope() # instanciate a new tefscope obj & configure the frame buffer or throw an error (..)

scope.test() # call a test fcn

time.sleep( 10 ) # sleep for ten seconds with a red screen before exiting (..)


