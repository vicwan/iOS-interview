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