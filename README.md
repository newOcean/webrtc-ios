webRTC iOS example app.

Forked from newOcean.  Updated to the latest webrtc iOS example code from google.  Not sure the trunk directory is needed.

To Run example:

- Build this code for a device (iPad or iPhone).
- Open a Google Chrome browser (not IE, Firefox or Safari - spent a day debugging why Firefox was not working - CHROME!!)
- Open this URL: https://apprtc.appspot.com
- Ensure the camera on your laptop has an image
- Make note of the room number in the URL after loading web page
- Run the iOS app and type in the room number
- Stand back .... Should here feedback audio between your laptop and iOS device.
- NOTE - the audio is the only channel implemented by Google, the video render portion on iOS is not implemented yet.


UPDATE 11/14/13:
- Video support added!
- Now video and audio are both full duplex
- Code is not ideal, needs to be cleaned up, to repeat, CODE IS A HACK and needs clean up
- Big thanks to [Bridger Maxwell] (http://www.bridgermaxwell.com) for the webRTC objC video code - totally could not be done without his help, THANK YOU!
- This [thread](https://groups.google.com/forum/#!msg/discuss-webrtc/vBD_A7gY9Io/I5YFux--6HgJ) on google groups was VERY, VERY helpful
- These libraries are the key to bringing video to life:
    - ios-example/libs/libjingle.a
    - ios-example/libs/libjingle_media.a
    - ios-example/libs/libjingle_peerconnection_objc.a
    - ios-example/libs/libvideo_render_module.a

To build XCode iOS app only for device (not simulator):
- project location: webrtc-ios/ios-example/AppRTCDemo.xcodeproj 
- Open the XCode project and set target for iPad / iPhone
- Build and run
- Should work without changes
(webrtc branch 3.46)

To build the video and jingle libs yourself, which you can then copy back into the ios-example/libs directory:
- Download a copy of the Google WebRTC build tools and code [here](http://www.webrtc.org/reference/getting-started)
    (webrtc branch 3.46)
- Copy the files in the webrtc_obj dir into this dir ...projdir.../trunk/talk/app/webrtc/objc
- Build the AppRTCDemo target: wrios && gclient runhooks && ninja -C out_ios/Debug AppRTCDemo
- Copy the resulting libs back into the Xcode project
      cp ...projdir.../trunk/out_ios/Debug/libvideo_render_module.a ...projdir.../ios_app/webrtc-ios/ios-example/libs
- I am not using the trunk dir provided in this repo.  Using the Google trunk that you downloaded in step one instead. 

Update 4/29/14:
 - Ensured my local repo was in sync with github
 - Set SDK and target device to 7.1
 - Compiled and saw over 100+ errors
 - Determined that "Other Linker Flags" needed to be set to:
       "-stdlib=libstdc++"
 - fixed all 100+ errors
 - URL for stun server in JSON key changed from URL to URLS, so changed parser
 - Ran client SW on my iPhone5 running 7.1
 - Worked!

My Test setup as of 4/29/14:
- MacBook Pro wih OSX 10.9.2
- Chrome browser connected to apprtc.appspot.com
- iPhone5 (iOS7) connected to Xcode 5.1 via debugger
- Occasionaly, I hit an issue with the TURN server not being reachable and need to re-run the app.  Some networks this is worse, e.g. home network versus work.
 

Contributing:
- Fork it
- Create your feature branch (`git checkout -b my_new_feature`)
- Commit your changes (`git commit -m 'Added some feature' -a`)
- Push to the branch (`git push origin my_new_feature`)
- Create a new Pull Request
- Please send in your changes!!

Again, this code needs a lot of cleanup, so please use at own risk.  Enjoy!

## License

Copyright 2013, 2014 Gregg Ganley, All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this project source code except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


[![analytics](http://www.google-analytics.com/collect?v=1&t=pageview&_s=1&dl=https%3A%2F%2Fgithub.com%2Fwebrtc-ios%2Fabout&_u=MAC~&cid=1757014354.1393964045&tid=UA-24755641-1)]()


