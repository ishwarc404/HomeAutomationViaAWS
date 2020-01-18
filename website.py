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
    URL = "http://54.152.237.21/return_status"
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
    data_received = json.loads(r.text)
    
    #we need to generalize this code. we cannot have so many if-else conditions
    #for each device. 

    # print(type(data_received))
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
    print("LED IS ON")
    return render_template("index.html")


def led_off():
    # api-endpoint 
    URL = "http://192.168.0.16/LED=OFF"
    # sending get request and saving the response as response object 
    r = requests.post(url = URL) 
    print("LED IS OFF")
    return render_template("index.html")
egrgege
if __name__ == "__main__":
    app.debug  = True
    app.run()