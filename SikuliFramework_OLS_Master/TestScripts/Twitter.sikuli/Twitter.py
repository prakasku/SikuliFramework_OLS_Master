import utils
reload(utils)
from utils import *
import os
import sys
from sikuli import *

import unittest


class TestTwitter(unittest.TestCase):

    def setUp(self):       
        cleanCache_And_LaunchPSE()

    def test_UI_Twitter(self):

        self.opentestImage()
        wait(2)
        findElement("1543992785068.png")
        clickElementTarget("1543992785068.png", -12, 0)
        wait(2)
        findElement("twitter.png")
        clickElement("twitter.png")
        wait(20)
        if(ElementExists("1543993047928.png")):
            findElement("1543993091861.png")
            clickElement("1543993091861.png")
            wait(10)
            findElement("1543992785068.png")
            rightClickElementTarget("1543992785068.png", 30, 0)
            findElement("twitter.png")
            clickElement("twitter.png")
            wait(2)
            if(ElementExists("1543997926494.png")):
                self.authorizeAndTweet()
                self.validate()
            #else:
            #   print("Testcase Failed: PSE-OLS Service Twitter is not initialized")
            #    exit()

        elif(ElementExists("1543997926494.png")):
            self.authorizeAndTweet()
            self.validate() 
        else:
            assertNegativeElementExists("Internet_FirewallConnection Issue.png")
        #    print("Testcase Failed: Seems to be an issue with internet connection or firewall")
        #   exit()
        #else:
        #    print("Testcase Failed: PSE-OLS Service Twitter is not initialized")

    def tearDown(self):
        closePSE()

    def validate(self):

        assertElementExists("1543999022316.png")
        clickElement("1544088134641.png")
        #    print("Testcase Passed, Image Posted on Twitter")
        #elif(assertNegativeElementExists("imageSizeMoreThan3MB.png")):
        closePSE()
        #    print("Testcase Failed, File size greater than 3MB")
        #   exit()
        #else:
        #    assertElementExists("1543999022316.png")
        #   print("Testcase Failed: Issue with Upload")
        #   exit()
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

        
    def authorizeAndTweet(self):
        
        clickElement("authorize.png")

        if(ElementExists("twitter_login.png") and ElementExists("twitter_login2.png")):
            typeKeysTarget("username.png", "psetest2016@gmail.com")
            clickElement("username-password.png")
            typeKeysTarget("password.png", "tester123")
            clickElement("login_authorize.png")
            wait(15)

        elif(ElementExists("twitter_loggedin.png")):
            clickElement("twitter_loggedin_authorize.png")
            wait(15)

        if(ElementExists("login_success.png")):
            findElement("minimize.png")
            clickElement("minimize.png")
            findElement("1543998864417.png")
            clickElement("1543998899982.png")
            wait(10)
            findElement("1543998954499.png")
            findElement("1544005497790.png")
            clickElement("1544005497790.png")
            typeKeys("PSE_OLS_Testing")
            clickElement("1543998971026.png")
            wait(10)
        #else:
        #   print("Testcase Failed: Verify login Credentials")
        #    exit()


    
    