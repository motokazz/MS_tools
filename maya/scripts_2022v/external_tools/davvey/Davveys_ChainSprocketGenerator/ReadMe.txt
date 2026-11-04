
///////////////////////////////////////////////////////////////////////////////
				
	Copyright © 2006 DVY_Chains. All rights reserved davvey@ntlworld.com

						- DVY_Chains -
///////////////////////////////////////////////////////////////////////////////
						
	DVY_Chains;
	Description and Usage Section

	Installation	

	Just install scripts in any Maya script path and install
	Icon in May\\Prefs\Icons directory (to use with any Shelf button)

	Note:- Any Duplicate files contained in any of my script packs can be used.
	Just ensure you copy the latest version of any file.
	These script packs are being built up using some common utility type scripts
	which are shared acroos more than one pack.


	Description Section

	These Scripts will build Dimensional accurate Metric Chains using the
	relevant ISO Standards and the GUI will show the English Equivalent
	during the setting up of the vrious options. The Metric Chains
	manufactured to the above standards are covered by ISO 606 and DIN 8187.
	
	These standards cover 3 versions:
	** SIMPLEX
	** DUPLEX
	** TRIPLEX
	
	The range of pitch sizes can vary between 4mm, (0.158 ins) to 114.3mm, (4.5 ins).
	
	American standard chains are covered by ISO 606, ANSI B29.1 and DIN 8188
	and eight versions are covered.
	
	** SIMPLEX, DUPLEX and TRIPLEX as for the European standard chains.
	** QUADRUPLEX, 4 strands.
	** QUINTUPLEX, 5 strands.
	** SEXTUPLEX, 6 strands.
	** OCTUPLEX, 8 strands.
	** DECUPLEX, 10 strands.
	
	The pitch sizes covered by this standard are 1/4 to 3 inch pitch.
	
	For Metric Chains above TRIPLEX these are normally classed as Custom but
	these Scripts will build the relevant number of Strands using "Standrd" metric
	Sizes and Specs
	

// Usage Section

	These scripts build Metric Chains but the UI will show the english 
	equivalent sizes during setup.
	Choose the number of teeth, type and material for the Chains. It may not
	be possible to achieve target speed ratios precisely because Chains must,
	of course, have an integer number of teeth and also because Chains in
	catalogues must be chosen from a preferred list of numbers of teeth. 
	
	The preferred standard Sprocket teeth numbers are:
	
	12 13 14 15 16 18 20 22 24 25 28 30
	32 34 38 40 45 50 54 60 64 70 72 75
	80 84 90 96 100 120 140 150 180 200 220 250
	
	Many catalogues display a more comprehensive range than this but many
	sizes will not be readily available 'off-the-shelf'. The range of
	available sizes will depend upon the Sprocket module (m). Generally the
	lower the module, the greater the range of Sprocket teeth sizes available.
	
	**THIS SCRIPT PACK WILL BUILD RANGE BETWEEN 9 AND 150 TOOTHED SPROCKETS**
	
	The Metric Chains manufactured to the standards covered by 
	ISO 606 and DIN 8187 are :-
	
	"03B", "04B", "05B", "06B", "08B", "10B", "12B", "16B",
	"20B", "24B", "28B", "32B", "40B", "48B", "56B", "64B", "72B"
	
	Large speed ratios are achieved in several stages, choosing the number
	of teeth for each Sprocket so that the overall reduction is as close to
	target as is possible.
	
	Example
	
	Select ISO Standard Pitch from drop down menu  the range is 03B to 72B  
	This is 5mm to 114.3 mm (0.197 to 4.5 inches).
	Choose the type (SIMLEX, DUPLEX, TRIPLEX etc.) Then set Sprocket type of 
	Staight-Sided, Hubbed or Spoked. Set Teeth per Sprocket and then Center 
	Distance and for best reults use disatnce of betwwen 30 and 50 pitches.
	
	The script will adjust Target Center Distance to give exactly an even number
	of Chain Pitches based on Pitch and target distance. After building the Sprockets,
	Sprocket_2 postion can be adjusted in the Y axis only if required. Then Build Chain
	if slected the Idler Spocket option will be built and can be postioned. This sprocket 
	has one of the Chains' CV's point Constrained to the sprocket to move chain path to suit
	sprocket position.
	
	Once Sprockets and Chain are built select Sprocket Group Top Node and press "Rig Chains"
	Button. After Rigging Sprocket Groups can not be added to.



	DVY_ChainDriver;
	
	It is called to rig Chain and Sprockets to set up drive for group.
	It uses Utility Nodes and KeyFraming to generate a Rotation Driver
	and sets each Sprockets rotation to correct ratio. Also sets up
	Chain loop at correct speed to match Sprocket_1 RPM.
	
	Each Sprockets Tooth engagement can be adjusted to correct any
	misalignment between chain and individual sprockets. Also Sprocket_1
	rotation speed can be set and/or reversed using attribute called
	RotateSpeedon Top Group Node. Also the chain speed can be controlled
	if any rotational mismatch occurs using an attribute called SpeedAdjust
	on Top Grouyp Node.

	Note:- The Scale of the Chains will be adjusted to set correct Sprocket Size relevant
	to the correct size for the Users Maya Unit settings i.e mm, cm, m, in, ft, yd.

	Davvey
	If you like the scripts please rate them.

	I Thought I saw Light at the end of the Tunnel
	but it was just some Bxxxxxx with more troubles.

	davvey@ntlworld.com

