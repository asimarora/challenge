import requests
from flask import Flask
from flask import jsonify
import json
import os

app = Flask(__name__)

def get_random_joke(first_name, last_name):
    try:
      joke_uri = os.environ['JOKE_URI']
      target_uri = joke_uri.format(first_name=first_name, last_name=last_name)
      response = requests.request("GET", target_uri)
      if response.status_code != 200:
        return False
      else:
        joke = response.json()['value']['joke']
        return joke
    except Exception as err:
      print ("Error: {0})".format(err))
      return False

def get_random_name():
    try:
      name_uri = os.environ['NAME_URI']
      response = requests.request("GET", name_uri, verify=False)
      if response.status_code != 200:
        return False
      else:
        name = response.json()['name']
        return name
    except Exception as err:
      print ("Error: {0})".format(err))
      return False

@app.route("/", methods=['GET'])
def get_joke():
    try:
      #Get Random Name
      name = get_random_name()
      if name:
        print ("Random name is: {0}".format(name))
        #Split into First and Last Name  
        first, *middle, last = name.split()
        if len(middle):
          last = ' '.join(middle) +  ' ' + last
        
        joke = get_random_joke(first, last)
        if joke:
          print ("Random joke is: {0})".format(joke))
          return jsonify({"Response":joke}), 200
      else:
        return jsonify({"Error": "Unable to handle request"}), 500

    except Exception as err:
      return jsonify({"Error": err}), 500

#Health Status Service 
@app.route("/status", methods=['GET'])
def test_jokes():
    status = 'I am a Nice Joke:)'
    orders_json = json.dumps(status)
    return orders_json, 418


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['JOKE_SERVICE_PORT'], debug=True)
