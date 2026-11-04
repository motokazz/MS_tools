/////////////////////////////////////////////////////////////////////////////			
/*				
	Copyright © 2006 DVY_InExDoors. All rights reserved davvey@ntlworld.com

						- DVY_InExDoors -
						
/////////////////////////////////////////////////////////////////////////////

Note:- Any Duplicate files contained in any of my script packs can be used.
Just ensure you copy the latest version of any file.
These script packs are being built up using some common utility type scripts
which are shared across more than one pack.						
						
	DVY_InExDoors;
	Description and Usage Section
	
	Installation	

	Just install scripts in any Maya script path and install
	Icon and Image files in May\\Prefs\Icons directory
						
	Description	
	
	Usage

	Type DVY_InExDoors in command line or middle mouse drag it to a shelf.
	There is an Icon file supplied to use with the Shelf Button.
	
	Description	

	This script calls a GUI where relevant Info can be entered to generate 
	a dimensionally accurate Door.

	The Doors are built with nominal frame sizes as follows.

	External Frame Width = 60 mm
	External Frame Height = 60 mm
	External Frame Depth = 75 mm
	Internal Frame Width = 30 mm
	Internal Frame Height = 30 mm
	Internal Frame Depth = 100 mm.
	External Frame Cill Depths of 0, 100, 150, 200 mm are
	available (default is 150 mm).

	After Selecting Door size using Option Menu or Custom sizes select
	number of Doors 1 or 2. Then select type of Interior or Exterior Door
	design from the various option menus. As the design is selected the GUI
	will update the display to show a diagram of the style. I have tried to
	label each style as descriptively as possible 

	The script will currently build `Plain` 2, 3, 4, 5, and 6 Panel Style
	Doors with Inward or Outward opening Hinges, which are left or right 
	side Hinge locations. Double Doors can also be built. Also there is a
	choice fo Glass Panel combinations. The exterior Door frame can have
	Panels either or both sides of any width. The Script will add simple
	White Shader for the Door and Frames and and a Glass Shader for the
	Glass Panes.

	The GUI has data field for Overall Door Width and Height and a Radio
	Button Group to set Cill Depth for external doors.

	After building the Door the script will lock off unused attributes and
	leave the Door Group Hinge postiomn unlocked and keyable.

	Note:- The Scale of the Door will be adjusted to set correct size
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