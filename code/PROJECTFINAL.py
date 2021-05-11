import board
import pulseio
import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

motor = pulseio.PWMOut(board.D13)
i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)
spkr_pwm = pulseio.PWMOut(board.A3, variable_frequency=True)

frequency = 659

lastTime = time.monotonic()

def pwm_level(pin, inc):
    pin.duty_cycle = int((0.1 * inc) * ((2 ** 16) - 1) - 0.1)

def play(freq):
    spkr_pwm.frequency = freq
    spkr_pwm.duty_cycle = 2 ** 15

def stop():
    spkr_pwm.duty_cycle = 0

def error_beep():
    while True:
        play(650)
        time.sleep(1)
        play(450)
        time.sleep(1)
        play(250)

def readingsensor(SoilVal, TempVal, last_time):
    if SoilVal <= 400:  # Get data from soil sensor dry
        if TempVal <= 0:
            print("Weather is too cold! Bring plant to warmer area.")
            error_beep()
        elif 0 < TempVal <= 13:  # cold data from temp
            print("The plant is dry and the temperature is cold.")
            print("-> Pump on")
            play(frequency)  # Play speaker
            motor.duty_cycle = int(0.4*(2**16-1))
            time.sleep(5)
            motor.duty_cycle = 0
            stop()
        elif 13 < TempVal <= 28:  # moderate data from temp
            print("The plant is dry and the temperature is moderate.")
            print("-> Pump on")
            play(frequency)  # Play speaker
            motor.duty_cycle = int(0.75*(2**16-1))
            time.sleep(5)
            motor.duty_cycle = 0
            stop()
        elif 28 < TempVal <= 36:  # hot data from temp
            print("The plant is dry and the temperature is hot.")
            print("-> Pump on")
            play(frequency)  # Play speaker
            motor.duty_cycle = (2**16-1)
            time.sleep(5)
            motor.duty_cycle = 0
            stop()
        elif 36 < TempVal:  # extreme data from temp
            print("Weather is too hot! Bring plant to cooler area.")
            error_beep()
        else:
            print("Temperature error. Please check sensor.")
            error_beep()
    elif 400 < SoilVal <= 1000:  # Get data from soil sensor (wet)
        print("Soil is already moist and does not need to be watered.")
    elif SoilVal > 1000:
        print("Overwatered! Please check plant.")
        error_beep()
    else:
        print("Soil Moisture error. Please check sensor.")
        error_beep()

def plot(s,t):        # Plot the data print((moisture, temp))
    print((s, t))
    time.sleep(0.5)

while True:
    # Read sensor
    SoilVal = ss.moisture_read()
    TempVal = ss.get_temp()
    plot(SoilVal, TempVal)
    if time.monotonic()-lastTime >= 30:
        lastTime = time.monotonic()
        readingsensor(SoilVal, TempVal, lastTime)
