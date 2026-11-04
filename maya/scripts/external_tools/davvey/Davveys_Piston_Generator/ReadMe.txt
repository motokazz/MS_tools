
////////////////////////////////////////////////////////////////////////////////////////
				
	Copyright © 2007 DVY_Pistons. All rights reserved davvey@ntlworld.com

						- DVY_Pistons -
////////////////////////////////////////////////////////////////////////////////////////

Note:- Any Duplicate files contained in any of my script packs can be used.
Just ensure you copy the latest version of any file.
These script packs are being built up using some common utility type scripts
which are shared across more than one pack.						

	DVY_Pistons;
	Description and Usage Section

	Installation	

	Just install scripts in any Maya script path and install
	Icon in May\\Prefs\Icons directory (to use with any Shelf button)


	Description Section

	These Scripts will build Dimensional accurate Metric Pistons and the GUI will
	show the English Equivalent during the setting up of the various options. 

	Usage Section

	To run script type DVY_Pistons in command line or middle mouse drag the 
	command to a shelf. There is a Shelf Icon included in the script pack.
	
	These scripts build Metric Pistons but the UI will show the english equivalent
	sizes during setup.
	 
	To use this these scripts. Set Rod Diameter required. Then Select Rod Length 
	required. The GUI will calculate and display nearest English equivalents for
	Diameter and Length. The Fields are already filled in with some default values to
	test the script. The default values are set using following relationships between
	dimensions as follows.
	 
	 	Cylinder ID = 2 * Rod Diameter. 
	 	Cylinder OD is 1.2 * Cylinder ID 
		Cylinder Length = Rod Length - Bore ID.
	 	
	For Best results try and use values with these ratios but script will work with
	other values. (but results maybe unpredictable) If Round Cylinder End Caps
	are used then the CheckBox for a Rod Cover can be selected. Also Spring Supports 
	can be added to allow a spring to fit over the Cylinder. The Rod Cover and Spring 
	Supports should only be selected to use with Clevis Types, Pin and Bush Mounts for
	Cylinder Ends. 
	
	The Group Top Node has some hidden attributes added to it (if the spring Options are 
	selected) 	which list some recommended dimensions for Spring Coil Diameter and the
	Radius of Section of Coil Spring, also Spring Length to match distance between
	Supports.
	Note :-  I am also currently developing a script to generate Springs which will use
	these dimensions to build a Spring to suit.";

	Note:- The Scale of the Piston will be adjusted to set correct Pulley size relevant
	to the correct size for the Users Maya Unit settings i.e mm, cm, m, in, ft, yd.

	After building Piston the script locks off unused Attributes and sets up Point and 
	Aim Constraints to rig Piston Movement. Each End of Piston has a locator which
	moves the Piston. Parent constrain these if required to set up Piston movement
	as needed. (The Piston Locators are based at control point of the Cylinder End
	e.g. Center Trunnion version has Locator at the Center Trunnion Point).

	Matching Spring.
	
	If Required After Building the Piston please use Davvey's Spring Generator
	a Spring to match the Piston and before moving Piston away from default
	build position.


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

