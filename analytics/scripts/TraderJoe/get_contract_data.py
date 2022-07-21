from web3 import Web3, HTTPProvider
from get_contract_addresses import read_data 
import pickle, os

URL = "https://api.avax.network//ext/bc/C/rpc"
w3 = Web3(HTTPProvider(URL))

contracts = read_data('contracts.p')
addrs = {i['data']['contract_address']: [] for i in contracts['data']['get_result_by_result_id']}

abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"src","type":"address"},{"indexed":true,"internalType":"address","name":"guy","type":"address"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"dst","type":"address"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"src","type":"address"},{"indexed":true,"internalType":"address","name":"dst","type":"address"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"src","type":"address"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"guy","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

if 'token_data.p' in os.listdir():
    addrs = pickle.load(open('token_data.p','rb'))

count = 0
for addr, contract_data in addrs.items():
    if contract_data:
        count += 1
        continue
    c = w3.eth.contract(address=Web3.toChecksumAddress(addr), abi=abi)
    try:
        name = c.functions.name().call()
    except:
        name = 'Unknown'
    try:
        symbol = c.functions.symbol().call()
    except:
        name = 'Unknown'
    try:
        decimals = c.functions.decimals().call()
    except:
        decimals = -1
    contract_data.extend([
        name,
        symbol,
        decimals
    ])
    count += 1
    if count % 100 == 0:
        pickle.dump(addrs,open('token_data.p','wb'))        
        print(f'{count} Addresses Queried')

pickle.dump(addrs,open('token_data.p','wb'))
count = 0
with open('token_data.sql', 'w', encoding='utf8') as fout:
    fout.write('WITH tokens AS (\n')
    for addr, (name, symbol, decimals) in addrs.items():
        name = name.replace("'",'')
        symbol = symbol.replace("'",'')
        fout.write(f"SELECT '{addr}' AS addr, '{name}' AS name, '{symbol}' AS symbol, {decimals} AS decimals {'UNION' if count < len(addrs) - 1 else ')'}" + '\n')
        count += 1