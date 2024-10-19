import click
import xnat
import logging
from .authenticate import get_credentials, CredentialExpiredError  # Import the custom exception

@click.command()
@click.option('--project', '-d', help="Destination XNAT project.", required=True)
@click.option('--username', '-u', help="Username for XNAT.")
@click.option('--server', '-s', help="Server URL for XNAT.")
@click.option('--password', '-p', hide_input=True, help="XNAT password.")
def archive_to_xnat(project, username, server, password):
    """
    Archive files from prearchive to XNAT project.
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
    logging.info('Starting archiving process.')

    try:
        with xnat.connect(server, user=username, password=password) as session:
            logging.info(f'Connected to XNAT {server}')
            prearchive = session.prearchive.sessions()
            up_sub_list = set()

            for each_prearchive in prearchive:
                try:
                    work_subject = each_prearchive.subject
                    up_sub_list.add(work_subject)
                    scan = each_prearchive.scans
                    sd = scan[0]
                    dcm_list = sd.dicom_dump()

                    # Extracting DICOM tags
                    study_date = next(tag['value'] for tag in dcm_list if tag['desc'] == 'Study Date')
                    study_time = next(tag['value'] for tag in dcm_list if tag['desc'] == 'Study Time')
                    modality = next(tag['value'] for tag in dcm_list if tag['desc'] == 'Modality')

                    # Create experiment label
                    exp_label = f'{work_subject}_{study_date}T{study_time}_{modality}'
                    
                    # Archive to XNAT
                    each_prearchive.archive(subject=work_subject, experiment=exp_label, overwrite="append")
                    logging.info(f'Successfully archived {exp_label} to project {project}.')
                
                except Exception as e:
                    logging.error(f"Error archiving {exp_label}: {e}")

    except Exception as e:
        logging.error(f"Failed to connect to XNAT: {e}")

if __name__ == '__main__':
    archive_to_xnat()
