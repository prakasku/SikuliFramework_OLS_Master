import HTMLTestRunner 
reload(HTMLTestRunner)
import unittest
import os,sys
import xlrd
import datetime

userdir = os.path.expanduser('~')
userdir.replace("\\", "\\\\")
#RootFolder = userdir + "\\Desktop\\SikuliFramework_PSE2019"
RootFolder = "C:\Users\Prakasku\Music\SikuliFramework_PSE2019_integratingFlicker"

if not RootFolder in sys.path: 
    sys.path.append(RootFolder)

from TestScripts import Constants as Constants
reload(Constants)
#from Effects import *
#from Transitions import *
#from GlassPane_GE import *
from Twitter import *
from Flicker import *

suite = unittest.TestSuite()

if len(sys.argv)>1 and str(sys.argv[1]) == "ExecutionviaJenkins":
    print "Test areas have been passed as parameter through Jenkins to TestDriver.sikuli script."
    os.chdir(Constants.RootFolder + "\\BatFiles")
    TestAreas_file = Constants.RootFolder + "\\BatFiles\\TestAreas.txt"
    with open(TestAreas_file) as f:
        testcase_arg = f.readlines()
        testcase_arg = [x.strip() for x in testcase_arg]
    testcase_list = testcase_arg[0].split(",")

else:
    print "Test areas have been passed as parameter through PSE_Test_Execution_Data excel file to TestDriver.sikuli script."
    workbook = xlrd.open_workbook(Constants.TestExecution_DataFile)
    worksheet = workbook.sheet_by_index(0)

    testcase_list = []
    for row in range(worksheet.nrows):
        area_flag = worksheet.cell(row, 4).value
        if area_flag == 1:
            testcase_list.append((str(worksheet.cell(row, 1).value)) + '.' + (str(worksheet.cell(row, 2).value)))

print "Test execution started for below test classes: "

for testcase in testcase_list:
    testCase = testcase.split(".")
    className = testCase[0]
    functionName = testCase[1]
    print className + "." + functionName
    suite.addTest(eval(className)(functionName))

now = datetime.datetime.now()    
outputfilename = Constants.RootFolder + "\\Output\\TestReport_" + str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second) + ".html"
outfile = file(outputfilename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='PSE OLS Tests Execution Report', verbosity=3, dirTestScreenshots = Constants.ScreenshotsFolder, description='This is test report for test execution of OLS tests for Photoshop Elements application.' )
runner.run(suite)