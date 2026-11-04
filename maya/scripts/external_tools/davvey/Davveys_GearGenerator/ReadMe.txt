
///////////////////////////////////////////////////////////////////////////////

				
	Copyright © 2006 DVY_Gears. All rights reserved davvey@ntlworld.com

						- DVY_Gears -

///////////////////////////////////////////////////////////////////////////////

Note:- Any Duplicate files contained in any of my script packs can be used.
Just ensure you copy the latest version of any file.
These script packs are being built up using some common utility type scripts
which are shared across more than one pack.						

//	Installation	

	Just install scripts in any Maya script path and install
	Icon in May\\Prefs\Icons directory (to use with any Shelf button)



//	Description Section

	These Scripts will nuild Dimensional accurate Metric Gears using the
	relevant ISO Standards and the GUI will show the English Equivalent
	during the setting up of the vrious options

// Usage Section

	Choose the number of teeth, type and material for the gears. It may not
	be possible to achieve target speed ratios precisely because gears must,
	of course, have an integer number of teeth and also because gears in
	catalogues must be chosen from a preferred list of numbers of teeth. 
	
	The preferred standard gear teeth numbers are:
	
	12 13 14 15 16 18 20 22 24 25 28 30
	32 34 38 40 45 50 54 60 64 70 72 75
	80 84 90 96 100 120 140 150 180 200 220 250
	
	Many catalogues display a more comprehensive range than this but many
	sizes will not be readily available 'off-the-shelf'. The range of
	available sizes will depend upon the gear module (m). Generally the
	lower the module, the greater the range of gear teeth sizes available.
	
	The preferred standard module sizes are:-
	
	0.5, 0.8, 1, 1.2 5, 1.5, 2, 2.5, 3, 4, 5, 6
	
	The full range which this script can produce includes Series 1 and 2
	which is extracted from JIS B 1701-1973 Standards.
	
		0.1, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60,
		0.70, 0.8, 0.90, 1.00, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9,
		10, 11, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 45, 50,
	
	Large speed ratios are achieved in several stages, choosing the number
	of teeth for each gear so that the overall reduction is as close to
	target as is possible.
	
	Example
	
	Choose the type (Spur, Single Helical, Double Helical etc.) and select
	Module (metric size). Then set Gear width. Select Teeth per Gear to a
	maximum of Ten (more can be added afterwards). Choose New Group (default)
	or add to existing Group.
	
	If adding to existing Group select Top Node and load into UI textField.
	
	Once Gear Groups are built select Gear Group Top Node and press "Rig Gears"
	Button. After Rigging Gear Groups can not be added to.
	
	After Rigging select the Gear Groups Top Node and to rotate Gear 2 set
	angle of rotation using the Channel Box attribute ".RotateGrp_2".
	Repeat for each other Gear if required. 
	Default speed of roation is 1 RPM for Gear_1 and to adjust set attribute 
	".RotateSpeed" to desired RPM.
	
	To connect one Gear Group to another Select the Gear to be used as a
	Driver first then select the Shaft to be driven (this must be the first 
	Gear Shaft in that Group). Press "Connect Gear" Button.
	Shafts do not have to be in line before connecting and can the Gear Group's
	Top Node can still be moved afterwards.
	
	This will connect the rotateX of the driver shaft to the rotateX of the
	driven shaft and add an attribute named ". Rotation" to the Driven Group
	Top Node. This can be set to 1, 0 or -1 forward, off and reverse.
	
	
	3.1 Example  
	
	To llustrate the choice of teeth numbers consider a 30:1 target reduction.
	Alternative solutions are:
	
	(72/12)(60/12) reduction, R = 30
	(72/13)(72/13) reduction, R = 30.67 - (2.2% error, closest to equal sharing)
	(72/13)(70/13) reduction, R = 29.82 - (0.6% error, very near to equal sharing)
	
	This achieved by running the GUI twice with Option to link shafts set for
	second run of GUI.
	
	It should be noted that although in this example the target ratio was
	attainable exactly, this will not always be so. Also it may be observed
	that whilst a common module size is required for pinion and wheel gears
	in each meshing gear pair, they need not be the same at each reduction
	stage. The changing speeds and torques at each stage may mean that a
	different module size is desirable from strength and gear size
	considerations.
		
	A Chain of Muliple gears can be set up to achieve any desired ratio if required

	Note:- The Scale of the Gears will be adjusted to set correct Gear Size relevant
	to the correct size for the Users Maya Unit settings i.e mm, cm, m, in, ft, yd.

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
