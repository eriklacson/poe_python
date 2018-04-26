#!bin/python
import sys
import binascii
import json
from Savoir import Savoir
from flask import Flask, jsonify, abort, make_response, request, url_for

#set multichain node account parameters
rpcuser = 'multichainrpc'
rpcpasswd = 'G5Z1x53jjUBDdpj8Xoe273Kc5mib72XGXMhhcHtjUSv1'
rpchost = '54.163.128.66'
rpcport = '9744'
stream = "poe"
chainname = 'chain1'

app = Flask(__name__)

#connect to multichain node
chain_api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

#home page
@app.route('/')
def index(): 
    return "Hello, World!"

#get stream info
@app.route('/api/1.0/info')
def get_info():
    chain_info = chain_api.getinfo()
    return jsonify({'chain_info': chain_info})

#get stream item
@app.route('/api/1.0/item/')
def get_items():
    chain_items = chain_api.liststreamitems(stream)
    return jsonify({'chain_items': chain_items})

@app.route('/api/1.0/item/<string:key>')
def get_key_item(key):
    key_item = chain_api.liststreamkeyitems(stream, key)
    return jsonify({'key_item_data': key_item[0]['data']})

#publish hash to the stream
@app.route('/api/1.0/publish/<string:hash>', methods=['POST'])
def publish_item(hash):
    if not request.json:
        abort(400)

    #get item details    
    item = {
        'title': request.json['title'],
        'description': request.json['description'],
        'owner': request.json['owner']
        }

    #convert item dict to json    
    json_item = json.dumps(item)

    #convert json to hex
    data_hex = binascii.hexlify(json_item)

    #publish in data stream with hash as the key
    verify = chain_api.publish('poe', hash, data_hex)
    
    return jsonify({'verify': verify})


if __name__ == '__main__':
    app.run(debug=True)

