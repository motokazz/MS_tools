///////////////////////////////////////////////////////////////////////////////
/*			
				
	Copyright © 2006 DVY_Escalators. All rights reserved davvey@ntlworld.com

						- DVY_Escalators -
///////////////////////////////////////////////////////////////////////////////

Note:- Any Duplicate files contained in any of my script packs can be used.
Just ensure you copy the latest version of any file.
These script packs are being built up using some common utility type scripts
which are shared across more than one pack.						
						
	DVY_Stairs;
	Description and Usage Section
	
	Installation	

	Just install scripts in any Maya script path and install
	Icon and Image files in May\\Prefs\Icons directory
						
	Description	
	
	Usage

	Type DVY_Escalators in command line or middle mouse drag it to a shelf.
	There is an Icon file supplied to use with the Shelf Button.
	
	Description	

	This script calls a GUI where relevant Info can be entered to generate
	a dimensionally accurate set of Escalator or Flat WalkWay.
	
	The Scripts will build a set of Escalator or a moving Flat Walkway.
	
	There are various options that can be selected and Data fields to enter
	various sizes. These are Floor Height, Length and Tread Width.
	The Diagram on front help section shows relevant dimensions.
	The Floor Height is from flat section at bottom of Escalator to flat section
	at Top of Escaltor. The Length is from centreline of lower curved section
	of Escalator to same at Top Section. This Length includes two 1000 mm straight
	sections of steps so 6000 mm equates to 2 x 1000 mm straight sections and
	approximately 4000 mm of angled step section. The recommended angle for
	Escalators is approximately 30 degrees and these scripts will build Escalators
	beteen 20 and 50 degrees but appearance may have errors at the extreme angles.
	The overall width of the Escalator is Tread Width plus 200 mm. The HandRail
	height of approximately 925 mm and width 100 mm are fixed along with the
	1000 mm flat sections. 
	
	After building the Escalator there will be a Hi and LoRes version of all
	moving parts arranged in two seperate layers and the script will rig the
	Steps and Both HandRails to move as per a real escalator. The default direction
	is down but this can be changed along with the speed by adjusting an attribute
	named `SpeedAdjust` located on the Group Top Node called `Escalator_Main_GrpN_`.
	Set it negative to change direction and zero will stop the Escalator travelling.
	Increase or	decrease the default value of 5 to sett speed and the range is +/- 50.
	
	The Escalator groups are arranged to allow positioning of the completed
	Escalator by rotating and translating the Group Top Node called
	`Escalator_Main_GrpN_`. The Motion Path Curves etc are parent Constrained
	to this top node. If Required once position is set the Three Group Nodes can
	be grouped together to clean up HyperGraph but this node must not be moved
	once grouped or double transform will occur.
	
	The Script will add a simple Stainless Steel Shader to all parts except the
	HandRail Supports which can be set to Glass or Stainless.

	After building the Escalators the script will lock off unused attributes and
	leave the Main group Translate and Rotate Nodes unlocked and keyable.

	Note:- The Scale of the Escalators will be adjusted to set correct size
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