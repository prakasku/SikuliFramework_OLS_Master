taskkill /F /IM "PhotoshopElementsEditor.exe"
taskkill /F /IM "Adobe QT32 Server.exe"
taskkill /F /IM "DynamicLinkManager.exe"
taskkill /F /IM "dwwin.exe"
taskkill /F /IM "Kill_PSE_Application.exe"
taskkill /F /IM "CrashReporterApp.exe"
taskkill /F /IM "Elements Auto Creations 2019.exe"


rd /s /q "C:\Users\%username%\AppData\Roaming\Adobe\Online Services"
cd "C:\Program Files\Adobe\Photoshop Elements 2019"
start PhotoshopElementsEditor.exe
exit