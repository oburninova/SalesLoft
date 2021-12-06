from flask import Flask, jsonify
import requests

#Init the app | or creating an object of Flask class
app = Flask(__name__)

#Create the route root for the app
@app.route('/', methods=['GET'])
def home():
    #create request to the target url
    response = requests.get('https://tradestie.com/api/v1/apps/reddit')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        raise "Something Went Wrong."

if __name__ == '__main__':
    #host=0.0.0.0
    #port:5000
    app.run(host='0.0.0.0', port=4000)
