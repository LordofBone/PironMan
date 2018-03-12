#imports for the envirophat
from envirophat import light
from envirophat import leds
from envirophat import weather
from envirophat import motion

#general imports
import os
import math
import time
import decimal

#OLED screen imports
import Adafruit_SSD1306

#stuff for drawing
import Image
import ImageFont
import ImageDraw

#set reset pins for both OLEDs
RST = 24
RST2 = 23

#setup displays with the correct i2c addresses
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3c)
disp2 = Adafruit_SSD1306.SSD1306_128_64(rst=RST2, i2c_address=0x3d)

#initialise the libraries
disp.begin()
disp2.begin()

#ensure the displays are cleared
disp.clear()
disp.display()
disp2.clear()
disp2.display()

#images
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
image2 = Image.new('1', (width, height))

#create draw objects
draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)

#draw rectangle to erase image
draw.rectangle((0,0,width,height), outline=0, fill=0)
draw2.rectangle((0,0,width,height), outline=0, fill=0)

#determining the direction of north for the heading sensor
north = 294

#load default fonts
font = ImageFont.load_default()

while True:
	
    #draw rectangle to erase image
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw2.rectangle((0,0,width,height), outline=0, fill=0)

	#here the sensor data is assigned to variables
	light_level = light.light()

	r, g, b = light.rgb()

	temp = weather.temperature()

	pressure = weather.pressure()

	x, y, z = motion.accelerometer()
	
	#calculating degrees to north
	corr_heading = (motion.heading() - north) % 360
    
    #here i assign headers to the data from the hat, into labelled strings (minimal labelling due to lens size)
	text_light = ('Lt:' + str(light_level))

	text_rgb = ('R/G/B')
	
	text_rgb_data = (str(r) + '/' + str(g) + '/' + str(b))

	text_temp = ('Tmp:' + str(temp))

	text_pressure = ('Pres: ' + str(pressure))

	text_motion_1 = ('Mot')

	text_motion_2 = ('X:' + str(x))

	text_motion_3 = ('Y:' + str(y))

	text_motion_4 = ('Z:' + str(z))
	
	text_heading = ('Deg:' + str(corr_heading))
	
	#finally the strings are written to the displays
	draw.text((0, 0), text_light, font=font, fill=255)

	draw.text((0, 10), text_rgb, font=font, fill=255)
	
	draw.text((0, 20), text_rgb_data, font=font, fill=255)

	draw.text((0, 30), text_temp, font=font, fill=255)

	draw.text((0, 40), text_pressure, font=font, fill=255)

	draw2.text((0, 0), text_motion_1, font=font, fill=255)

	draw2.text((0, 10), text_motion_2, font=font, fill=255)

	draw2.text((0, 20), text_motion_3, font=font, fill=255)

	draw2.text((0, 30), text_motion_4, font=font, fill=255)
	
	draw2.text((0, 40), text_heading, font=font, fill=255)

	disp.image(image.transpose(Image.FLIP_LEFT_RIGHT))
	disp.display()
	disp2.image(image2.transpose(Image.FLIP_LEFT_RIGHT))
	disp2.display()

	time.sleep(0.1)

