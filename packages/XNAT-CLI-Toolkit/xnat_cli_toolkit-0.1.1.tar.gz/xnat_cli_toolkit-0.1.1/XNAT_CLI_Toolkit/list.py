import click
import xnat
import logging
import os
from datetime import datetime
import pytz
from .authenticate import get_credentials


# Getting date and time for logs
melbtz = pytz.timezone('Australia/Melbourne')
melbdt = datetime.now(melbtz)
str_melbdt = str(melbdt).split('.')[0].replace(':', '_')

@click.command()
@click.option('--server', '-s', prompt=False, help="The XNAT server URL (e.g., http://localhost). If not provided, it will be fetched from stored credentials.")
@click.option('--username', '-u', prompt=False, help="The XNAT username. If not provided, it will be fetched from stored credentials.")
@click.option('--password', '-p', prompt=False, hide_input=True, help="The XNAT password. If not provided, it will be fetched from stored credentials.")
@click.option('--project-id', '-pid', prompt=False, help="The XNAT project ID to list subjects. If not provided, it will list all projects.")
def list_projects(server, username, password, project_id):
    """
    List projects or subjects within a specified project on the XNAT server.
    
    If server, username, and password are not provided,
    it will use credentials from the .netrc file.

    If project_id is provided, list subjects in that project.
    If project_id is not provided, list all projects.
    """
    session = None

    # Set up logging in the current working directory
    current_directory = os.getcwd()
    logs_folder = os.path.join(current_directory, 'logs')
    os.makedirs(logs_folder, exist_ok=True)
    log_file_path = os.path.join(logs_folder, f'{str_melbdt}_list_projects.log')

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ])

    try:
        # If CLI options are provided, use them; otherwise, fall back on .netrc
        if server and username and password:
            click.echo("Using provided credentials...")
            logging.info("Using provided credentials for connection.")
        else:
            click.echo("Using credentials from .netrc...")
            server, username, password = get_credentials()
            logging.info("Using credentials from .netrc.")
            click.echo(f"Server: {server}, Username: {username}")

        # Connect to the XNAT server
        session = xnat.connect(server=server, user=username, password=password)

        if session is None:
            click.echo("Failed to connect to the XNAT server.")
            logging.error("Failed to connect to the XNAT server.")
            return

        # If a project ID is provided, list the subjects in that project
        if project_id:
            click.echo(f"Listing subjects for project: {project_id}")
            logging.info(f"Fetching subjects for project {project_id}.")
            try:
                project = session.projects[project_id]
                subjects = project.subjects
                for subject in subjects:
                    click.echo(f"Subject ID: {subject}; Subject Label: {subjects[subject].label}")
                logging.info(f"Fetched subjects for project {project_id}.")
            except KeyError:
                click.echo(f"Project ID '{project_id}' not found.")
                logging.error(f"Project ID '{project_id}' not found.")
        else:
            # If no project ID is provided, list all projects
            click.echo("Listing all projects:")
            logging.info("Fetching all projects.")
            projects = session.projects
            for project in projects:
                click.echo(f"Project ID: {project}")
            logging.info("Fetched all projects.")

    except Exception as e:
        click.echo(f"Error: {str(e)}")
        logging.error(f"Error: {str(e)}")

    finally:
        if session:
            session.disconnect()
            logging.info("Disconnected from the XNAT server.")


if __name__ == '__main__':
    list_projects()
