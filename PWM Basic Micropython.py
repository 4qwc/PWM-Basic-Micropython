# PWM basic Micropython
from machine import Pin, PWM  # กำหนดใช้งานไลบราลี่ PWM
import time

FRQ = 100 # กำหนดความถี่ 0-1000Hz esp8266v3
led = PWM(Pin(5), FRQ) #กำหนด output

while True:
    for i in range(0, 1023):
        led.duty(i)# 0 - 1024 กำหนดค่า % output
        time.sleep_ms(100)

# การทำงานเริ่มต้นที่ กำหนดค่าให้ FRQ (ความถี่ที่ต้องการ 0-1000Hz for ESP8266)
# กำหนด output pin 5 = โมดูล PWM
# ใช้loop while ทำงานตามเป็นจริงจะเข้าทำที่ for
# range(0, 1023)กำหนดให้ทำเริ่มจาก 0 สิ้นสุดที่ 1023
# กำหนดตัวแปร i รับค่าการทำงานแต่ละรอบเก็บที่ i
# led.duty(i) นำค่าไปแสดงผลที่ output
