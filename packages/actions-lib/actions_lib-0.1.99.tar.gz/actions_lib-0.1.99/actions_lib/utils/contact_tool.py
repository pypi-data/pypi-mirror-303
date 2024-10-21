from typing import Tuple, Dict
from web3 import Web3
from ens import ENS
import logging

logger = logging.getLogger(__name__)

def default_if_none(value, default="NULL"):
    return default if value is None else value

def redis_add_contact(redis_client, user: str, name: str, address: str, ens_name: str = None) -> Tuple[int, str]:
    """
    Add a contact to the Redis database. 

    :param redis_client: The Redis client instance.
    :param user: The user identifier.
    :param name: The contact name.
    :param address: The contact Ethereum address.
    :param ens_name: The ENS name if available.
    :return: Tuple with status code and message.
    """
    if not Web3.is_address(address):
        return 410, f"Input address: {address} is not a valid Ethereum address"
    
    lower_key = f"{user}_{name}".lower()
    
    # Check if the contact already exists
    if redis_client.hget(f"contact:{lower_key}", "address"):
        return 420, f"Already added {name} to contacts"
    
    redis_client.hset(f"contact:{lower_key}", mapping={
        "address": address,
        "ens_name": default_if_none(ens_name)
    })
    
    return 200, f"Added {name} ({address}) to contacts successfully"

def redis_edit_contact(redis_client, user: str, name: str, address: str, ens_name: str = None) -> Tuple[int, str]:
    """
    Edit an existing contact in the Redis database.

    :param redis_client: The Redis client instance.
    :param user: The user identifier.
    :param name: The contact name.
    :param address: The new contact Ethereum address.
    :param ens_name: The new ENS name if available.
    :return: Tuple with status code and message.
    """
    if not Web3.is_address(address):
        return 410, f"Input address: {address} is not a valid Ethereum address"
    
    lower_key = f"{user}_{name}".lower()
    contact_key = f"contact:{lower_key}"

    # Check if the contact exists
    if not redis_client.exists(contact_key):
        return 404, f"Contact {name} not found"
    
    # Update the contact information
    redis_client.hset(contact_key, mapping={
        "address": address,
        "ens_name": default_if_none(ens_name)
    })
    
    return 200, f"Updated {name} ({address}) in contacts successfully"

def redis_delete_contact(redis_client, user: str, name: str) -> Tuple[int, str]:
    """
    Delete an existing contact from the Redis database.

    :param redis_client: The Redis client instance.
    :param user: The user identifier.
    :param name: The contact name to be deleted.
    :return: Tuple with status code and message.
    """
    lower_key = f"{user}_{name}".lower()
    contact_key = f"contact:{lower_key}"

    # Check if the contact exists
    if not redis_client.exists(contact_key):
        return 404, f"Contact {name} not found"
    
    # Delete the contact
    deleted = redis_client.delete(contact_key)
    
    if deleted:
        return 200, f"Deleted contact {name} successfully"
    else:
        return 500, f"Failed to delete contact {name}"

def get_contact_address(redis_client, user: str, contact: str, w3: Web3) -> Tuple[int, str]:
    """
    Retrieve a contact address. If the contact is an ENS name, resolve it using Web3.

    :param redis_client: The Redis client instance.
    :param user: The user identifier.
    :param contact: The contact name or Ethereum address.
    :param w3: The Web3 instance.
    :return: Tuple with status code and address or error message.
    """
    if Web3.is_address(contact):
        return 200, w3.to_checksum_address(contact)
    
    lower_key = f"{user}_{contact}".lower()
    address = redis_client.hget(f"contact:{lower_key}", "address")

    if not address and contact.endswith(".eth"):
        try:
            ns = ENS.from_web3(w3)
            address = ns.address(contact)
            logger.info(f"Resolved ENS: {contact} -> {address}")
            if not address:
                return 404, f"Cannot find {contact} on ENS, or the address format is incorrect."
        except Exception as e:
            logger.error(f"ENS resolution error: {e}")
            return 500, str(e)
    elif not address:
        return 404, f"Cannot find {contact} in contacts, or the address format is incorrect."
    
    return 200, w3.to_checksum_address(address)

def redis_show_contact(redis_client, user: str, name: str = None) -> Tuple[int, str]:
    """
    Display all contacts for a user in markdown format.

    :param redis_client: The Redis client instance.
    :param user: The user identifier.
    :param name: Optional contact name to filter.
    :return: Tuple with status code and markdown result or error message.
    """
    try:
        contact_mapping = get_user_contacts_mapping(redis_client, user)
        if name:
            contact_mapping = {name: contact_mapping.get(name, None)}
            if not contact_mapping[name]:
                return 404, f"Cannot find {name} in contacts."
        result = generate_markdown(contact_mapping)
    except Exception as e:
        logger.error(f"Error fetching contacts: {e}")
        return 500, str(e)
    
    return 200, result

def get_user_contacts_mapping(redis_client, user: str) -> Dict[str, Dict[str, str]]:
    """
    Retrieve the contact mapping for a specific user.

    :param redis_client: The Redis client instance.
    :param user: The user identifier.
    :return: Dictionary of contact names with addresses and ENS names.
    """
    contact_mapping = {}
    for key in redis_client.scan_iter(match=f"contact:{user.lower()}_*"):
        try:
            name = key.split('_')[-1]
            address = redis_client.hget(key, 'address')
            ens_name = redis_client.hget(key, 'ens_name')
            
            if address:
                contact_mapping[name] = {
                    "address": address,
                    "ens_name": default_if_none(ens_name)
                }
        except Exception as e:
            print(f"Error fetching contact: {e}", flush=True)
    
    return contact_mapping

def generate_markdown(mapping: Dict[str, Dict[str, str]]) -> str:
    """
    Generate a markdown table from a mapping of contacts.

    :param mapping: Dictionary of contact names to details.
    :return: Markdown formatted string.
    """
    markdown_lines = ["| Name | Address | ENS |", "|------|---------|----------|"]
    for name, details in mapping.items():
        address = default_if_none(details.get('address'))
        ens_name = default_if_none(details.get('ens_name'))
        markdown_lines.append(f"| {name} | {address} | {ens_name} |")
    
    return "\n".join(markdown_lines)