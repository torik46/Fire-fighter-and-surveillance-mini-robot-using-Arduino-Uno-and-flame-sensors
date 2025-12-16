
"""
Project: Fire Fighter and Surveillance Mini Robot
Platform: Python (Raspberry Pi / Simulation)
Description:
- Reads flame sensor
- Controls motors
- Activates CO2 foam (relay)
"""

import time

# ----- Pin Definitions (BCM numbering assumed) -----
FLAME_SENSOR = 2

M1_IN1 = 5
M1_IN2 = 6
M2_IN3 = 9
M2_IN4 = 10

FOAM_PIN = 8

# ----- Mock GPIO Setup (Replace with RPi.GPIO when using Raspberry Pi) -----
class GPIO:
    BCM = 'BCM'
    OUT = 'OUT'
    IN = 'IN'
    HIGH = 1
    LOW = 0

    @staticmethod
    def setmode(mode): pass

    @staticmethod
    def setup(pin, mode): pass

    @staticmethod
    def input(pin):
        # Simulated flame detection (change to LOW to simulate fire)
        return GPIO.HIGH

    @staticmethod
    def output(pin, state):
        print(f"GPIO {pin} -> {'HIGH' if state else 'LOW'}")


GPIO.setmode(GPIO.BCM)

pins = [M1_IN1, M1_IN2, M2_IN3, M2_IN4, FOAM_PIN]
for p in pins:
    GPIO.setup(p, GPIO.OUT)

GPIO.setup(FLAME_SENSOR, GPIO.IN)

# ----- Robot Control Functions -----
def move_forward():
    GPIO.output(M1_IN1, GPIO.HIGH)
    GPIO.output(M1_IN2, GPIO.LOW)
    GPIO.output(M2_IN3, GPIO.HIGH)
    GPIO.output(M2_IN4, GPIO.LOW)
    print("Robot moving forward")

def stop_robot():
    for p in [M1_IN1, M1_IN2, M2_IN3, M2_IN4]:
        GPIO.output(p, GPIO.LOW)
    print("Robot stopped")

def activate_foam():
    print("Fire detected! Activating CO2 foam...")
    GPIO.output(FOAM_PIN, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(FOAM_PIN, GPIO.LOW)
    print("Fire extinguished")

# ----- Main Loop -----
try:
    while True:
        flame = GPIO.input(FLAME_SENSOR)

        if flame == GPIO.LOW:
            stop_robot()
            activate_foam()
        else:
            move_forward()

        time.sleep(0.5)

except KeyboardInterrupt:
    stop_robot()
    print("System shutdown")
