print('main')

import ble_uart_peripheral

import time

ble = ble_uart_peripheral.bluethooth.BLE()
BLEuart = ble_uart_peripheral.BLEUART(ble)

def on_rx():
    print("rx: ", BLEuart.read().decode().strip())
    
BLEuart.irq(handler=on_rx)

import async_mqtt_uart