#import "RTCDataChannel.h"

#include "talk/app/webrtc/datachannelinterface.h"
#include "talk/base/scoped_ref_ptr.h"

@interface RTCDataChannel (Internal)

@property(nonatomic, assign, readonly) talk_base::scoped_refptr<webrtc::DataChannelInterface> dataChannel;

- (id)initWithDataChannel:(talk_base::scoped_refptr<webrtc::DataChannelInterface>)dataChannel;

@end
