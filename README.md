webRTC iOS example app.

Forked from newOcean.  Updated to the latest webrtc iOS example code from google.  Not sure the trunk directory is needed.

To Run exmample:

- Build this code for a device (iPad or iPhone).
- Open a Google Chrome browser (not IE, Firefox or Safari - spent a day debugging why Firefox was not working - CHROME!!)
- Open this URL: https://apprtc.appspot.com
- Ensure the camera on your laptop has an image
- Make not of the room number in the URL after loading web page
- Run the iOS app and type in the room number
- Stand back .... Should here feedback audio between your laptop and iOS device.
- NOTE - the audio is the only channel implemented by Google, the video render portion on iOS is not implemented yet.


TODO:
- implement the video renderer for iOS, to make the demo full audio and video

