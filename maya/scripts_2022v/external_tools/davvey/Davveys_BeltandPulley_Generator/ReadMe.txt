
///////////////////////////////////////////////////////////////////////////////
				
	Copyright © 2006 DVY_Pulleys. All rights reserved davvey@ntlworld.com

						- DVY_Pulleys -
///////////////////////////////////////////////////////////////////////////////

Note:- Any Duplicate files contained in any of my script packs can be used.
Just ensure you copy the latest version of any file.
These script packs are being built up using some common utility type scripts
which are shared across more than one pack.						

	DVY_Pulleys;
	Description and Usage Section

	Installation	

	Just install scripts in any Maya script path and install
	Icon in May\\Prefs\Icons directory (to use with any Shelf button)


	Description Section

	These Scripts will build Dimensional accurate Metric Pulleys and Belts
	and the GUI will show the English Equivalent during the setting 
	up of the various options. 
		

// Usage Section

	These scripts build Metric Pulleys and Belts but the UI will show
	 the english equivalent sizes during setup.
	 
	 When building the Flat-Belt and Vee-Belt Type Pulleys and Belts enter belt 
	 sizes then Pulley Outside Diameter. The recommended shaft and Flange sizes
	 will be calculated but can be adjusted if required.
	 Note Flanges will only be built if this option is chosen.
	 
	 Select style of each Pulley and Flange option if required.
	 
	 Build Pulleys. Then set Pulley 2 to 5 positions as required.
	 Build Belt Path and adjust as required.
	 Then Build and Rig Belts as required.
	 Note The building of the Belt or Belts can take some time as there  are a lot
	 of calculations and items to build.


	DVY_BeltDriver;
	
	It is called to rig Pulleys and Belts to set up drive for group.
	It uses Utility Nodes and KeyFraming to generate a Rotation Driver
	and sets each Pulley rotation to correct ratio. Also sets up
	Belt loop at correct speed to match Pulley_1 RPM.
	
	When building Toothed Belt each Pulleysd Tooth engagement can be
	adjusted to correct any misalignment between Belt and individual Pulleys
	Also Pulley_1 rotation speed can be set and/or reversed using attribute
	called RotateSpeed on Top Group Node. 

	Note:- The Scale of the Belts and Pulleys will be adjusted to set correct
	Pulley size relevant to the correct size for the Users Maya Unit settings
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

