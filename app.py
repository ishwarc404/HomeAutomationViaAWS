from flask import Flask,render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/led_on")
# def led_on():
#     # api-endpoint 
#     URL = "http://192.168.0.16/LED=ON"
#     # sending get request and saving the response as response object 
#     r = requests.post(url = URL) 
#     return render_template("index.html")

# @app.route("/led_off")
# def led_off():
#     # api-endpoint 
#     URL = "http://192.168.0.16/LED=OFF"
#     # sending get request and saving the response as response object 
#     r = requests.post(url = URL) 
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.debug  = True
#     app.run()