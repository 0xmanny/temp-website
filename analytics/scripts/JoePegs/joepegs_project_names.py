from duneanalytics import DuneAnalytics
from web3 import Web3, HTTPProvider
from FlatLaunchpeg import abi

def get_dune_data():
    uname = input('Dune Username?\n')
    pwd = input('Dune Password?\n')
    query_id = ''
    while isinstance(query_id, str):
        query_id = input('Query ID?\n')
        try:
            query_id = int(query_id)
        except:
            pass

    dune = DuneAnalytics(uname, pwd)
    dune.login()
    dune.fetch_auth_token()

    result_id = dune.query_result_id(query_id=query_id)
    data = dune.query_result(result_id)

    return {i['data']['project']: [] for i in data['data']['get_result_by_result_id']}

def get_project_data(contract_addrs):
    URL = "https://api.avax.network//ext/bc/C/rpc"
    w3 = Web3(HTTPProvider(URL))

    query = 'WITH project_data AS (\n'

    count = 0
    for addr, data in contract_addrs.items():
        contract = w3.eth.contract(address=Web3.toChecksumAddress(addr),abi=abi)
        try:
            name = contract.functions.name().call().replace("'",'')
        except:
            name = 'UNKNOWN'
        try:
            symbol = contract.functions.symbol().call().replace("'",'')
        except:
            name = 'UNKNOWN'
        try:
            supply = contract.functions.supply().call()
        except:
            name = -1
        data.append(name)
        data.append(symbol)
        data.append(supply)
        query += f"    SELECT '{addr}' AS project, '{name}' AS name, '{symbol}' AS symbol, {supply} AS supply {'UNION' if count + 1 < len(contract_addrs) else ')'}" + '\n'
        count += 1

    return contract_addrs, query

if __name__ == '__main__':
    contract_addrs = get_dune_data()
    project_data, query = get_project_data(contract_addrs)
    with open('joepeg_project_names.sql','w',encoding='utf8') as fout:
        fout.write(query)