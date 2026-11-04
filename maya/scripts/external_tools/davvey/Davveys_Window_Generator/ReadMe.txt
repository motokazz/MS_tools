/////////////////////////////////////////////////////////////////////////////			
/*				
	Copyright © 2006 DVY_Windows. All rights reserved davvey@ntlworld.com

						- DVY_Windows -
///////////////////////////////////////////////////////////////////////////////

Note:- Any Duplicate files contained in any of my script packs can be used.
Just ensure you copy the latest version of any file.
These script packs are being built up using some common utility type scripts
which are shared across more than one pack.						

	DVY_Windows;
	Description and Usage Section
	
	Installation	

	Just install scripts in any Maya script path and install
	Icon and Image files in May\\Prefs\Icons directory
						
	Usage

	Type DVY_Windows in command line or middle mouse drag it to a shelf.
	There is an Icon file supplied to use with the Shelf Button.
	
	Installation
	
	Install all scripts in any Maya Script folder and install all image files
	in Maya's Icon folder.
	
	Description	
	
	This script calls a GUI where relevant Info can be entered to generate 
	a dimensionally accurate Window.

	The Windows are built with nominal frame sizes as follows.

	Frame Width = 50 mm
	Frame Height = 50 mm
	Frame Depth = 40 mm
	Opening Window Frame Width = 30 mm
	Opening Window Frame Height = 30 mm
	Opening Window Frame Depth = 40 mm.
	Cill Depths of 0, 100, 150, 200 mm are available (default is 150 mm).

	After enetering Overall Window sizes select type of Window Cill required
	then select type of Window design from the various option menus. As the 
	design is selected the GUI will update the disaply to show a diagram of
	the style. I have tried to label each style as descriptively as possible 

	The script will currently build `Standard` style Windows with outward
	opening Hinges. It will build Windows with fixed panes, Left, Right
	and Top Hung opening Windows. The Script will add simple White Shader
	for the Frames and Window Frames and a Glass Shader for the Glass Panes.

	The GUI has data field for Overall Window Width and Height and a Radio
	Button Group to set Cill Depth.

	After building the Window the script will lock off unused attributes and
	leave the Window Group Hinge postiomn unlocked and keyable.

	Note:- The Scale of the Window will be adjusted to set correct size
	relevant to the correct size for the Users Maya Unit settings 
	i.e mm, cm, m, in, ft, yd.
	

Installation example (for Maya 8.0):

1. Install scripts in the Maya Script directory
	E:\Documents and Settings\Davvey\My Documents\Maya\8.0\scripts

2. Install all icons (xpm files) in
	E:\Documents and Settings\Davvey\My Documents\Maya\8.0\prefs\icons
	
	Davvey
If you like the scripts please rate them.

I Thought I saw Light at the end of the Tunnel
but it was just some Bxxxxxx with more troubles.

davvey@ntlworld.com