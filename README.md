# EP-Detector
component (likely to be touched by mistake) detection tool on Android


To Run this tool, you also have to:
1.install appium
2.install adb, configure environment variables and make sure you can use command 'adb ...' in cmd directly

The variables you should set including:
1.deviceName in Main.py, which can get by use command 'adb device' in cmd
2.platformVersion in Main.py, the version of Android in your phone
3.TestApp.netCon in AppiumTester.py, in which way your phone get data (wlan or mobile data traffic or you are using imitator)
4.TestApp.appName in AppiumTester.py, the name of the app you will test, if you don't know how to get the Name,you can set this variable to 'None', and start this tool with your phone in the main page of the app you will test.
