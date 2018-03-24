

from flask import Flask

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


    #parse it with NLP (Emerson)


    #Add it to google calendar (hardcode for now)
    
    data = {}
    return jsonify(data)

@app.route('/test')
def test():
    return jsonify({'key': 'Value'})

if __name__ == '__main__':
    app.run(debug=True)
