#Created by : Sidney Kang
#Created on : 15 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit0-04
# This program is the hello, world program, but with a 3 buttons that display hello, world in 3 different languages

import ui

def english_touch_up_inside(sender):
	  view['hello_world_label'].text = ("Hello, World!")
	  # This displays hello, world! in english  
def french_touch_up_inside(sender):
	  view['hello_world_label'].text = ("Bonjour, le monde!")
	  # This displays hello, world! in french
def galician_touch_up_inside(sender):
	  view['hello_world_label'].text = ("Ola, Mundo!")
	  # This displays hello, world! in galician

view = ui.load_view()
view.present('sheet')
