# pyColorList
An RGB tool I created for personal reference
pyColorList

see the lower case readme file for use - editing seems to throw my layout off balance

NOTE: I am still working on this - I may upload a rough or unfinished version, but 
it is not really ready yet. It does run as an importable module, but needs work

Author: Ben Woodfield
Date: 21/11/2016
ver: 0.0000001
-----------------------------------------------------------------------------------

CONTENTS:
    Information
    
    Goals
    
    Usage

-----------------------------------------------------------------------------------
INFORMATION
A very simple shell / command line based tool that was aimed to just be used
for personal reference.

When I use modules like Pygame I always have to check up on RGB values. I wanted to 
have an easy to use program that can be used to get a list of colours with a simple
command -

Then when you see a colour you want to use, you can use a second command to get the
RGB values returned to you. If you know the colour name you can skip the colour list
option

''' In the UK 'color' is spelled as 'colour'. This has tripped me up a few times 
before now so I just used the traditional Python spelling (color) throughout the 
program'''

Go easy on me, this is my first contribution to Python and is also the very first
version of the program/module so I know there is major room for improvement - room that 
will be filled as I figure things out

-----------------------------------------------------------------------------------
GOALS:
    Clean up the look and feel
    Create a simpler user interface
    Make it integrate with Pygame (just import, then use color names directly instead of RGB)
    Have this running as a proper Python module (not needing to have it stored in the same dir)

-----------------------------------------------------------------------------------
USAGE:

1.Have the script in a directory you are working in, and run a shell to use it
2.Use the command terminal to execute it 
3.Execute it as a stand-alone program

1. SHELL:
    >>> from pyColorList import colorList
    
    >>> print colorList
    
    >>> from pyColorlist import <color from list> 
    
    >>> print <color from list>

2. TERMINAL:
    Open the script directory in a terminal,
    
    Run the Python Interpreter ( >>> python)
    
    >>> from pyColorList import colorList
    
    >>> print colorList
    
    >>> print <color from list>

3. STAND-ALONE:
    Just open her up in IDLE and you can see the code (and values)
    (It will also run in IDLE)  
    
    
 I am making a very simple Pygame app to go with this, that allows the user to test a colour
 by creating a small window with a background colour displaying a colour of choice
