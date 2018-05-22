#!bin/python
import sys
import binascii
import json
from flask_bootstrap import Bootstrap
from Savoir import Savoir
from flask import Flask, jsonify, abort, make_response, request, url_for, render_template

#set multichain node account parameters
rpcuser = 'multichainrpc'
rpcpasswd = 'G5Z1x53jjUBDdpj8Xoe273Kc5mib72XGXMhhcHtjUSv1'
rpchost = '54.163.128.66'
rpcport = '9744'
stream = "poe"
chainname = 'chain1'

app = Flask(__name__)
bootstrap = Bootstrap(app)

#connect to multichain node
chain_api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

#home page
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/asset/<string:key>')
def asset(key): 
    return render_template('asset.html', key=key)

@app.route('/publish')
def publish(): 
    return render_template('publish.html')

@app.route('/verify')
def verify(): 
    return render_template('verify.html')

#get stream info
@app.route('/api/1.0/info')
def get_info():
    chain_info = chain_api.getinfo()
    return jsonify({'chain_info': chain_info})

#get stream item
@app.route('/api/1.0/items')
def get_items():
    chain_items = chain_api.liststreamitems(stream)
    return jsonify({'chain_items': chain_items})

@app.route('/api/1.0/item/<string:key>')
def get_key_item(key):
    key_item = chain_api.liststreamkeyitems(stream, key)
    item_json = binascii.unhexlify(key_item[0]['data'])
    item = json.loads(item_json)
    
    return jsonify({'item': item})

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
