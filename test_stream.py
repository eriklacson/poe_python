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

#connect to multichain node
chain_api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

#get poe stream
poe_stream = chain_api.liststreamitems('poe')
#convert stream to json
poe_json = json.dumps(poe_stream)
#convert stream to dict
poe_dict = json.loads(poe_json)

print poe_stream[0]['txid']





