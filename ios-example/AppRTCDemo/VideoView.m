//
//  VideoView.m
//
/*
 *
 * Last updated by: Gregg Ganley
 * Nov 2013
 *
 */


#import "VideoView.h"

#import "RTCVideoRenderer.h"
#import <QuartzCore/QuartzCore.h>

@interface VideoView () {
    UIInterfaceOrientation _videoOrientation;
    UIColor *_color;
    
    RTCVideoTrack *_track;
    RTCVideoRenderer *_renderer;
}
@property (nonatomic, retain) UIView<RTCVideoRenderView> *renderView;
@property (nonatomic, retain) UIImageView *placeholderView;
@end

@implementation VideoView

#define VIDEO_WIDTH 320
#define VIDEO_HEIGHT 640

static void init(VideoView *self) {
    
    //** not sure if this frame size does anything...
    UIView<RTCVideoRenderView> *renderView = [RTCVideoRenderer newRenderViewWithFrame:CGRectMake(200, 100, 240, 180)];
    [self setRenderView:renderView];
    UIImageView *placeholderView = [[UIImageView alloc] initWithFrame:[renderView frame]];
    [self setPlaceholderView:placeholderView];
    NSDictionary *views = NSDictionaryOfVariableBindings(renderView, placeholderView);
    NSDictionary *metrics = @{@"VIDEO_WIDTH" : @(VIDEO_WIDTH), @"VIDEO_HEIGHT" : @(VIDEO_HEIGHT)};
    
    [placeholderView setTranslatesAutoresizingMaskIntoConstraints:NO];
    [self addSubview:placeholderView];
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self attribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:placeholderView attribute:NSLayoutAttributeCenterX multiplier:1 constant:0]];
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self attribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:placeholderView attribute:NSLayoutAttributeCenterY multiplier:1 constant:0]];

    
    [renderView setTranslatesAutoresizingMaskIntoConstraints:NO];
    [self addSubview:renderView];
    [renderView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"H:[renderView(VIDEO_WIDTH)]" options:0 metrics:metrics views:views]];
    [renderView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"V:[renderView(VIDEO_HEIGHT)]" options:0 metrics:metrics views:views]];
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self attribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:renderView attribute:NSLayoutAttributeCenterX multiplier:1 constant:0]];
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self attribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:renderView attribute:NSLayoutAttributeCenterY multiplier:1 constant:0]];
    

    //** rounded corners of frame
    // [[self layer] setCornerRadius:VIDEO_HEIGHT/2.0];
    [[self layer] setMasksToBounds:YES];
    [self setBackgroundColor:[UIColor redColor]];

}

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        init(self);
    }
    return self;
}

-(id)initWithCoder:(NSCoder *)aDecoder {
    self = [super initWithCoder:aDecoder];
    if (self) {
        init(self);
    }
    return self;
}

-(UIImage *)placeholderImage {
    return [[self placeholderView] image];
}

- (void)setPlaceholderImage:(UIImage *)placeholderImage {
    [[self placeholderView] setImage:placeholderImage];
}

- (UIInterfaceOrientation)videoOrientation {
    return _videoOrientation;
}

-(CGSize)intrinsicContentSize {
    // We add a bit of a buffer to keep the video from showing out of our border
    CGFloat borderSize = 0; //[[self layer] borderWidth];
    return CGSizeMake(VIDEO_HEIGHT + borderSize - 1, VIDEO_HEIGHT + borderSize - 1);
}

- (void)setVideoOrientation:(UIInterfaceOrientation)videoOrientation {
    if (_videoOrientation != videoOrientation) {
        _videoOrientation = videoOrientation;
                
        CGFloat angle;
        switch (videoOrientation) {
            case UIInterfaceOrientationPortrait:
                angle = M_PI_2;
                break;
            case UIInterfaceOrientationPortraitUpsideDown:
                angle = -M_PI_2;
                break;
            case UIInterfaceOrientationLandscapeLeft:
                angle = M_PI;
                break;
            case UIInterfaceOrientationLandscapeRight:
                angle = 0;
                break;
        }
        // The video comes in mirrored. That is fine for the local video, but the remote video should be put back to original
        CGAffineTransform xform = CGAffineTransformMakeScale([self isRemote] ? -1 : 1, 1);
        xform = CGAffineTransformRotate(xform, angle);
        [[self renderView] setTransform:xform];
    }
}

