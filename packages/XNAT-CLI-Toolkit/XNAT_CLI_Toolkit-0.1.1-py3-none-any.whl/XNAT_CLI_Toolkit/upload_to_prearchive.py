import click
import xnat
import os
import logging
import json
from .authenticate import get_credentials, CredentialExpiredError  # Import the custom exception

@click.command()
@click.option('--project', '-d', help="Destination XNAT project.", required=True)
@click.option('--username', '-u', help="Username for XNAT.")
@click.option('--server', '-s', help="Server URL for XNAT.")
@click.option('--source', '-x', help="Directory containing source ZIP files.", required=True)
@click.option('--password', '-p', hide_input=True, help="XNAT password.")
def upload_to_prearchive(project, username, server, password, source):
    """
    Upload DICOM files to XNAT prearchive.
    """
    # Fetch credentials from get_credentials if not provided
    if not username or not server or not password:
        try:
            stored_server, stored_username, stored_password = get_credentials()
            server = server or stored_server
            username = username or stored_username
            password = password or stored_password
        except CredentialExpiredError as e:
            click.echo(str(e))
            return

    # Adjust server URL if it doesn't end with '/'
    if not server.endswith('/'):
        server += '/'

    # Create log file
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Starting upload to prearchive.')

    # Collect all ZIP files from the source directory
    files_list = [os.path.join(root, file) for root, _, files in os.walk(source) for file in files if file.endswith('.zip')]

    # List to track newly added subject IDs
    new_subjects = []

    try:
        with xnat.connect(server, user=username, password=password) as session:
            logging.info(f'Connected to XNAT {server}')
            up_error_list = []

            for up_file in files_list:
                logging.info(f'Uploading {up_file}')
                try:
                    # Upload the file to the prearchive
                    session.services.import_(up_file, project=project, destination='/prearchive')
                    logging.info(f'Uploaded {up_file} to Prearchive.')

                    # Extract the subject ID from the uploaded file name (or other method)
                    subject_id = os.path.basename(up_file).replace('.zip', '')  # Modify this if needed
                    new_subjects.append(subject_id)

                except Exception as e:
                    logging.error(f"Error uploading {up_file}: {e}")
                    up_error_list.append(up_file)

    except Exception as e:
        logging.error(f"Failed to connect to XNAT: {e}")

    # Save the newly added subjects to a temporary JSON file
    if new_subjects:
        with open('new_subjects.json', 'w') as f:
            json.dump(new_subjects, f)
        logging.info('Saved newly added subjects to new_subjects.json.')

    # Log any upload errors
    if up_error_list:
        logging.error('Files failed to upload:')
        for error_file in up_error_list:
            logging.error(error_file)

if __name__ == '__main__':
    upload_to_prearchive()
