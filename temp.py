from flask import Flask, render_template
import requests
import json


def temp():
    # api-endpoint
    URL = "http://192.168.43.107/TEMP"
    # sending get request and saving the response as response object
    r = requests.post(url=URL)
    print(r.content)


while(True):
    temp()
