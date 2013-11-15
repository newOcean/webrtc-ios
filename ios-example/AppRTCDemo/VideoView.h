//
//  VideoView.h
//
/*
 *
 * Last updated by: Gregg Ganley
 * Nov 2013
 *
 */

#import <UIKit/UIKit.h>
#import "RTCVideoTrack.h"

@interface VideoView : UIView

@property (nonatomic) UIInterfaceOrientation videoOrientation;
@property (nonatomic, strong) UIImage *placeholderImage;
@property (nonatomic) BOOL isRemote;

- (void)renderVideoTrackInterface:(RTCVideoTrack *)track;
- (void)setVideoOrientation:(UIInterfaceOrientation)videoOrientation;

- (void)pause:(id)sender;
- (void)resume:(id)sender;
- (void)stop:(id)sender;
- (UIImage*)snapshot;

@end
