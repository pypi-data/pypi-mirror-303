from web3 import Web3

from actions_lib.actions.transfer.transfer import ALLOWANCE_ABI, CHAIN_ID_MAPPING, ERC20_APPROVE_ABI, convert_to_wei, get_web3, TOKEN_MAPPING
from actions_lib.actions.type import Action, ActionData

SUPPORTED_TOKENS = {
    "eth": {
        "usdc": "0xd10519Aa03FE7Ffb95189B52B74F94Fb33E2C88a",  # testnet
        # "usdc": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # mainnet
    },
    "base": {
        "usdc": "0x45b58118a5374dccf7fd6f3f66c66278ab7473d9", # testnet
        # "usdc": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", # mainnet
    }
}

CHAIN_NAME_MAPPING = {
    "eth": "ETH",
    "base": "Base"
}

def authorize_token(token, amount, step: any, **kwargs):
    redis_client = kwargs.get("redis_client")
    executor = kwargs.get("executor")
    spender_info = kwargs.get('spender')

    active_chain_key = f"user:active_chain:{executor}"
    active_chain = redis_client.get(active_chain_key) or "base"
    chain_raw = active_chain.lower()
    providers = kwargs.get("providers")

    spender_address = spender_info[chain_raw]['control_address']

    w3 = get_web3(providers, chain_raw)
    amount_to_transfer = convert_to_wei(float(amount), chain_raw, token.lower())
    
    token_address = TOKEN_MAPPING[chain_raw][token.lower()]['address']
    if token_address is not None:
        token_address = w3.to_checksum_address(token_address)
    action_params = {
        "func": "approve",
        "chainId": CHAIN_ID_MAPPING[chain_raw],
        'contract': token_address,
        '_spender': spender_address,
        '_value': amount_to_transfer,
        'abi': ERC20_APPROVE_ABI
    }
    action_data = ActionData(func='', group='', params=action_params)
    action = Action(msg=None, type='wallet', data=action_data.__dict__)
    
    return {'result': {"code": 200, "content": "Authorization parameters are ready"}, 'action': action.__dict__, 'next_action': None }

def show_authorized_tokens(step: any, **kwargs):
    spender_info = kwargs.get('spender')
    providers = kwargs.get('providers')
    executor = kwargs.get("executor")

    result = fetch_approved_amounts(executor, providers, spender_info)
    return { 'result': { 'code': 200, 'content': result }, 'action': None, 'next_action': None }

def get_allowance(providers, chain, token_address, owner, spender):
    web3 = get_web3(providers, chain)
    token_address = Web3.to_checksum_address(token_address)
    contract = web3.eth.contract(address=token_address, abi=ALLOWANCE_ABI)
    spender = Web3.to_checksum_address(spender)
    owner = Web3.to_checksum_address(owner)
    allowance = contract.functions.allowance(owner, spender).call()
    return allowance

def fetch_approved_amounts(owner, providers, spender_info):
    """Iterate over SUPPORTED_TOKENS to fetch the approved allowance for each token and return a Markdown table."""
    markdown_table = "| Token | Allowance |\n|-------|-----------|\n"
    for chain, tokens in SUPPORTED_TOKENS.items():
        for token_name, token_address in tokens.items():
            try:
                spender = spender_info.get(chain.lower()).get('control_address')
                allowance = get_allowance(providers, chain, token_address, owner, spender)
                allowance_in_readable_format = Web3.from_wei(allowance, 'mwei')  # Convert to a readable unit
                # Add a row to the Markdown table
                markdown_table += f"| {CHAIN_NAME_MAPPING[chain]} ({token_name.upper()}) | {allowance_in_readable_format} |\n"
            except Exception as e:
                print(f"Error fetching allowance for {token_name} on {chain}: {e}")
                markdown_table += f"| {CHAIN_NAME_MAPPING[chain]} ({token_name.upper()}) | Error |\n"

    return markdown_table
