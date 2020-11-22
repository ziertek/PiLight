#!/usr/bin/env python

import confuse

class Config:
    def __init__(self):
        self.config = confuse.Configuration('PiLight', __name__)
        
    def getBrightness(self):
        brightness = self.config['Hat']['Brightness'].get()
        return brightness

    def getRotation(self):
        rotation = self.config['Hat']['Rotation'].get()
        return rotation

    def getWebsiteName(self):
        name = self.config['Web']['Name'].get()
        return name

    def getLabels(self):
        labels = self.config['Web']['Labels'].get()
        return labels