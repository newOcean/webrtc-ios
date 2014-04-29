/*
 * libjingle
 * Copyright 2013, Google Inc.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *  1. Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright notice,
 *     this list of conditions and the following disclaimer in the documentation
 *     and/or other materials provided with the distribution.
 *  3. The name of the author may not be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
 * WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
 * EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 * OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/*
 *
 * Last updated by: Gregg Ganley
 * Nov 2013
 *
 */

#import <UIKit/UIKit.h>

#import "GAEChannelClient.h"
#import "APPRTCAppClient.h"
#import "RTCSessionDescriptonDelegate.h"
#import "RTCVideoTrack.h"

// Used to send a message to an apprtc.appspot.com "room".
@protocol APPRTCSendMessage<NSObject>

- (void)sendData:(NSData *)data;
// Logging helper.
- (void)displayLogMessage:(NSString *)message;
@end

@class APPRTCViewController;

// The main application class of the AppRTCDemo iOS app demonstrating
// interoperability between the Objcective C implementation of PeerConnection
// and the apprtc.appspot.com demo webapp.
@interface APPRTCAppDelegate : UIResponder<ICEServerDelegate,
                                           GAEMessageHandler,
                                           APPRTCSendMessage,
                                           RTCSessionDescriptonDelegate,
                                           UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;
@property (strong, nonatomic) APPRTCViewController *viewController;
@property (nonatomic, strong)  RTCVideoTrack *localVideoTrack;

@end
