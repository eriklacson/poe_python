from Savoir import Savoir
rpcuser = 'multichainrpc'
rpcpasswd = 'G5Z1x53jjUBDdpj8Xoe273Kc5mib72XGXMhhcHtjUSv1'
rpchost = '54.163.128.66'
rpcport = '9744'
chainname = 'chain1'

chain_api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

return_string = chain_api.publish('poe', 'key2', '68656c6c6f20776f726c64')

print chain_api.getinfo()
print chain_api.liststreamitems('poe')
print "success if now error"


