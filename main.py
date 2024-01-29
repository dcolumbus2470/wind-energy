def on_touch_fwd_button_down():
    fwdMotors.middle_servo.fwd_set_speed(0)
fwdSensors.touch.fwd_on_touch(jacdac.ButtonEvent.DOWN, on_touch_fwd_button_down)

def on_dial1_fwd_dial_turned_direction_ccw(difference):
    fwdMotors.left_servo.fwd_set_speed(fwdSensors.dial1.fwd_position())
fwdSensors.dial1.fwd_on_dial_turned(fwdSensors.DialDirection.CCW,
    on_dial1_fwd_dial_turned_direction_ccw)

def on_dial1_fwd_dial_turned_direction_cw(difference2):
    fwdMotors.left_servo.fwd_set_speed(fwdSensors.dial1.fwd_position())
fwdSensors.dial1.fwd_on_dial_turned(fwdSensors.DialDirection.CW,
    on_dial1_fwd_dial_turned_direction_cw)
