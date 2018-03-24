from flask import Flask
import requests
import json

import base64

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
    dataSend = {
    "requests": [
    {
        "image": {
            "content": str2
        },
        "features": [
            {
                "type": "TEXT_DETECTION"
            }
        ]
    }
    ]
}
    
    r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAzgApTEy_zJacjx7EgA6AGTcEfxl9Gako", json = dataSend)
    response_str = r.text
    #parse it with NLP (Emerson)


    #Add it to google calendar (hardcode for now)
    
    data = {}
    return jsonify(data)

@app.route('/test')
def test():
    return jsonify({'key': 'Value'})

if __name__ == '__main__':
    app.run(debug=True)
