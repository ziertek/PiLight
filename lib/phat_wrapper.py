#!/usr/bin/env python

# Build as I was having issues with the unicorn wrapper from the project.
# This is just build for the Unicorn pHAT at this point, unlike the original wrapper.

import contextlib
import io
import colorsys
import spidev
import unicornhat as unicorn

class PhatWrapper:
    def __init__(self):
        self.brightness = 0.5
        self.rotation = 180
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