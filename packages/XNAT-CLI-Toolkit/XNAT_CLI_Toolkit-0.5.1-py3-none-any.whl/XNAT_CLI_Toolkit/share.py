import click
import xnat
import pandas as pd
import logging
from datetime import datetime
import pytz
import os
from .authenticate import get_credentials  # Import the get_credentials function

# Getting date and time for logs
melbtz = pytz.timezone('Australia/Melbourne')
melbdt = datetime.now(melbtz)
str_melbdt = str(melbdt).split('.')[0].replace(':', '_')

# Function to generate URL for API requests
def url_generator(server, is_sub, subject, source, destination, experiment):
    """
    Generate API URL for subject or experiments
    """
    if is_sub:
        api_url = f"{server}data/projects/{source}/subjects/{subject}/projects/{destination}?label={subject}"
    else:
        api_url = f"{server}data/projects/{source}/subjects/{subject}/experiments/{experiment}/projects/{destination}?label={experiment}"
    
    return api_url

@click.command()
@click.option('--server', '-s', prompt=False, help="The XNAT server URL (e.g., http://localhost). If not provided, it will be fetched from stored credentials.")
@click.option('--username', '-u', prompt=False, help="The XNAT username. If not provided, it will be fetched from stored credentials.")
@click.option('--password', '-p', prompt=False, hide_input=True, help="The XNAT password. If not provided, it will be fetched from stored credentials.")
@click.option('--table', '-t', prompt=True, help="Path to CSV file containing the subject, source, and destination project data.")
@click.pass_context
def share_subjects(ctx, server, username, password, table):
    """
    Share subjects and experiments between XNAT projects based on a CSV file.
    """
    # If server, username, or password are not provided via CLI, fetch from get_credentials()
    if not server or not username or not password:
        try:
            stored_server, stored_username, stored_password = get_credentials()
            server = server or stored_server
            username = username or stored_username
            password = password or stored_password
            click.echo(f"Using stored credentials for server: {server}, username: {username}.")
        except Exception as e:
            click.echo(f"Error fetching stored credentials: {e}")
            ctx.exit()

    if not server.endswith("/"):
        server += "/"

    # Reading the CSV file
    df = pd.read_csv(table, dtype={'subject': 'object'})
    subject = df["subject"]
    source = df["source"]
    destination = df["destination"]

    # Set up logging in the current working directory
    current_directory = os.getcwd()
    logs_folder = os.path.join(current_directory, 'logs')
    os.makedirs(logs_folder, exist_ok=True)
    log_file_path = os.path.join(logs_folder, f'{str_melbdt}_share.log')

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ])

    logging.info(f"Connecting to {server} as {username}")
    session = None
    try:
        # Connecting to the XNAT server
        session = xnat.connect(server, user=username, password=password)
        logging.info(f"Successfully connected to {server}")
        
        # Iterate over subjects and share them
        for i in range(len(subject)):
            try:
                src_project = session.projects[source[i]]
                logging.info(f"Source project: {source[i]} is available.")
            except Exception as e:
                logging.error(f"Source project: {source[i]} is not available. Error: {e}")
                continue

            try:
                xnat_sub = src_project.subjects[subject[i]]
                logging.info(f"Subject: {subject[i]} is available in source project: {source[i]}.")
            except Exception as e:
                logging.error(f"Subject: {subject[i]} is not available in source project: {source[i]}. Error: {e}")
                continue

            try:
                dest_project = session.projects[destination[i]]
                logging.info(f"Destination project: {destination[i]} is available.")
            except Exception as e:
                logging.error(f"Destination project: {destination[i]} is not available. Error: {e}")
                continue
            
            # Generate the API URL for the subject
            api_url_sub = url_generator(server, True, subject[i], source[i], destination[i], None)
            try:
                session.put(path=api_url_sub)
                logging.info(f"SUBJECT: {subject[i]} SHARING SUCCESSFUL")
            except Exception as e:
                logging.error(f"SUBJECT: {subject[i]} SHARING FAILED. Error: {e}")
                continue
            
            # Share experiments within the subject
            for each_experiment in xnat_sub.experiments.values():
                api_url_exp = url_generator(server, False, subject[i], source[i], destination[i], each_experiment.label)
                try:
                    session.put(path=api_url_exp)
                    logging.info(f"EXPERIMENT: {each_experiment.label} SHARING SUCCESSFUL")
                except Exception as e:
                    logging.error(f"EXPERIMENT: {each_experiment.label} SHARING FAILED. Error: {e}")
                    continue
    except Exception as e:
        logging.error(f"Failed to connect to XNAT server. Error: {e}")

if __name__ == '__main__':
    share_subjects()
