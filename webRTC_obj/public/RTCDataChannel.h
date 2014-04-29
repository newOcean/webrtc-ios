#import <Foundation/Foundation.h>

@protocol RTCDataChannelDelegate;

// RTCVideoSource is an ObjectiveC wrapper for DataChannelInterface.
@interface RTCDataChannel : NSObject

@property (weak, nonatomic) id<RTCDataChannelDelegate>delegate;

- (void)send:(NSData *)message;

#ifndef DOXYGEN_SHOULD_SKIP_THIS
// Disallow init and don't add to documentation
- (id)init __attribute__(
    (unavailable("init is not a supported initializer for this class.")));
#endif /* DOXYGEN_SHOULD_SKIP_THIS */

@end


@protocol RTCDataChannelDelegate<NSObject>

// Called when new data arrives
- (void)dataChannel:(RTCDataChannel *)dataChannel gotMessage:(NSData *)message;
- (void)dataChannel:(RTCDataChannel *)dataChannel stateChange:(BOOL)isOpen;

@end
