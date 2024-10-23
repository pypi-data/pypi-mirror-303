"""SFTP client."""
import csv
import io
import logging
import os
import tempfile

import paramiko
import pgpy


class SftpClient:
    """Wrapper around the SFTP client for the workflow."""

    def __init__(
        self, host: str, known_host: str, username: str, private_key: str, rsa_pkey: str = None, port: int = 22
    ) -> None:
        """Initialize the SFTP wrapper."""
        self.host = host
        self.known_host = known_host
        self.username = username
        self.private_key = private_key
        self.port = port
        self.rsa_pkey = rsa_pkey

    def get_sftp_client(self) -> paramiko.SFTPClient:
        """Establish and return an SFTP client."""
        try:
            ssh_client = paramiko.SSHClient()
            self.add_host_to_known_hosts()

            # Reject SFTP connection without host added to known hosts file
            ssh_client.load_system_host_keys()
            ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy())

            key_fo: io.StringIO = io.StringIO(self.private_key)
            pkey: paramiko.RSAKey = paramiko.RSAKey.from_private_key(key_fo, password=self.rsa_pkey)

            ssh_client.connect(
                hostname=self.host,
                port=self.port,
                username=self.username,
                pkey=pkey,
            )
            return ssh_client.open_sftp()
        except Exception as error:
            logging.error(f"Failed to connect to SFTP server: {error}")
            raise

    def check_sftp(self, upload_dir: str = None) -> None:
        """Check external services are accessible and required permissions are given."""
        sftp_client = None
        try:
            sftp_client = self.get_sftp_client()

            # Change directory if specified
            if upload_dir:
                sftp_client.chdir(upload_dir)
            else:
                sftp_client.chdir(".")
        finally:
            # Close connections
            if sftp_client:
                sftp_client.close()

    def add_host_to_known_hosts(self):
        """Add known host from config to known hosts file."""
        ssh_dir = os.path.expanduser("~/.ssh")
        known_hosts_file = os.path.join(ssh_dir, "known_hosts")  # Path to known_hosts file

        # Ensure the .ssh directory exists
        os.makedirs(ssh_dir, exist_ok=True)

        # Check if the key is already present in the known_hosts file
        if not os.path.exists(known_hosts_file) or self.known_host not in open(known_hosts_file).read():
            with open(known_hosts_file, "a") as known_hosts:
                known_hosts.write(self.known_host)
            logging.info("Host key for %s added to known_hosts")
        else:
            logging.info("Host key for %s already exists in known_hosts")

    def write_csv_file(
        self, header: tuple, data: list, target_filename: str, upload_dir: str = None, pgp_key: str = None
    ):
        """
        Write data to a CSV file and uploads it to a remote server via SFTP.

        Args:
            header (tuple[str, ...]): A tuple containing the column headers for the CSV file.
            data (list): A list of rows to be written to the CSV file. Each row should be a list of
            values matching the headers.
            upload_dir (str): The directory on the remote SFTP server where the file should be uploaded.
            If not provided, the file is uploaded to the current directory.
            target_filename (str): The name of the file to be saved on the remote server.
        """
        with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(header)
            for row in data:
                writer.writerow(row)

            csv_file.flush()
            csv_file.seek(0)

            sftp_client = self.get_sftp_client()

            # Change directory if specified
            if upload_dir:
                sftp_client.chdir(upload_dir)
            else:
                sftp_client.chdir(".")

            if pgp_key:
                pgp_key, _ = pgpy.PGPKey.from_blob(pgp_key)
                file_message: pgpy.PGPMessage = pgpy.PGPMessage.new(csv_file.name, file=True)
                encrypted_message: pgpy.PGPMessage = pgp_key.encrypt(file_message)
                csv_io: io.StringIO = io.StringIO(str(encrypted_message))
                sftp_client.putfo(csv_io, target_filename, confirm=False)
            else:
                # Upload file
                sftp_client.putfo(csv_file, target_filename, confirm=False)

            sftp_client.close()
