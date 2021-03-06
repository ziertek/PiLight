#!/usr/bin/env python

import contextlib
import io
import colorsys
import spidev
import lib.confParser as config
import unicornhat as unicorn

class PhatWrapper:
    def __init__(self):
        cfg = config.Config()
        self.brightness = cfg.getBrightness()
        self.rotation = cfg.getRotation()
        self.hat = unicorn
        self.hat.set_layout(unicorn.PHAT)
        self.hat.brightness(self.brightness)
        self.hat.rotation(self.rotation)
        self.width,self.height = self.hat.get_shape()

    def getHat(self):
        return self.hat

    def clear(self):
        return self.hat.off()

    def getShape(self):
        return self.width,self.height

    def setAll(self,R,G,B):
        self.hat.set_all(R,G,B)
        self.hat.show()

    def getBrightness(self):
        return self.brightness

    def setPixel(self, x, y, r, g, b):
        self.hat.set_pixel(x, y, r, g, b)

    def show(self):
        self.hat.show()

    def setPixels(r, g, b, jsonObj = None):
        if jsonObj is not None:
                Icon = jsonObj['name']
                for x in range(width):
                        for y in range(height):
                                pixel = jsonObj['pixels'][y][x]
                                if pixel['red'] == -1:
                                        red = r
                                else:
                                        red = pixel['red']
                                if pixel['green'] == -1:
                                        green = g
                                else:
                                        green = pixel['green']
                                if pixel['blue'] == -1:
                                        blue = b
                                else:
                                        blue = pixel['blue']
                                hat.setPixel(x, y, red, green, blue)
        else:
                Icon="none"
                hat.set_all(r,g,b)