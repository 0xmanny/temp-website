from web3 import Web3
from web3 import HTTPProvider

RPC = 'https://mainnet.optimism.io'
provider = HTTPProvider(RPC)

w3 = Web3(provider)

contracts = [
 '0x03c188a43b3deea4426599f2e582aab6e76417d3',
 '0x06141423dcf1a5a4c137039063ac873cdc1e363a',
 '0x0d693efd716021878d5979fab4cf8f6c1b7ce450',
 '0x207addb05c548f262219f6bfc6e11c02d0f7fdbe',
 '0x226c48ab4986e60f216dd9bff0d784ac2f10a003',
 '0x2441a0952a74994890f3326143032736ec7aada4',
 '0x265013a5915cebb9344c9e259d531e55855da45d',
 '0x278631efe7e7b4c2ec49927b255c2ca42be2c1b1',
 '0x335bd4ffa921160fc86ce3843f80a9941e7456c6',
 '0x3e2882ef90fafab1894bec08f57745a0dd63950a',
 '0x3e5b814cda46765e2fe250f2421fbddf4b879021',
 '0x43c3f2d0aa0ebc433d654bb6ebf67f0c03f8d8d9',
 '0x43ce87a1ad20277b78cae52c7bcd5fc82a297551',
 '0x46b8a98d72820e28465a172687af920cc167e587',
 '0x47029bc8f5cbe3b464004e87ef9c9419a48018cd',
 '0x49b5c691685aaeeaaaff57ab6ccef081a165f5bb',
 '0x4c8b195d33c6f95a8262d56ede793611ee7b5aad',
 '0x4f7ebc19844259386dbddb7b2eb759eefc6f8353',
 '0x534f3135757db41c4f705b0eac697659f68c4014',
 '0x53bea2d15efe344b054e73209455d2b6aa1c9462',
 '0x557949dde71e88cc2f41d33d341ff42417a35a2d',
 '0x587233ce63d7c1e081ce9d94d9940544758f6d01',
 '0x588443c932b45f47e936b969eb5aa6b5fd4f3369',
 '0x58f98be02c4ffb675af8857013a9c0dfa5750d04',
 '0x61eba8151880ea81743795faf3e4042b38e8638c',
 '0x6580c6ee0bb96651be0aa8db382b48ea7acd077d',
 '0x6c5019d345ec05004a7e7b0623a91a0d9b8d590d',
 '0x6fd5bee1ddb4dbbb0b7368b080ab99b8ba765902',
 '0x78fa29412998acedd7728b4cf5623ee5e2f8f589',
 '0x79c912fef520be002c2b6e57ec4324e260f38e50',
 '0x85ff5b70de43fee34f3fa632addd9f76a0f6baa9',
 '0x9056eb7ca982a5dd65a584189994e6a27318067d',
 '0x9355292f66552ea5717b274d27eefc8254011d83',
 '0x93fc04cd6d108588ecd844c7d60f46635037b5a3',
 '0x986d353a3700530be4e75794830f57e657bc68cb',
 '0x9c8a59934fba9af82674eff5d13a24e7c7e7a1f1',
 '0xac49498b97312a6716ef312f389b7e4d183a2a7c',
 '0xadf902b11e4ad36b227b84d856b229258b0b0465',
 '0xb840adae1a31b52778188b9e948fc79a4bc99d44',
 '0xbe61c199d356d205b3beba3634a7992af5e28631',
 '0xc2058aa3b3f96075cc33946bcd1963bfa660315b',
 '0xc4e7cfc1db28fa7d729fdb3617b48dfdd45a4511',
 '0xcdd41009e74bd1ae4f7b2eecf892e4bc718b9302',
 '0xcfcf4bb472aa2ad6c82ebef2377a20829b6356ad',
 '0xd04f675127d37bf7b009453116c17b7ef088cceb',
 '0xd16232ad60188b68076a235c65d692090caba155',
 '0xd3650ab80545c31088f89fb6d16930796758f3c1',
 '0xd62c9d8a3d4fd98b27caaefe3571782a3af0a737',
 '0xdee1856d7b75abf4c1bdf986da4e1c6c7864d640',
 '0xe2ea57fdf87624f4384ef6da5f3844e8e9e5d878',
 '0xe41d6ffc6ca900c063463209e5684f3af6a2bd44',
 '0xe47d437252fe9cb5e74396eee63360d8647df25d',
 '0xe75a3f4bf99882ad9f8aebab2115873315425d00',
 '0xe8537b6ff1039cb9ed0b71713f697ddbadbb717d',
 '0xe8633ce5d216ebfdddf6875067dfb8397dedcaf3',
 '0xec24eb97cec2f0f6a2d61254990b0f163bbbfe1d',
 '0xf813538cd3b3c6195f78353507a16e46f14f1567',
 '0xfb65a99210966813e98594233fbfbcf18cd013e4',
 '0xfd7fddfc0a729ecf45fb6b12fa3b71a575e1966f',
 '0xfdad8f85c0f3895c85301f549d124ce526479bf8',
 '0xffb6c35960b23989037c8c391facebc8a17de970',
 '0xffd74ef185989bff8752c818a53a47fc45388f08'
]

abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Claim","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Fees","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"reserve0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"reserve1","type":"uint256"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"blockTimestampLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimFees","outputs":[{"internalType":"uint256","name":"claimed0","type":"uint256"},{"internalType":"uint256","name":"claimed1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"claimable0","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"claimable1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"}],"name":"current","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentCumulativePrices","outputs":[{"internalType":"uint256","name":"reserve0Cumulative","type":"uint256"},{"internalType":"uint256","name":"reserve1Cumulative","type":"uint256"},{"internalType":"uint256","name":"blockTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fees","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address","name":"tokenIn","type":"address"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint256","name":"_reserve0","type":"uint256"},{"internalType":"uint256","name":"_reserve1","type":"uint256"},{"internalType":"uint256","name":"_blockTimestampLast","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"index0","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"index1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastObservation","outputs":[{"components":[{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint256","name":"reserve0Cumulative","type":"uint256"},{"internalType":"uint256","name":"reserve1Cumulative","type":"uint256"}],"internalType":"struct Pair.Observation","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"metadata","outputs":[{"internalType":"uint256","name":"dec0","type":"uint256"},{"internalType":"uint256","name":"dec1","type":"uint256"},{"internalType":"uint256","name":"r0","type":"uint256"},{"internalType":"uint256","name":"r1","type":"uint256"},{"internalType":"bool","name":"st","type":"bool"},{"internalType":"address","name":"t0","type":"address"},{"internalType":"address","name":"t1","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"observationLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"observations","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint256","name":"reserve0Cumulative","type":"uint256"},{"internalType":"uint256","name":"reserve1Cumulative","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"points","type":"uint256"}],"name":"prices","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"granularity","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"reserve0","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"reserve0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"reserve1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"reserve1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"points","type":"uint256"},{"internalType":"uint256","name":"window","type":"uint256"}],"name":"sample","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stable","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"supplyIndex0","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"supplyIndex1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sync","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokens","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

addr_to_name = dict()

for addr in contracts:
    contract = w3.eth.contract(address=Web3.toChecksumAddress(addr), abi=abi)
    name = contract.functions.name().call()
    addr_to_name[addr] = name

from pprint import pprint
pprint(addr_to_name)