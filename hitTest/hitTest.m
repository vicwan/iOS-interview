// 没用的垃圾版本
- (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event {
    UIView *touchView = self;
    if ([self pointInside:point withEvent:event] &&
        (!self.hidden) &&
        self.userInteractionEnabled &&
        (self.alpha > 0.01f))
    {
        for (UIView *subview in self.subviews) {
            CGPoint subPoint = [subview convertPoint:point fromView:self];
            UIView *subTouchView = [subview hitTest:subPoint withEvent:event];
            if (subTouchView) {
                touchView = subTouchView;
                break;
            }
        }
    }else {
        touchView = nil;
    }
    
    return touchView;
}

// 可用版本
- (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event {
    if (!self.isUserInteractionEnabled || self.isHidden || self.alpha <= 0.01) {
        return nil;
    }
    if ([self pointInside:point withEvent:event]) {
        for (UIView *subview in [self.subviews reverseObjectEnumerator]) {
            CGPoint convertedPoint = [subview convertPoint:point fromView:self];
            UIView *hitTestView = [subview hitTest:convertedPoint withEvent:event];
            if (hitTestView) {
                return hitTestView;
            }
        }
        return self;
    }
    return nil;
}
