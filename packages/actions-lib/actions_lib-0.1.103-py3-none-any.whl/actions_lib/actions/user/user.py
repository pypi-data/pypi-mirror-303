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
    result = {}
    account_info = get_account_info(redis_client, executor)
    user_assets = get_user_assets(redis_client, executor, w3)
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

def get_base_usdc_balance(address: str, w3: Web3) -> float:
    address = Web3.to_checksum_address(address)
    usdc_address = Web3.to_checksum_address(TOKEN_MAPPING['base']['usdc']['address'])
    usdc_contract = w3.eth.contract(
        address=usdc_address,
        abi=ERC20_ABI
    )
    raw_balance = usdc_contract.functions.balanceOf(address).call()
    return raw_balance

def get_user_assets(redis_client, user_id, w3):
    result = []
    chain = 'base'
    user_id = user_id.lower()
    chain = chain.lower()   
    key = f"mpc_address:{user_id}:{chain}"
    
    redis_data = redis_client.hgetall(key)
    if not redis_data:
        result.append({'chain': 'Base', 'token': 'USDC', 'amount': 0 })
        return result
    else:
        usdc_balance = get_base_usdc_balance(redis_data['wallet_address'], w3)
        result.append({'chain': 'Base', 'token': 'USDC', 'amount': usdc_balance})
        return result

def increase_token_amount(redis_client, user_id, chain, token, amount):
    """
    Increase the amount of a specific token for a user on a given chain.

    Args:
        user_id (str): The user ID.
        chain (str): The blockchain network (e.g., 'eth', 'bnb').
        token (str): The token name (e.g., 'usdc', 'eth').
        amount (int): The amount to increase.

    Returns:
        int: The updated amount of the token.
    """
    user_id = user_id.lower()
    chain = chain.lower()
    token = token.lower()
    key = f"user:asset:{user_id}:{chain}"
    # Use HINCRBY to increment the token amount
    new_amount = redis_client.hincrby(key, token, amount)
    return new_amount


def decrease_token_amount(redis_client, user_id, chain, token, amount):
    """
    Decrease the amount of a specific token for a user on a given chain.

    Args:
        user_id (str): The user ID.
        chain (str): The blockchain network (e.g., 'eth', 'bnb').
        token (str): The token name (e.g., 'usdc', 'eth').
        amount (int): The amount to decrease.

    Returns:
        int: The updated amount of the token.

    Raises:
        ValueError: If the token balance is insufficient.
    """
    user_id = user_id.lower()
    chain = chain.lower()
    token = token.lower()

    key = f"user:asset:{user_id}:{chain}"
    # Get the current token amount
    current_amount = redis_client.hget(key, token)
    current_amount = int(current_amount) if current_amount else 0

    # Ensure the balance is sufficient
    if current_amount < amount:
        raise ValueError(f"Insufficient {token.upper()} balance. Current balance: {convert_to_value(current_amount, 6)}")

    # Use HINCRBY to decrement the token amount
    new_amount = redis_client.hincrby(key, token, -amount)
    return new_amount

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
        f"**Inference fee remain balance:** ${convert_to_value(ai_balance, 6)}\n"
        f"**Assets:**\n\n"
    )
    
    # Define the table structure
    table_header = "| Chain | Token | Amount |\n|-------|-------|--------|\n"
    rows = [f"| {asset['chain'].upper()} | {asset['token'].upper()} | {convert_to_value(asset['amount'], 6)} |" for asset in assets]
    table = table_header + "\n".join(rows)
    
    # Combine the header and table into the final Markdown output
    markdown_output = header + table
    return markdown_output

def convert_to_value(amount, decimal):
    amount = amount / (10 ** decimal)
    return float(amount)