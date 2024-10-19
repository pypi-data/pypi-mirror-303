import click
import xnat
import logging
import json
from .authenticate import get_credentials, CredentialExpiredError  # Import the custom exception

@click.command()
@click.option('--project', '-d', help="Destination XNAT project.", required=True)
@click.option('--username', '-u', help="Username for XNAT.")
@click.option('--server', '-s', help="Server URL for XNAT.")
@click.option('--password', '-p', hide_input=True, help="XNAT password.")
@click.option('--new_subjects_file', '-n', default='new_subjects.json', help="Path to the JSON file containing newly added subjects.")
def update_demographics(project, username, server, password, new_subjects_file):
    """
    Update demographic variables for newly added subjects in the XNAT project.
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
    logging.info('Starting update of demographic variables.')

    # Load newly added subjects from JSON file
    try:
        with open(new_subjects_file, 'r') as f:
            new_subjects = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        click.echo("Failed to load new subjects file. Please check the file path and format.")
        return

    with xnat.connect(server, user=username, password=password) as session:
        project = session.projects[project]

        for subject_label in new_subjects:
            subject = project.subjects[subject_label]

            subject_age = subject_dob = subject_gender = None

            for experiment in subject.experiments.values():
                for scan in experiment.scans.values():
                    ds = scan.dicom_dump()
                    for tag in ds:
                        if tag['tag1'] == "(0010,1010)":
                            subject_age = tag["value"] or None
                        if tag['tag1'] == "(0010,0030)":
                            subject_dob = tag["value"] or None
                        if tag['tag1'] == "(0010,0040)":
                            subject_gender = tag["value"] or None

            if subject_age is not None:
                subject.fields['subject_age'] = int(subject_age[:-1]) if subject_age[-1] == 'Y' else 0
            if subject_dob is not None:
                subject.fields['subject_dob'] = subject_dob
            if subject_gender is not None:
                subject.fields['subject_gender'] = {'M': 'Male', 'F': 'Female', 'O': 'Other'}.get(subject_gender, subject_gender)

            logging.info(f'Subject: {subject.label}; Age: {subject.fields.get("subject_age")}; Gender: {subject.fields.get("subject_gender")}')

if __name__ == '__main__':
    update_demographics()
    