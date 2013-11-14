webRTC iOS example app.

Forked from newOcean.  Updated to the latest webrtc iOS example code from google.  Not sure the trunk directory is needed.

To Run example:

- Build this code for a device (iPad or iPhone).
- Open a Google Chrome browser (not IE, Firefox or Safari - spent a day debugging why Firefox was not working - CHROME!!)
- Open this URL: https://apprtc.appspot.com
- Ensure the camera on your laptop has an image
- Make not of the room number in the URL after loading web page
- Run the iOS app and type in the room number
- Stand back .... Should here feedback audio between your laptop and iOS device.
- NOTE - the audio is the only channel implemented by Google, the video render portion on iOS is not implemented yet.


UPDATE 11/14/13:
- Video support added!
- Now video and audio are both full duplex
- Code is very ugly, needs to be cleaned up
- Big thanks to [Bridger Maxwell] (http://www.bridgermaxwell.com) for the webRTC objC video code - totally could not be done without his help, THANK YOU!
- This [thread](https://groups.google.com/forum/#!msg/discuss-webrtc/vBD_A7gY9Io/I5YFux--6HgJ)


TO build the libs yourself:
- Copy the webrtc_obj files into this dir <projdir>/trunk/talk/app/webrtc/objc
- build the AppRTCDemo: wrios && gclient runhooks && ninja -C out_ios/Debug AppRTCDemo
- copy libs into Xcode build cp <projdir>/trunk/out_ios/Debug/libvideo_render_module.a <projdir>/ios_app/webrtc-ios/ios-example/libs


