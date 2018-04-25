import binascii
from Savoir import Savoir

rpcuser = 'multichainrpc'
rpcpasswd = 'G5Z1x53jjUBDdpj8Xoe273Kc5mib72XGXMhhcHtjUSv1'
rpchost = '54.163.128.66'
rpcport = '9744'
chainname = 'chain1'

chain_api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

text_string = "hello world"
data_hex = binascii.hexlify(text_string)

return_string = chain_api.publish('poe', 'key6', data_hex)

print return_string + "\n\n"

print chain_api.liststreamitems('poe')





