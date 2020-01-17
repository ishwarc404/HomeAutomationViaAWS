from flask import Flask, request, render_template
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("server.html")


device_status = { "led_status" : "on"}
@app.route("/led_on") #note this led on is different from what is running on the local server
#this route runs only on the AWS
def led_on():
    device_status["led_status"] = "on"
    return render_template("server.html")

@app.route("/led_off")
def led_off():
    device_status["led_status"] = "off"
    return render_template("server.html")

@app.route("/return_status")
def return_status():
    return_data = json.dumps(device_status)
    return return_data



if __name__ == "__main__" :
    app.debug = True
    app.run()