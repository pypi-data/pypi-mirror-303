import click
import xnat
import os
from getpass import getpass
import pytz
from datetime import datetime
import logging
from .authenticate import get_credentials, CredentialExpiredError  # Assuming get_credentials is a module that fetches credentials

# Getting date and time for logs
melbtz = pytz.timezone('Australia/Melbourne')
melbdt = datetime.now(melbtz)
str_melbdt = str(melbdt).split('.')[0].replace(' ', '_').replace(':', '-')

current_directory = os.getcwd()

# Create 'logs' folder in the current working directory if it doesn't exist
logs_folder = os.path.join(current_directory, 'logs')
os.makedirs(logs_folder, exist_ok=True)
log_file_path = os.path.join(logs_folder, f'{str_melbdt}_share.log')

# Configuring logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(log_file_path),
    logging.StreamHandler()
])

logging.info(f'pwd: {os.getcwd()}\n')

@click.command()
@click.option('--project', '-d', help="Destination XNAT project.", required=True)
@click.option('--username', '-u', help="Username for XNAT.")
@click.option('--server', '-s', help="Server URL for XNAT.")
@click.option('--source', '-x', help="Directory containing source ZIP files.", required=True)
@click.option('--password', '-p', hide_input=True, confirmation_prompt=False, help="XNAT password.")
@click.pass_context
def upload_and_archive(ctx, project, username, server, password, source):
    """
    Upload and archive DICOM files to XNAT, then update demographic variables for uploaded subjects.
    """
    try:
        # Fetch credentials from get_credentials if not provided
        if not username or not server or not password:
            stored_server, stored_username, stored_password = get_credentials()
            server = server or stored_server
            username = username or stored_username
            password = password or stored_password
    except CredentialExpiredError:
        logging.error("Credentials have expired. Please re-authenticate.")
        return  # Exit the function if credentials are expired

    # Adjust server URL if it doesn't end with '/'
    if not server.endswith('/'):
        server += '/'

    # Getting zip files to upload
    files_list = []
    for root, dirs, files in os.walk(source):
        for each in files:
            if '.zip' in each:
                files_list.append(os.path.join(root, each))

    # Uploading to XNAT prearchive
    up_error_list = []
    up_sub_list = set()

    try:
        with xnat.connect(server, user=username, password=password) as session:
            logging.info(f'Connected to XNAT {server}')
            for up_file in files_list:
                logging.info(f'Uploading {up_file}')
                try:
                    upload_response = session.services.import_(up_file, project=project, destination='/prearchive')
                    logging.info(f'Uploaded to Prearchive. Project: {project}')
                except Exception as e:
                    logging.error(f"Error uploading {up_file}: {e}")
                    up_error_list.append(up_file)

            # Archiving to XNAT Project
            logging.info('Upload completed, now archiving.')
            prearchive = session.prearchive.sessions()
            for each_prearchive in prearchive:
                try:
                    work_subject = each_prearchive.subject
                except IndexError:
                    continue

                up_sub_list.add(work_subject)
                scan = each_prearchive.scans
                sd = scan[0]
                dcm_list = sd.dicom_dump()

                # Initialize variables with default values
                study_date = study_time = modality = 'unknown'

                # Extract DICOM tags with error handling
                for tag_dict in dcm_list:
                    if tag_dict['desc'] == 'Study Date': 
                        study_date = tag_dict['value']
                    elif tag_dict['desc'] == 'Study Time': 
                        study_time = tag_dict['value']
                    elif tag_dict['desc'] == 'Modality': 
                        modality = tag_dict['value']

                try:
                    study_time = study_time.split('.')[0]
                except Exception as e:
                    logging.error(f"Error processing study time: {e}")
                    study_time = '000000'

                exp_label = f'{work_subject}_{study_date}T{study_time}_{modality}'

                try:
                    each_prearchive.archive(subject=work_subject, experiment=exp_label, overwrite="append")
                    logging.info(f'Successfully Archived: {exp_label} to Project: {project}')
                except Exception as e:
                    logging.error(f"Error archiving {exp_label}: {e}")

            # Updating Demographic Custom Variable
            logging.info('Archive completed. Now updating Demographic Variables.')
            project = session.projects[project]
            for xnat_sub in up_sub_list:
                subject = project.subjects[xnat_sub]
                
                subject_age = subject_dob = subject_gender = None

                # Extract demographic data with error handling
                for experiment in subject.experiments.values():
                    for scan in experiment.scans.values():
                        try:
                            ds = scan.dicom_dump()
                            for tag in ds:
                                if subject_age is None and tag['tag1'] == "(0010,1010)":
                                    subject_age = tag["value"] or None
                                if subject_dob is None and tag['tag1'] == "(0010,0030)":
                                    subject_dob = tag["value"] or None
                                if subject_gender is None and tag['tag1'] == "(0010,0040)":
                                    subject_gender = tag["value"] or None
                                
                                if subject_age is not None and subject_dob is not None and subject_gender is not None:
                                    break
                            if subject_age is not None and subject_dob is not None and subject_gender is not None:
                                break
                        except Exception as e:
                            logging.error(f"Error processing DICOM data for subject {xnat_sub}: {e}")

                # Update subject fields with error handling
                if subject_age is not None:
                    subject.fields['subject_age'] = 0 if subject_age[-1] == 'M' else int(subject_age[:-1])

                if subject_dob is not None:
                    subject.fields['subject_dob'] = subject_dob

                if subject_gender is not None:
                    subject.fields['subject_gender'] = {'M': 'Male', 'F': 'Female', 'O': 'Other'}.get(subject_gender, subject_gender)

                logging.info(f'Subject: {xnat_sub}; Age: {subject_age}; Gender: {subject_gender}')

    except Exception as e:
        logging.error(f"Error connecting to XNAT or during processing: {e}")

    # Displaying error files if any
    if len(up_error_list) != 0:
        logging.error('Files failed to upload:')
        for error_file in up_error_list:
            logging.error(error_file)

if __name__ == '__main__':
    upload_and_archive()
