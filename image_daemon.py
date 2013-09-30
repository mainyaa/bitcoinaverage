# Script to create dynamic PNG to include live price

import os
import sys
import requests
import time
from PIL import Image, ImageDraw, ImageFont
from bitcoinaverage.server import FONT_PATH, WWW_DOCUMENT_ROOT
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO


# config locations
url = "https://api.bitcoinaverage.com/ticker/USD"
base = WWW_DOCUMENT_ROOT + "/img/" + "logo_xsmall.png"
font_loc = FONT_PATH + "arialbd.ttf"


def filename():
    filename = WWW_DOCUMENT_ROOT + "price_small" + ".png"
    return filename

def pil_image(rate):

    white = (255,255,255) # colour of background
    grey = (79,79,79)
    light_grey = (247,247,247)
    blue = (66,139,202)
    light_blue = (139,182,220)

    base_im = Image.open(base, 'r') # open base image
    im = Image.new("RGB", [180,55], light_grey)
    draw = ImageDraw.Draw(im)   # create a drawing object that is used to draw on the new image

    rate_text = rate # text to draw
    domain_text = "BitcoinAverage.com"

    # drawing
    draw.text((65,5), rate_text, fill=grey, font=ImageFont.truetype(font_loc, 24))
    draw.text((55,35), domain_text, fill=light_blue, font=ImageFont.truetype(font_loc, 12))
    im.paste(base_im, (2,12))

    # save open image as PNG
    im.save(filename(), 'PNG')

    return filename # and we're done!

def get_rate():
    r = requests.get(url).json()
    rate = "$" + str(r['last'])
    return rate


while True:

    pil_image(get_rate())

    time.sleep(60*5)