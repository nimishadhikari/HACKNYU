from flask import Flask, jsonify
import requests
import json

import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/postImage', methods=['POST'])
def postImage():
    if not request.json:
        abort(400)

    #Grab the base64 string from the react app (Nimish)
    base64_string = request.json['string']

    #Send it to the google vision api (Mateo)
    dataSend = makeGoogleVisionData(base64_string)
    
    #Send it early for Nimish to make sure he can connect
    return dataSend


    r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAzgApTEy_zJacjx7EgA6AGTcEfxl9Gako", json = dataSend)
    response_str = r.text
    #parse it with NLP (Emerson)


    #Add it to google calendar (hardcode for now)
    
    data = {}
    return jsonify(data)

@app.route('/test', methods=['GET'])
def test():
    print("route test")
    return jsonify({'key': 'Value'})


def makeGoogleVisionData(base64_string):
    return {
    "requests": [
    {
        "image": {
            "content": base64_string
        },
        "features": [
            {
                "type": "TEXT_DETECTION"
            }
        ]
    }
    ]
}



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

