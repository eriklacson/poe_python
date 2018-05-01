import sys
import json
import binascii
from Savoir import Savoir

#set multichain node settings
rpcuser = 'multichainrpc'
rpcpasswd = 'G5Z1x53jjUBDdpj8Xoe273Kc5mib72XGXMhhcHtjUSv1'
rpchost = '54.163.128.66'
rpcport = '9744'
chainname = 'chain1'
stream = 'poe'
#connect to multichain node
chain_api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

key = 'erik'

#get poe stream
key_item = chain_api.liststreamkeyitems(stream, key)
item_json = binascii.unhexlify(key_item[0]['data'])
#item = json.loads(item_json)

print item_json