- (void)renderVideoTrackInterface:(RTCVideoTrack *)videoTrack {
    [self stop:nil];
    
    _track = videoTrack;
    
    if (_track) {
        if (!_renderer) {
            _renderer = [[RTCVideoRenderer alloc] initWithRenderView:[self renderView]];
        }
        [_track addRenderer:_renderer];
        [self resume:self];
    }
    //** flip the video over
    [self setVideoOrientation:UIInterfaceOrientationLandscapeLeft];
    [self setVideoOrientation:UIInterfaceOrientationPortrait];
    [self setVideoOrientation:UIInterfaceOrientationLandscapeLeft];
}

#if 0
- (void)orientationChanged:(NSNotification *)notification
{
        UIDeviceOrientation deviceOrientation = [UIDevice currentDevice].orientation;
        CGRect rect = CGRectMake(0, 0, [[UIScreen mainScreen] bounds].size.height, [[UIScreen mainScreen] bounds].size.width);
        
        
        switch (deviceOrientation) {
            case 1:
                [[UIApplication sharedApplication] setStatusBarOrientation:UIInterfaceOrientationPortrait animated:NO];
                [UIView beginAnimations:nil context:NULL];
                [UIView setAnimationDuration:0.1];
                self.view.transform = CGAffineTransformMakeRotation(0);
                self.view.bounds = [[UIScreen mainScreen] bounds];
                [UIView commitAnimations];
                break;
            case 2:
                [[UIApplication sharedApplication] setStatusBarOrientation:UIInterfaceOrientationPortraitUpsideDown animated:NO];
                [UIView beginAnimations:nil context:NULL];
                [UIView setAnimationDuration:0.1];
                self.view.transform = CGAffineTransformMakeRotation(-M_PI);
                self.view.bounds = [[UIScreen mainScreen] bounds];
                [UIView commitAnimations];
                break;
            case 3:
                [[UIApplication sharedApplication] setStatusBarOrientation:UIInterfaceOrientationLandscapeRight animated:NO];
                //rect = CGRectMake(0, 0, [[UIScreen mainScreen] bounds].size.height, [[UIScreen mainScreen] bounds].size.width);
                [UIView beginAnimations:nil context:NULL];
                [UIView setAnimationDuration:0.1];
                self.view.transform = CGAffineTransformMakeRotation(M_PI_2);
                self.view.bounds = rect;
                [UIView commitAnimations];
                break;
            case 4:
                [[UIApplication sharedApplication] setStatusBarOrientation:UIInterfaceOrientationLandscapeLeft animated:NO];
                [UIView beginAnimations:nil context:NULL];
                [UIView setAnimationDuration:0.1];
                //rect = CGRectMake(0, 0, [[UIScreen mainScreen] bounds].size.height, [[UIScreen mainScreen] bounds].size.width);
                self.view.transform = CGAffineTransformMakeRotation(-M_PI_2);
                self.view.bounds = rect;
                [UIView commitAnimations];
                break;
                
            default:
                break;
        }
}
#endif
      
      
      
-(void)pause:(id)sender {
    [_renderer stop];
}

-(void)resume:(id)sender {
    [_renderer start];
}

- (void)stop:(id)sender {
    [_track removeRenderer:_renderer];
    [_renderer stop];
}

#if 0
- (UIImage*)snapshot {
    UIImage *unorientedSnapshot = [[self renderView] snapshot];
    UIImage *snapshot = nil;
    
    // apply view xform into snapshot. we do this rather than keep the orientation as metadata in UIImage because some parts of UIKit don't manage to respect the metadata properly (UIImagePNGRepresentation, UIButton's auto-darkening on press)
    CGAffineTransform xform = [[self renderView] transform];
    if (!CGAffineTransformEqualToTransform(xform, CGAffineTransformIdentity)) {
        CGSize xformedSize = CGRectApplyAffineTransform([unorientedSnapshot us_bounds], xform).size;
        UIGraphicsBeginImageContext(xformedSize);
        CGContextRef ctx = UIGraphicsGetCurrentContext();
        CGContextConcatCTM(ctx, xform);
        [unorientedSnapshot drawInRect:CGContextGetClipBoundingBox(ctx)];
        snapshot = UIGraphicsGetImageFromCurrentImageContext();
        UIGraphicsEndImageContext();
    } else {
        snapshot = unorientedSnapshot;
    }
    
    return snapshot;
}

#endif
@end
