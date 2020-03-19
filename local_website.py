from flask import Flask, render_template
import requests
import json
app = Flask(__name__)


@app.route("/")
def index():
    while(True):
        device_status()

    return render_template("index.html")


def device_status():
    # api-endpoint
    #global testting
    # URL = "http://52.0.39.202/return_status"

    #local testing
    URL = "http://127.0.0.1:8000/return_status"
    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    data_received = json.loads(r.text)

    # we need to generalize this code. we cannot have so many if-else conditions
    # for each device.

    if(data_received["led_status"] == "on"):
        led_on()
    else:
        led_off()

    if(data_received["door_status"] == "on"):
        door_open()
    else:
        door_close()
    return render_template("index.html")


def led_on():
    # api-endpoint defw
    URL = "http://192.168.0.111/LED=ON"
    # sending get request and saving the response as response object
    r = requests.post(url=URL)
    print("LED IS ON")
    return render_template("index.html")


def led_off():
    # api-endpoint
    URL = "http://192.168.0.111/LED=OFF"
    # sending get request and saving the response as response object
    r = requests.post(url=URL)
    print("LED IS OFF")
    return render_template("index.html")


def door_open():
    # api-endpoint defw
    URL = "http://192.168.0.111/DOOR=OPEN"
    # sending get request and saving the response as response object
    r = requests.post(url=URL)
    print("DOOR IS OPEN")
    return render_template("index.html")


def door_close():
    # api-endpoint defw
    URL = "http://192.168.0.111/DOOR=CLOSE"
    # sending get request and saving the response as response object
    r = requests.post(url=URL)
    print("DOOR IS OPEN")
    return render_template("index.html")


def temp():
    # api-endpoint
    URL = "http://192.168.0.111/TEMP"
    # sending get request and saving the response as response object
    r = requests.post(url=URL)
    print(r.content)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
