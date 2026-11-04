/////////////////////////////////////////////////////////////////////////////			
/*				
	Copyright © 2006 DVY_Springs. All rights reserved davvey@ntlworld.com

						- DVY_Springs -
///////////////////////////////////////////////////////////////////////////////
Note:- Any Duplicate files contained in any of my script packs can be used.
Just ensure you copy the latest version of any file.
These script packs are being built up using some common utility type scripts
which are shared across more than one pack.						

	DVY_Springs;
	Description and Usage Section
	
	NOTE:- Maya's POLY HELIX Tool is required to run this script.

	Installation	

	Just install scripts in any Maya script path and install
	Icon and Image files in May\\Prefs\Icons directory
						
	Usage

	Type DVY_Springs in command line or middle mouse drag it to a shelf.
	There is an IcOn file supplied to use with the Shelf Button.
	
	Installation
	
	Install all scripts in any Maya Script folder and install all image files
	in Maya's Icon folder.
	
	Description	
	
	This script is call a GUI where releavnt Info can be enetered to generate 
	a dimensionally accurate Spring.

	Enter Spring dimensions and GUI will also show English equivalent sizes.
	Select top and Bottom Spring ends as required then press Build Spring Button.
	The Script can build the following styles of Springs.
	
	Closed_Ground_End, Closed_Flat_End, Open_End,  
	Hook_Loop_End, Closed_Loop_End, xtended_Loop_End, Cone_End
	
	As each option is selected an image of the style will be updated in the GUI.
	The top and Bottom ends can be the same or different styles.
	
	Genrally Compression springs are built using the first three styles and
	extension using the remaining four styles.
	
	There is a Radio Button to select style but this will only change the name
	of the Spring and the User can set the styles as required.
	
	The Top and Bottom sections are point and aim constrained to Top and Bottom
	Locators which can be used to "operate the Spring".
	
	The spring will stretch as the Top and Bottom Locators are move in the Y-axis
	The Move the spring use the Top Gotp Node to Transalte and Roate the Spring.
	
	The Spring is generated from a PolyHelix which is a locked Node to prevent 
	deletion of its construction History. The Helix has is its Height attribute
	connected to the output of a distance node which is in turn connected to the
	world space postions of the Top and Bottom Locators. The Spring Body is
	constrained to the Bottom End Section of the Spring and this ensures realistic
	stretching of the spring when either end of the spring is pulled.
	
	Unused attributes are locked off if not required.
	
	If required the script can build a Spring to match a Round Cap End Piston 
	previously built using Davvey's Piston Generator. 
	To use this option load the Pistons Top Group Node into the GUI before pressing 
	the Build Spring Button.
	
	Note:- The Scale of the Spring will be adjusted to set correct Spring size
	relevant to the correct size for the Users Maya Unit settings 
	i.e mm, cm, m, in, ft, yd.
	
	TO DELETE A SPRING
	
	PLEASE USE THE DELETE SPRING BUTTON IN THE GUI. THE REASON FOR THIS IS THAT
	THERE ARE LOCKED NODES IN THE SPRING GROUP WHICH MEANS THE NODE CANNOT BE 


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