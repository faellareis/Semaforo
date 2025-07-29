from machine import Pin
from utime import sleep

print("Hello, ESP32!")

led_verde = Pin(15, Pin.OUT)
led_amarelo = Pin(2, Pin.OUT)
led_vermelho = Pin(4, Pin.OUT)

while True:
    led_verde.on()
    print("Led VERDE ON!")
    sleep(20)
    led_verde.off()
    print("Led VERDE OFF!")
    sleep(0.5)

    led_amarelo.on()
    print("Led AMARELO ON!")
    sleep(10)
    led_amarelo.off()
    print("Led AMARELO OFF!")
    sleep(0.5)

    led_vermelho.on()
    print("Led VERMELHO ON!")
    sleep(7)
    led_vermelho.off()
    print("LED VERMELHO OFF!")
    sleep(0.5)