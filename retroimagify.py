#
# retroimagify.py
# 
# Created on: 21.4.2019
# Original author: t33bu (Teemu Leppänen, tjlepp@gmail.com)
# New features: ch0eeb 
#
# This work is licensed under Creative Commons
# Attribution-NonCommercial-ShareAlike (CC BY-NC-SA 4.0)
# https://creativecommons.org/licenses/by-nc-sa/4.0/
 
import os
import sys
import math
from PIL import Image

# Target system
retro_system = ''
resolution = []
palette = []
image_name = ''
# Use target system resolution?
resize = True
# Convert the image into grayscale?
grayScale = False

# Function to read selected system palette from a file
def read_palette(name):
	f = open(name + '.txt','r')
	res = [int(r,16) for r in f.readline().strip().split(',')]
	li = f.readlines()
	pal = [tuple([int(c,16) for c in l.strip().split(',')]) for l in li]
	f.close()
	return res, pal

# Function to calculate distance between the given colors 
# Based on algorithm presented here https://www.compuphase.com/cmetric.htm
def color_distance(i,k):
	rmean = int((i[0]+k[0])/2)
	r = i[0]-k[0]
	g = i[1]-k[1]
	b = i[2]-k[2]
	return math.sqrt((((512+rmean)*r*r)>>8)+4*g*g+(((767-rmean)*b*b)>>8))

# Function to convert given color to closest color in a palette
def convert_color(p):
	dist = []
	for i in palette:
		dist.append(color_distance(p,i))
	return palette[dist.index(min(dist))]

# Main program
# Parse command line
if '-o' in sys.argv:
	retro_system = sys.argv[sys.argv.index('-o')+1]
	resolution,palette = read_palette(retro_system)
else:
	print('Fatal error: no output system given!')
	sys.exit(2)

if '-noresize' in sys.argv:
	resize = False

if '-g' in sys.argv:
	grayScale = True
	
image_name = sys.argv[-1]

# Open image
im = Image.open(image_name)
if resize == True:
	im = im.resize(resolution,Image.ANTIALIAS)
else:
	resolution = im.size
pixels = im.load()

# Run the transformation
for x in range(im.size[0]):
	os.system('cls')
	print('Converting',image_name,'to',retro_system,'with resolution',resolution,'...')
	print(x+1,'/',im.size[0])
	for y in range(im.size[1]):
		pixels[x,y] = convert_color(pixels[x,y])

if grayScale: 
	im = im.convert('LA')

# Save as new image
new_image = image_name.split('.')[0] + '_' + retro_system + '.png'
print('Saving as',new_image, "...")
im.save(new_image)
