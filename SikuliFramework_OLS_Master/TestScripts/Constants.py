import os, sys

AppPath_PSE = "C:\Program Files\Adobe\Photoshop Elements 2019\PhotoshopElementsEditor.exe"
userdir = os.path.expanduser('~')
userdir.replace("\\", "\\\\")

RootFolder = "C:\Users\Prakasku\Music\SikuliFramework_PSE2019_integratingFlicker"
#RootFolder = userdir + "\\Desktop\\SikuliFramework_PSE2019"

BaselineFolder = RootFolder + "\\TwitterBaselineImages\\"
OutputFolder = RootFolder + "\\Output\\"
TestDataFile_path = RootFolder + "\\TestData\\test.mp4"
Sikuli_Path = userdir + "\\Downloads"
ScreenshotsFolder = RootFolder + "\\Output\\Screenshots"
TestExecution_DataFile = RootFolder + "\\TestData\\PSE_Test_Execution_Data.xls"
BatFilesFolder = RootFolder + "\\BatFiles\\"