from flask import Flask,render_template
import requests
import json
app = Flask(__name__)


@app.route("/")
def index():
    while(True):
        led_status()

    return render_template("index.html")

def led_status():
    # api-endpoint 
    URL = "http://3.82.93.9//return_status"
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
    data_received = json.loads(r.text)
    
    print(type(data_received))
    if(data_received["led_status"] == "on"):
        led_on()
    else:
        led_off()
    return render_template("index.html")


def led_on():
    # api-endpoint defw
    URL = "http://192.168.0.16/LED=ON"
    # sending get request and saving the response as response object 
    r = requests.post(url = URL) 
    return render_template("index.html")


def led_off():
    # api-endpoint 
    URL = "http://192.168.0.16/LED=OFF"
    # sending get request and saving the response as response object 
    r = requests.post(url = URL) 
    return render_template("index.html")

if __name__ == "__main__":
    app.debug  = True
    app.run()