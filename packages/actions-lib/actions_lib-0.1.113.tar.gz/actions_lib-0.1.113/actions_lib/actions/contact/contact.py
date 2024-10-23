from web3 import Web3
from ens import ENS
from actions_lib.utils.contact_tool import redis_add_contact, redis_edit_contact, redis_delete_contact, redis_show_contact
import logging

logger = logging.getLogger(__name__)

def resolve_ens_name(w3: Web3, address: str) -> str:
    """
    Resolves the ENS name for a given Ethereum address.

    :param w3: Web3 instance.
    :param address: Ethereum address.
    :return: ENS name if found, otherwise None.
    """
    try:
        ns = ENS.from_web3(w3)
        ens_name = ns.name(address)
        if ens_name:
            logger.info(f"Resolved ENS name for {address}: {ens_name}")
        else:
            logger.info(f"No ENS name found for the address {address}")
        return ens_name
    except Exception as e:
        logger.error(f"Error resolving ENS name for address {address}: {e}")
        return None

def add_contact(name: str, address: str, step: any, **kwargs) -> dict:
    """
    Adds a contact with the given name and address to the Redis database.

    :param name: Contact name.
    :param address: Contact Ethereum address.
    :param step: Step object in the workflow (details depending on object structure).
    :param kwargs: Additional parameters including redis_client, executor, and providers.
    :return: Result of the add operation.
    """
    redis_client = kwargs.get('redis_client')
    executor = kwargs.get('executor')
    providers = kwargs.get('providers')
    w3 = providers['ethereum']['w3']

    ens_name = resolve_ens_name(w3, address)
    code, res = redis_add_contact(redis_client, executor, name, address, ens_name)

    return {
        'result': {'code': code, 'content': res},
        'action': None,
        'next_action': None
    }

def edit_contact(name: str, address: str, step: any, **kwargs) -> dict:
    
    redis_client = kwargs.get('redis_client')
    executor = kwargs.get('executor')
    providers = kwargs.get('providers')
    w3 = providers['ethereum']['w3']
    ens_name = resolve_ens_name(w3, address)
    code, res = redis_edit_contact(redis_client, executor, name, address, ens_name)
    return {
        'result': {'code': code, 'content': res},
        'action': None,
        'next_action': None
    }

def delete_contact(name: str, step: any, **kwargs) -> dict:
    redis_client = kwargs.get('redis_client')
    executor = kwargs.get('executor')
    code, res = redis_delete_contact(redis_client, executor, name)
    return {
        'result': {'code': code, 'content': res},
        'action': None,
        'next_action': None
    }

def show_contact_by_name(name: str, step: any, **kwargs) -> dict:
    """
    Shows contact details by name.

    :param name: Contact name.
    :param step: Step object in the workflow (details depending on object structure).
    :param kwargs: Additional parameters including redis_client and executor.
    :return: Result of the show operation.
    """
    return show_contacts(name=name, **kwargs)

def show_all_contact(step: any, **kwargs) -> dict:
    """
    Shows all contacts for the executor.

    :param step: Step object in the workflow (details depending on object structure).
    :param kwargs: Additional parameters including redis_client and executor.
    :return: Result of the show operation.
    """
    return show_contacts(name=None, **kwargs)

def show_contacts(name: str = None, **kwargs) -> dict:
    """
    Shows contact details by name or shows all contacts if name is None.

    :param name: Contact name or None to show all.
    :param kwargs: Additional parameters including redis_client and executor.
    :return: Result of the show operation.
    """
    redis_client = kwargs.get('redis_client')
    executor = kwargs.get('executor')

    code, res = redis_show_contact(redis_client, executor, name)

    return {
        'result': {'code': code, 'content': res},
        'action': None,
        'next_action': None
    }