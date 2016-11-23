# 21/11/2016 added some more colors to the list
# need to update colorList with the Added color names

'''
    Author : Ben Woodfield
    Project: PyColor
    Version: 0.1
    Date   : 20.11.2016 (started)
    
    My first module - Pygame Colours (pycolor)
    Takes RGB values for a wide range of colours and stores
    them into variables the pycolor module can then be imported
    into any script to remove the task of setting RGB values
'''


print('           Welcome to PyColor              ')
print('-------------------------------------------')
print('Use: < print(colorList) > for a list of colors')
print('Use: < print(a_color_name) > for R G B values ')
print('-------------------------------------------')
print('Terminal Use: from pycolor import <color>  ')
print('Terminal Use: <print color> to see RGB values')

colorList = 'black | gray | white | red | orange | brown | yellow | green | lime | turquoise | cyan | sky | blue | purple | magenta | pink | crimson | lightPink | hotPink | raspberry | orchid | plum | violet | darkViolet | indigo | navyBlue | cobalt | skyBlue | lightBlue | azure | teal | mint | honeydew | limeGreen | ivory | beige | olive | khaki | banana | gold | wheat | moccasin | eggshell | tan | brick | melon | carrot | chocolate | flesh | sienna | coral | sepia | salmon | tomato | snow | fireBrick | maroon | lightGrey | silver | darkGrey | gray'


# Original colors added originally for testing   

black      = (0,   0,   0  ),
gray       = (142, 142, 142),
white      = (255, 255, 255),
red        = (255,   0,   0),
orange     = (255,  85,   0),
brown      = (160, 112,  80),
yellow     = (255, 255,   0),
green      = ( 81, 197,   0),
lime       = (  0, 255,   0),
turquoise  = (  0, 255, 198),
cyan       = (  0, 255, 255),
sky        = (  0, 127, 255),
blue       = (  0,   0, 255),
purple     = (127,   0, 255),
magenta    = (255,   0, 255),
pink       = (255,   0, 127)
# Added colors (color list information from: http://cloford.com/resources/colours/500col.htm)
crimson    = (220,  20,  60)
lightPink  = (255, 182, 193)
hotPink    = (255, 285, 180)
raspberry  = (135,  38,  87)
orchid     = (218, 112, 214)
plum       = (221, 160, 221)
violet     = (238, 130, 238)
darkViolet = (148,   0, 211)
indigo     = ( 75,   0, 130)
navyBlue   = (  0,   0, 128)
cobalt     = ( 68,  89, 161)
skyBlue    = (135, 206, 235)
lightBlue  = (173, 216, 230)
azure      = (240, 255, 255)
teal       = (  0, 128, 128)
mint       = (189, 151, 201)
honeydew   = (240, 255, 240)
limeGreen  = (  0, 255,   0)
ivory      = (255, 255, 240)
beige      = (245, 245, 220)
olive      = (128, 128,   0)
khaki      = (240, 230, 140)
banana     = (227, 207,  87)
gold       = (255, 215,   0)
wheat      = (245, 222, 179)
moccasin   = (255, 228, 181)
eggshell   = (252, 230, 201)
tan        = (210, 180, 140)
brick      = (156, 102,  31)
melon      = (227, 168, 105)
carrot     = (237, 145,  33)
chocolate  = (210, 105,  30)
flesh      = (225, 125,  64)
sienna     = (160,  82,  45)
coral      = (255, 127,  80)
sepia      = ( 94,  38,  18)
salmon     = (155, 140, 105)
tomato     = (255,  99,  71)
snow       = (255, 250, 250)
fireBrick  = (178,  34,  34)
maroon     = (128,   0,   0)
lightGrey  = (211, 211, 211)
silver     = (192, 192, 192)
darkGrey   = (169, 169, 169)
gray       = (128, 128, 128)
