import network, time
import urequests, machine, os
from board import rgbled_board, motor
import switch

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('Connected:', wlan.ifconfig())    

connect_wifi("Hiran_2.4", "70913sathu")

def check_for_update():
    print("Checking for updates...")
    try:
        # Replace with your GitHub RAW or local server URL
        version_url = "https://raw.githubusercontent.com/itoon/ota/main/version.txt?time="+time.time()
        code_url = "https://raw.githubusercontent.com/itoon/ota/main/main.py?time="+time.time()

        current_version = "1.0.12"
        r = urequests.get(version_url)
        latest_version = r.text.strip()
        r.close()

        if latest_version != current_version:
            print("New version available:", latest_version)
            r = urequests.get(code_url)
            with open("main.py", "w") as f:
                f.write(r.text)
            r.close()
            print("Update complete, rebooting...")
            machine.reset()
        else:
            print("Already up to date.")
    except Exception as e:
        print("Update failed:", e)

rgbled_board.clear()
motor.turn_left(50, 1)
rgbled_board.set_color(0, '#00ffff')
rgbled_board.set_color(1, '#00ffff')
rgbled_board.show()

def SW1PressCB(_=None):
    print("Already up to date.")
    check_for_update()
switch.pressed(switch.SW1, SW1PressCB)

while True:
    
    pass
