from machine import Pin, PWM, ADC
import time

# Motor 1
motor1_pwm = PWM(Pin(17), freq=1000)
motor1_in1 = Pin(13, Pin.OUT)

# Motor 2
motor2_pwm = PWM(Pin(11), freq=1000)
motor2_in1 = Pin(12, Pin.OUT)

ldr1 = ADC(Pin(2), atten=ADC.ATTN_11DB)
ldr2 = ADC(Pin(1), atten=ADC.ATTN_11DB)
ldr3 = ADC(Pin(7), atten=ADC.ATTN_11DB)
ldr4 = ADC(Pin(6), atten=ADC.ATTN_11DB)
ldr5 = ADC(Pin(5), atten=ADC.ATTN_11DB)

def drive_forward(speed):
    motor1_pwm.duty_u16(int(65535 * speed))
    motor2_pwm.duty_u16(int(65235 * speed))
    motor1_in1.value(0)  
    motor2_in1.value(1)

def stop():
    motor1_pwm.duty_u16(0)
    motor2_pwm.duty_u16(0)

THRESHOLD = 30000
BASE_SPEED = 0.35
TURN_SPEED = 0.15

last_direction = 0

while True:
    ldr_values = [
        ldr1.read_u16(),
        ldr2.read_u16(),
        ldr3.read_u16(),
        ldr4.read_u16(),
        ldr5.read_u16()
    ]
    
    print(ldr_values)


    left = ldr_values[0] < THRESHOLD
    left_mid = ldr_values[1] < THRESHOLD
    center = ldr_values[2] < THRESHOLD
    right_mid = ldr_values[3] < THRESHOLD
    right = ldr_values[4] < THRESHOLD

    if center:
        drive_forward(BASE_SPEED)
    elif right_mid or right:
        motor1_in1.value(1)
    elif left_mid or left:
        motor2_in1.value(0)

    else:
        motor2_in1.value(0)

    # time.sleep(0.02)