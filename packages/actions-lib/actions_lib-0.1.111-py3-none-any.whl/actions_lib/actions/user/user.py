from web3 import Web3

from actions_lib.actions.consts import TOKEN_MAPPING

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function",
    },
]

def show_account_info(step: any, **kwargs):
    redis_client = kwargs.get('redis_client')
    executor = kwargs.get('executor')
    providers = kwargs.get("providers")
    w3 = providers['base']['w3']
    mpc_address = kwargs.get('mpc_address')
    result = {}
    account_info = get_account_info(redis_client, executor)
    user_assets = get_user_base_assets(mpc_address)
    result['remain_balance'] = account_info['remain_balance']
    result['address'] = executor
    result['assets'] = user_assets

    res = generate_complete_markdown(executor, account_info['remain_balance'], user_assets)
    return {
        'result': {'code': 200, 'content': res},
        'action': None,
        'next_action': None
    } 

def get_account_info(redis_client, user_id):
    user_id = user_id.lower()
    print(f"user_id: {user_id}")
    account_key = f"user:account:{user_id}"
    default_values = {
        'charge_total': '0',
        'action_fee': '0',
        'tx_fee': '0'
    }
    account_info = redis_client.hgetall(account_key)
    default_values.update(account_info)
    result = {k: int(default_values.get(k, '0')) for k in ['charge_total', 'action_fee', 'tx_fee']}
    extra_fund = get_extra_funds(redis_client, user_id)
    
    result['remain_balance'] = result['charge_total'] - result['action_fee'] - result['tx_fee'] + extra_fund
    return result

def get_extra_funds(redis_client, account_id):
    account_id = account_id.lower()
    extra_funds = redis_client.hget(f'user_funds:{account_id}', 'extra_funds')
    return int(extra_funds or 0)

def get_base_usdc_mpc_balance(mpc_address):
    return float(mpc_address.balance('usdc'))

def get_base_usdc_balance(address: str, w3: Web3) -> float:
    address = Web3.to_checksum_address(address)
    # usdc_address = Web3.to_checksum_address(TOKEN_MAPPING['base']['usdc']['address'])
    usdc_address = Web3.to_checksum_address("0x036CbD53842c5426634e7929541eC2318f3dCF7e")
    usdc_contract = w3.eth.contract(
        address=usdc_address,
        abi=ERC20_ABI
    )
    raw_balance = usdc_contract.functions.balanceOf(address).call()
    return raw_balance

def get_user_base_assets(mpc_address):
    result = []
    try:
        usdc_balance = get_base_usdc_mpc_balance(mpc_address)
        result.append({'chain': 'Base', 'token': 'USDC', 'amount': usdc_balance})
    except Exception as e:
        print(f"Error getting USDC balance: {e}", flush=True)
        result.append({'chain': 'Base', 'token': 'USDC', 'amount': 0 })
    return result

# def get_user_assets(redis_client, user_id, w3, mpc_address):
#     result = []
#     chain = 'base-sepolia'
#     user_id = user_id.lower()
#     chain = chain.lower()   
#     key = f"mpc_address:{user_id}:{chain}"
    
#     redis_data = redis_client.hgetall(key)
#     if not redis_data:
#         result.append({'chain': 'Base', 'token': 'USDC', 'amount': 0 })
#         return result
#     else:
#         # usdc_balance = get_base_usdc_balance(redis_data['wallet_address'], w3)
#         usdc_balance = get_base_usdc_mpc_balance(mpc_address)
#         print(f"usdc_balance: {usdc_balance}", flush=True)
#         result.append({'chain': 'Base', 'token': 'USDC', 'amount': usdc_balance})
#         return result

def generate_complete_markdown(user_address, ai_balance, assets):
    """
    Generate a complete Markdown report with user info and assets.

    Args:
        user_address (str): The user's Ethereum address.
        ai_balance (float): The remaining AI balance.
        assets (list): A list of dictionaries with 'chain', 'token', and 'amount'.

    Returns:
        str: A complete Markdown report.
    """
    # Header with user address and AI balance
    header = (
        f"**Account address:** `{user_address}`\n"
        f"**AI service fee balance:** ${convert_to_value(ai_balance, 6)}\n"
        f"**Assets:**\n\n"
    )
    
    # Define the table structure
    table_header = "| Chain | Token | Amount |\n|-------|-------|--------|\n"
    rows = [f"| {asset['chain']} | {asset['token'].upper()} | {asset['amount']} |" for asset in assets]
    table = table_header + "\n".join(rows)
    
    # Combine the header and table into the final Markdown output
    markdown_output = header + table
    return markdown_output

def convert_to_value(amount, decimal):
    amount = amount / (10 ** decimal)
    return float(amount)