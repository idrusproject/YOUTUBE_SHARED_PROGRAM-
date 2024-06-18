import network
import urequests as requests
import random
import utime

# Function to connect to Wi-Fi
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Wi-Fi connected:", wlan.ifconfig())

# Connect to Wi-Fi (replace 'your_ssid' and 'your_password' with your Wi-Fi credentials)
ssid = 'Max 20A Unfused'
password = 'bonaparte'
connect_to_wifi(ssid, password)

# API endpoint URL and JSON data
api_url = "xxxxxxx"
# api_url = "http://192.168.1.36:8080/idrusproject_tutorial/dashboard/update"
headers = {"CONTENT_TYPE": "application/json"}  # Optional headers

# Initialize the last_request_time
last_request_time = 0

while True:
    current_time = utime.time()

    # Check if it's been 3 seconds since the last request
    if current_time - last_request_time >= 3:
        t = random.randint(20, 40)
        h = random.randint(80, 100)

        data = {
            'temperature': t,
            'humidity': h
        }

        # Send the POST request
        response = requests.post(url=api_url, json=data, headers=headers)

        # Print the response
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.content)

        # Update the last_request_time
        last_request_time = current_time

    # Delay for a short time before checking again
    utime.sleep(0.1)
