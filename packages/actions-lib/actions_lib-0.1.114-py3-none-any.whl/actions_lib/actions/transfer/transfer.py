import time
from typing import Tuple, Dict, Any
from web3 import HTTPProvider, Web3
from eth_utils.abi import function_abi_to_4byte_selector, collapse_if_tuple
from actions_lib.actions.consts import CHAIN_ID_MAPPING, TOKEN_MAPPING
from actions_lib.actions.type import Action, ActionData
from actions_lib.utils.contact_tool import get_contact_address
from cdp import *

# ABIs
ALLOWANCE_ABI = """[{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]"""

CONTROL_CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "value", "type": "uint256"},
        ],
        "name": "controlTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {"inputs": [{"internalType": "address", "name": "owner_", "type": "address"}], "name": "setOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "token_", "type": "address"}], "name": "setToken", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {"inputs": [{"internalType": "address", "name": "token_", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "withdraw", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"stateMutability": "payable", "type": "receive"},
    {"inputs": [], "name": "TRANSFER", "outputs": [{"internalType": "bytes4", "name": "", "type": "bytes4"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "TRANSFERFROM", "outputs": [{"internalType": "bytes4", "name": "", "type": "bytes4"}], "stateMutability": "view", "type": "function"},
]

ERC20_APPROVE_ABI = """[{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""

ERC20_TRANSFER_ABI = """[{"constant":false,"inputs":[{"name":"recipient","type":"address"},{"name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""

def mpc_transfer(mpc_address: WalletAddress, destination, chain_raw, token_raw, token_address, amount):
    tx_hash = None
    try:
        if chain_raw == 'base' and token_raw == 'usdc':
            transfer = mpc_address.transfer(amount, 'usdc', destination, gasless=True)
            try:
                transfer.wait()
            except Exception as e:
                print(f"Transfer error: {e}", flush=True)

            timeout = 10  
            start_time = time.time()
            while str(transfer.status) not in ['complete','failed']:
                if time.time() - start_time > timeout:
                    print("Timeout: Transaction status check exceeded 10 seconds.", flush=True)
                    break
                print(f"Waiting for transaction status: {transfer.status}", flush=True)
                transfer.reload()
                tx_hash = str(transfer.transaction_hash)
                time.sleep(1)

            if str(transfer.status) == 'complete':
                status = 200
                transfer_status = 1
                print(f"Transfer complete: {transfer.transaction_hash}", flush=True)
                print(f"Transfer successfully landed on-chain: {transfer.transaction_link}", flush=True)
            else:
                print(f"Error: {transfer.status}")
                status = 500
                transfer_status = 0
                print(f"Transfer failed on-chain: {transfer.transaction_link}", flush=True)

            info = {
                "content": generate_tx_link_content(str(transfer.status), transfer.transaction_link),
                "tx_hash": transfer.transaction_hash,
                "chain": chain_raw,
                "status": transfer_status,
                "code": status
            }

            return info
        else:
            # amount_to_transfer = convert_to_wei(float(amount), chain_raw, token_raw)
            # transfer = default_address.invoke_contract(
            #     contract_address=token_address,
            #     abi=ERC20_TRANSFER_ABI,
            #     method="transfer",
            #     args={"to": destination, "value": amount_to_transfer}
            # )
            info = {
                "content": f"Unsupported token in auto mode. You can try using manual mode.",
                "code": 500
            }
            return info
    except Exception as e:
        error_message = str(e)
        if "Insufficient funds" in error_message:
            error_message += " You need to first deposit USDC into the asset."
            
        print(f"Exception occurred: {e}, Tx hash: {tx_hash}", flush=True)
        info = {
            "content": error_message,
            "code": 500
        }
        return info

def get_web3(providers, chain):
    if providers[chain]['w3'] is None:
        providers[chain]['w3'] = Web3(HTTPProvider(providers[chain]['rpc']))
    return providers[chain]['w3']

def get_user_action_mode(redis_client, user_id):
    user_id = user_id.lower()
    action_mode_key = f"user:action_mode:{user_id}"
    mode = redis_client.get(action_mode_key)
    if mode:
        return mode
    else:
        return 'manual'

def convert_to_wei(amount, chain, token):
    decimal = TOKEN_MAPPING[chain][token.lower()]['decimal']
    amount = float(amount) * (10 ** decimal)
    return int(amount)

def convert_to_value(amount, chain, token):
    decimal = TOKEN_MAPPING[chain][token.lower()]['decimal']
    amount = amount / (10 ** decimal)
    return float(amount)

def get_token_address(chain, token):
    try:
        # Safely access nested keys using .get() to avoid KeyError
        address = TOKEN_MAPPING.get(chain, {}).get(token, {}).get("address")
        return address
    except Exception as e:
        return f"Get token address failed. Error: {str(e)}"

def transfer(receiver: str, amount: float, step: any, chain: str = "base", token: str = "usdc", **kwargs: Any) -> Dict[str, Any]:
    print(f"receiver: {receiver}, amount: {amount}, chain: {chain}, token: {token}, step: {step}", flush=True)
    
    chain_raw = chain.lower()
    executor = kwargs.get("executor")
    redis_client = kwargs.get("redis_client")
    providers = kwargs.get("providers")
    run_mode = get_user_action_mode(redis_client, executor)

    if not providers or chain_raw not in providers:
        raise ValueError(f"Provider for chain {chain} not found")
    
    w3 = get_web3(providers, chain_raw)
    eth_w3 = get_web3(providers, 'eth')
    token_raw = token.lower()
    token_address = get_token_address(chain_raw, token_raw)

    mpc_address = kwargs.get('mpc_address')
    if token_address is not None:
        token_address = w3.to_checksum_address(token_address)
    print(f"token address: {token_address}", flush=True)
    
    if run_mode.lower() == 'auto':
        return handle_auto_transfer(w3, eth_w3, mpc_address, executor, receiver, amount, token_address, redis_client, chain_raw, token_raw)
    else:
        return handle_manual_transfer(w3, eth_w3, executor, receiver, amount, token_address, redis_client, chain_raw, token_raw)

def handle_auto_transfer(w3: Web3, eth_w3, mpc_address, executor, receiver, amount, token_address, redis_client, chain_raw, token_raw):
    if token_raw == 'usdc' and chain_raw == 'base':
        try:
            code, receiver_address = get_contact_address(redis_client, executor, receiver, eth_w3)
            if code != 200:
                return {'result': {"content": f"{receiver_address}", "code": 420}, 'action': None, 'next_action': None}

            to = w3.to_checksum_address(receiver_address)
            executor = w3.to_checksum_address(executor)

            print(f"to: {to}, executor: {executor}", flush=True)
            info = mpc_transfer(mpc_address, to, chain_raw, token_raw, token_address, amount)
            return {'result': info, 'action': None, 'next_action': None}
        except Exception as e:
            return handle_auto_transfer_error(e)
    else:
        # token = token_raw.upper()
        # if token_raw in ['btc', 'cbbtc', 'wbtc']:
        #     if chain_raw == 'base':
        #         token = 'cbBTC'
        #     else:
        #         token = 'WBTC'
        return {'result': {"code": 500, "content": f"Unsupported token in auto mode. You can try using manual mode."}, 'action': None, 'next_action': None}
        

def handle_manual_transfer(w3: Web3, eth_w3, executor, receiver, amount, token_address, redis_client, chain_raw, token_raw):
    active_chain_key = f"user:active_chain:{executor}"
    active_chain = redis_client.get(active_chain_key) or "base"
    print(f"active_chain_key: {active_chain_key}, active_chain: {active_chain}", flush=True)
    
    active_chain_id = CHAIN_ID_MAPPING[active_chain.lower()]
    param_chain_id = CHAIN_ID_MAPPING[chain_raw]
    
    if param_chain_id != active_chain_id:
        return handle_incorrect_network(w3, eth_w3, executor, receiver, amount, chain_raw, token_raw, redis_client)
    
    code, receiver_address = get_contact_address(redis_client, executor, receiver, eth_w3)
    if code != 200:
        return {'result': {"content": f"{receiver_address}", "code": 420}, 'action': None, 'next_action': None}

    amount_to_transfer = convert_to_wei(float(amount), chain_raw, token_raw)
    to = w3.to_checksum_address(receiver_address)
    params = {
        'from': executor,
        'to': to,
        'amount': amount_to_transfer,
        'token': token_address,
        'chain': param_chain_id
    }
    
    if token_address is None:
        # token_address = TOKEN_MAPPING[chain_raw]['usdc']['address']
        params = {
            'to': to,
            'amount': amount_to_transfer,
            'chainId': CHAIN_ID_MAPPING[chain_raw],
            'contract': None,
            'func': 'transferETH',
            'abi': None
        }
    else:
        params = {
            'recipient': to,
            'amount': amount_to_transfer,
            'chainId': CHAIN_ID_MAPPING[chain_raw],
            'contract': token_address,
            'func': 'transfer',
            'abi': ERC20_TRANSFER_ABI
        }
    action_data = ActionData(func='transfer', group='transfer', params=params)
    action = Action(msg=None, type='wallet', data=action_data.__dict__)
    return {'result': {"code": 200, "content": "Manual transfer parameters are constructed"}, 'action': action.__dict__, 'next_action': None}

# def handle_insufficient_allowance(w3, eth_w3, executor, receiver, amount, spender_address, token_address, chain_raw, token_raw, redis_client):
#     amount_to_transfer = convert_to_wei(float(amount), chain_raw, token_raw)
#     action_params = {
#         "func": "approve",
#         "chainId": CHAIN_ID_MAPPING[chain_raw],
#         'contract': token_address,
#         '_spender': spender_address,
#         '_value': amount_to_transfer,
#         'abi': ERC20_APPROVE_ABI
#     }
#     action_data = ActionData(func='', group='', params=action_params)
#     action = Action(msg=None, type='wallet', data=action_data.__dict__)

#     code, receiver_address = get_contact_address(redis_client, executor, receiver, eth_w3)
#     if code != 200:
#         return {'result': {"content": f"{receiver_address}", "code": 420}, 'action': None, 'next_action': None}

#     next_params = {
#         'receiver': w3.to_checksum_address(receiver_address),
#         'amount': amount,
#         'chain': chain_raw,
#         'token': token_raw,
#         'run_mode': 'auto'
#     }
#     next_action_data = ActionData(func='transfer', group='transfer', params=next_params)
#     next_action = Action(msg=None, type='backend', data=next_action_data.__dict__)
#     return {'result': {"code": 200, "content": "Insufficient allowance, proceeding with approval."}, 'action': action.__dict__, 'next_action': next_action.__dict__}

def handle_incorrect_network(w3, eth_w3, executor, receiver, amount, chain_raw, token_raw, redis_client):
    params = {"chainId": CHAIN_ID_MAPPING[chain_raw]}
    action_data = ActionData(func='switch_chain', group='', params=params)
    action = Action(msg=None, type='setting', data=action_data.__dict__)

    code, get_contact_res = get_contact_address(redis_client, executor, receiver, eth_w3)
    if code != 200:
        return {'result': {"content": get_contact_res, "code": code}, 'action': None, 'next_action': None}

    receiver_address = get_contact_res
    next_params = {
        'receiver': w3.to_checksum_address(receiver_address),
        'amount': amount,
        'chain': chain_raw,
        'token': token_raw,
        'run_mode': 'manual'
    }
    next_action_data = ActionData(func='transfer', group='transfer', params=next_params)
    next_action = Action(msg=None, type='backend', data=next_action_data.__dict__)

    return {'result': {'code': 200, 'content': 'Incorrect network, switching to the correct network for you.'}, 'action': action.__dict__, 'next_action': next_action.__dict__}

def maybe_send_transaction(w3: Web3, control_contract, sender_address, token, executor, to, amount_to_transfer, private_key, chain=None, executor_balance=None):
    nonce = w3.eth.get_transaction_count(sender_address)
    current_gas_price = w3.eth.gas_price
    increase = current_gas_price * 25  // 100
    new_gas_price = current_gas_price + increase
    tx = control_contract.functions.transferFromERC20(
        token, executor, to, amount_to_transfer).build_transaction({
            'from': sender_address,
            'nonce': nonce,
            'gasPrice': new_gas_price,
        })
    gas_estimate = w3.eth.estimate_gas(tx)
    tx['gas'] = gas_estimate
    gas_cost = gas_estimate * new_gas_price
    
    print(f"gas_estimate: {gas_estimate}, gas_cost: {gas_cost}, executor_balance: {executor_balance}")
    if executor_balance[chain] < gas_cost:
        return False, 0x0
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    return True, w3.eth.send_raw_transaction(signed_tx.rawTransaction)

def handle_auto_transfer_error(e):
    message = f"Transfer failed with unknown error: {e}"
    return {'result': {"content": message, "status": 0, "code": 500}, 'action': None, 'next_action': None}

def handle_transaction_error(e, control_contract, w3):
    name, params = decode_custom_error(control_contract.abi, w3, str(e))
    if not name:
        message = f"Transfer failed with unknown error: {e}"
    else:
        message = f"Transfer error, error name: {name}, parameters: {params}"
    return {'result': {"content": message, "status": 0, "code": 500}, 'action': None, 'next_action': None}

def generate_markdown_content(status, hash_value, blockchain_explore):
    status_text = "successful" if status == 1 else "failed"
    return f"Transfer {status_text}. You can check the transaction on [blockchain explorer]({blockchain_explore}{hash_value})"


def generate_tx_link_content(status, tx_link):
    status_text = "successful" if status == 'complete' else "failed"
    return f"Transfer {status_text}. You can check the transaction on [blockchain explorer]({tx_link})"


def decode_custom_error(contract_abi, w3, error) -> Tuple[str, str]:
    # Parse error content, the error content must look like:
    # "Call method: submitServiceProof,xxxxx,error:('xxxxxx','xxxxxxx')"
    tmp_array = error.split(":")
    if len(tmp_array) != 3:
        return None, None
    param_str = tmp_array[2]
    param_str = param_str.replace("(","")
    param_str = param_str.replace(")","")
    param_str = param_str.replace(",","")
    param_str = param_str.replace("'","")
    errors = param_str.split()

    for error in [abi for abi in contract_abi if abi["type"] == "error"]:
        # Get error signature components
        name = error["name"]
        data_types = [collapse_if_tuple(abi_input) for abi_input in error.get("inputs", [])]
        error_signature_hex = function_abi_to_4byte_selector(error).hex()
        # Find match signature from error
        for error in errors:
            if error_signature_hex.casefold() == error[2:10].casefold():
                params = ','.join([str(x) for x in w3.codec.decode(data_types,bytes.fromhex(error[10:]))])
                #decoded = "%s(%s)" % (name , str(params))
                return name, params
    return None, None #try other contracts until result is not None since error may be raised from another called contract