import utils
reload(utils)
from utils import *
import os
import sys
from sikuli import *

import unittest


class TestFlicker(unittest.TestCase):

    def setUp(self):       
        cleanCache_And_LaunchPSE()

    def test_UI_Flicker(self):
        self.opentestImage()
        wait(2)
        findElement("1543992785068.png")
        clickElementTarget("1543992785068.png", -12, 0)
        wait(2)
        findElement("Flicker.PNG")
        clickElement("Flicker.PNG")
        wait(5)
        if(ElementExists("1546508979791.png")):
            findElement("1546510086268.png")
            clickElement("1546510086268.png")
            wait(5)
            findElement("1546509218301.png")
            clickElement("1546509235029.png")
            self.basicUploadWorkFlow()

          
        elif(ElementExists("1546509218301.png")):
            clickElement("1546509235029.png")
            self.basicUploadWorkFlow()

    def opentestImage(self):
        findElement("1544008989694.png")
        doubleClickElement("1544008989694.png")
        wait(2)
        findElement("1544009057642.png")
        clickElement("1544009057642.png")
        wait(2)
        findElement("1544009532015.png")
        doubleClickElement("1544009532015.png")
        wait(2)
        findElement("1544081241042.png")
        clickElement("1544081241042.png")
        findElement("1544009309405.png")
        clickElement("1544009309405.png")

    def validate(self):
        wait(5)
        assertElementExists("1546510343472.png")
        clickElement("1546510355499.png")
        closePSE()
    
    def tearDown(self):
        closePSE()

    def new_signin(self):
        wait(2)
        typekeysTarget("1546509308011.png", "psetest2016")
        wait(2)
        findElement("1546509567993.png")
        clickElement("1546509567993.png")
        wait(2)
        typeKeys("tester123")
        wait(2)
        findElement("1546509760538.png")
        clickElement("1546509760538.png")

    def already_signin(self):
        findElement("1546511067650.png")
        clickElement("1546511067650.png")
        findElement("1546509567993.png")
        clickElement("1546509567993.png")
        wait(2)
        typeKeys("tester123")
        wait(2)
        findElement("1546509760538.png")
        clickElement("1546509760538.png")

    def authorizeAndUpload(self):
        findElement("1546510708688.png")
        clickElement("1546510708688.png")
        wait(2)
        if(ElementExists("1546509932833.png")):
            findElement("1546509987077.png")
            clickElement("1546509987077.png")
            findElement("1546510030570.png")
            clickElement("1546510042054.png")
            wait(10)
            if(ElementExists("1546510148231.png")):
                findElement("1546510211437.png")
                clickElement("1546510211437.png")
        
    def basicUploadWorkFlow(self):
        if(ElementExists("1546509279794.png")):
            self.new_signin()
            wait(5)
            if(ElementExists("1546509863556.png")):
                self.authorizeAndUpload()
                wait(10)
                self.validate()
        elif(ElementExists("1546511043912.png")):
            self.already_signin()
            wait(5)
            if(ElementExists("1546509863556.png")):
                self.authorizeAndUpload()
                wait(10)
                self.validate()
        elif(ElementExists("1546509863556.png")):
            self.authorizeAndUpload()
            wait(10)
            self.validate()            
        
    