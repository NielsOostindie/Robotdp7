from machine import Pin, PWM, ADC
import time

# Motor 1
motor1_pwm = PWM(Pin(17), freq=1000)
motor1_in1 = Pin(13, Pin.OUT)

# Motor 2
motor2_pwm = PWM(Pin(11), freq=1000)
motor2_in1 = Pin(12, Pin.OUT)

sensorL1 = ADC(Pin(2), atten=ADC.ATTN_11DB)
sensorL2 = ADC(Pin(1), atten=ADC.ATTN_11DB)
sensorM = ADC(Pin(7), atten=ADC.ATTN_11DB)
sensorR2 = ADC(Pin(6), atten=ADC.ATTN_11DB)
sensorR1 = ADC(Pin(5), atten=ADC.ATTN_11DB)


def drive(left_speed, right_speed):
    # Motor 1 = links
    motor1_in1.value(1 if left_speed > 0 else 0)
    motor1_pwm.duty_u16(int(abs(left_speed) * 65535))

    # Motor 2 = rechts
    motor2_in1.value(1 if right_speed > 0 else 0)
    motor2_pwm.duty_u16(int(abs(right_speed) * 65535))

def drive_forward(speed):
    motor1_pwm.duty_u16(int(65535 * speed))
    motor2_pwm.duty_u16(int(65535 * speed))
    motor1_in1.value(0)  
    motor2_in1.value(1)

def stop():
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)

THRESHOLD = 30000
BASE_SPEED = 0.4
TURN_SPEED = 0.2

last_direction = 0

while True:
    lijn_values = [
        sensorL1.read_u16(),
        sensorL2.read_u16(),
        sensorM.read_u16(),
        sensorR2.read_u16(),
        sensorR1.read_u16()
    ]


    print(lijn_values)

    if lijn_values[2] < THRESHOLD:
        drive_forward(BASE_SPEED)
    else: 
        stop()
    print(lijn_values)