
 as_polyFracture.py v0.5g


 Python script for Maya


	by Alin Sfetcu
		aSfetcu @ gmail.com


	Creation date:	08-may-2009
	Last update:	19-feb-2014


  Installation:
  ---------------
	- copy script file (.py) from the .zip file in your ..\maya\scripts
	- add a new (python) button to your shelf with code :

				import as_polyFracture as pf
				reload(pf)
				pf.pub_polyVoronoi()


  Run:
  ---------------
	- press that shelf button


  Description:
  ---------------
	- this script lets you :
		- break an object using a 3D voronoi algorithm
		- have a look here ( http://vimeo.com/3399172 )


  Usage:
  ---------------
	- break stuff :)


  Limitations:
  ---------------
  - doesn`t like concave geometry (cups, glasses etc)


  To do:
  ---------------
	- find time to add more features
	- fix the bug with concave objects
	- assign other shader to interior faces


  History:
  ---------------
	-v0.5g: [  19-feb-2014 ]
		- step 3 works in: Maya 2012 x64, Maya 2013 x64 and Maya 2014 x64

	-v0.5e: [  16-apr-2013 ]
		- (again) i have deactivated step 3. You need to clean the locators found outside your mesh by hand.

	-v0.5d: [  28-jul-2012 ]
		- i have fixed step 3 (tested on Maya 2013 x64 SP1)... yeah right!

	-v0.5c: [  05-dec-2011 ]
		- i have deactivated step 3. You need to clean the locators found outside your mesh by hand.

	-v0.5: [  21-oct-2010 ]
		- i hope this time that pestering bug inside the clean step is fixed.

	-v0.4: [  29-may-2010 ]
		- fixed a bug with Maya 2011 when trying to "clean" the locators.
		
	-v0.3: [  11-apr-2010 ]
		- fixed a bug where trying to break a resulting piece even more was generating an error.

	-v0.2: [  14-mar-2010 ]
		- fixed a bug where the embedded Python found in Maya 2009 has no idea what math.isnan is :)

	-v0.1: [  10-mar-2010 ]
		- first release


  ..and of course,
  ----------------

  YOU ARE USING THIS PROGRAM AT YOUR OWN RISK! I SHALL NOT BE LIABLE FOR ANY KIND OF DAMAGE TO
  YOUR SYSTEM RESULTED FROM THE USE OF THIS PROGRAM. ALTHOUGH TESTED AND DISTRIBUTED WITH
  NO HARM INTENDED, I MAY NOT GUARANTEE ANY SAFETY UPON USING THIS PIECE OF SOFTWARE.

  You may use this script free of charge.

  DO NOT MODIFY THIS SCRIPT UNLESS YOU HAVE MY PERMISSION.

  If you need help, advices, questions regarding this script or if you find a bug please contact
  me at aSfetcu @ gmail.com. If you report a bug please include a precise description of the bug.

  Thank you!

