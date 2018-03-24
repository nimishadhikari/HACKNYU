import requests
import json
from time import sleep
import base64

with open("poster.JPG", "rb") as imageFile:
    strtest = base64.b64encode(imageFile.read())
    str2 = strtest.decode("utf-8", "backslashreplace")
    #print(str2)

#fh = open("imageToSave.png", "wb")
#fh.write(base64.b64decode(strtest))
#fh.close()

#msg = []
#dict1 = {"image":{"content":"hello"}}
#dict2 = {"features":[{"type":"DOCUMENT_TEXT_DETECTION"}]}

#msg = [dict1, dict2]

#msg_send = {"requests" : msg}

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


#try:
#    json2str = json.dumps(msg_send)
#except:
#    print("Could not json2str")

r = requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAzgApTEy_zJacjx7EgA6AGTcEfxl9Gako", json = dataSend)

print(r.text)
