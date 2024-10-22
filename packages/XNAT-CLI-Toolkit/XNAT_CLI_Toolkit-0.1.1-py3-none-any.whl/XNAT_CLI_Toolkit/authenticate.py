import os
import netrc
import argparse
import json
import time
from datetime import datetime, timedelta

EXPIRATION_TIME = 3600  # 1 hour in seconds

def store_credentials(host, username, password):
    """
    Store credentials in the .netrc file and store the timestamp.
    """
    netrc_file = os.path.expanduser("~/.netrc")

    # Check if the .netrc file exists, create if not
    if not os.path.exists(netrc_file):
        with open(netrc_file, 'w') as f:
            pass

    # Read existing entries
    try:
        netrc_data = netrc.netrc(netrc_file)
    except netrc.NetrcParseError:
        netrc_data = None

    # Update or add new credentials
    with open(netrc_file, 'a') as f:
        if netrc_data and host in netrc_data.hosts:
            print(f"Updating credentials for {host}")
        else:
            print(f"Adding credentials for {host}")
            f.write(f"machine {host}\n")
            f.write(f"login {username}\n")
            f.write(f"password {password}\n")

    # Set file permissions to be secure (only readable by the user)
    os.chmod(netrc_file, 0o600)
    print(f"Credentials for {host} saved to {netrc_file}")

    # Store last entered credentials and timestamp in a JSON file
    last_credentials_file = os.path.expanduser("~/.last_credentials.json")
    last_credentials = {
        "last_host": host,
        "last_username": username,
        "last_password": password,
        "timestamp": time.time()  # Store current time as the timestamp
    }
    with open(last_credentials_file, 'w') as f:
        json.dump(last_credentials, f)
    print(f"Last entered credentials saved to {last_credentials_file}")

def store():
    parser = argparse.ArgumentParser(description="Store host credentials in .netrc")

    # Mark arguments as required
    parser.add_argument("--host", "-s", type=str, required=True, help="XNAT server URL.")
    parser.add_argument("--username", "-u", type=str, required=True, help="XNAT username.")
    parser.add_argument("--password", "-p", type=str, required=True, help="XNAT password.")

    # Automatically show help message if no arguments are provided
    if len(os.sys.argv) == 1:
        parser.print_help()
        os.sys.exit(1)

    args = parser.parse_args()

    store_credentials(args.host, args.username, args.password)

class CredentialExpiredError(Exception):
    """Custom exception for expired credentials."""
    pass

def get_credentials():
    """
    Fetch the last entered host and its credentials from the JSON file.
    Check if the credentials have expired (older than 1 hour).
    """
    try:
        last_credentials_file = os.path.expanduser("~/.last_credentials.json")
        if not os.path.exists(last_credentials_file):
            raise Exception("No last entered credentials found.")

        with open(last_credentials_file, 'r') as f:
            last_credentials = json.load(f)

        last_host = last_credentials.get("last_host")
        last_username = last_credentials.get("last_username")
        last_password = last_credentials.get("last_password")
        timestamp = last_credentials.get("timestamp")

        if timestamp is None:
            raise Exception("Credentials are missing a timestamp.")

        # Check if credentials are expired
        current_time = time.time()
        if current_time - timestamp > EXPIRATION_TIME:
            raise CredentialExpiredError("Credentials have expired.")

        return last_host, last_username, last_password

    except CredentialExpiredError:
        raise CredentialExpiredError("Credentials have expired. Please enter new ones through xnat-authenticatetry.")
    except Exception as e:
        raise Exception(f"Failed to retrieve credentials: {str(e)}")

if __name__ == "__main__":
    store()
