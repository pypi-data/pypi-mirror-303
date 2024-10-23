from __future__ import annotations

import json
import logging
import os
import pickle
import shutil
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Final, List
from uuid import uuid4
from zipfile import ZipFile

import click
import jmespath
import requests
from dacite import from_dict
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from hurry.filesize import size
from requests import JSONDecodeError, Session

from kaas_cli.config import DEFAULT_PROJECT_ID, DEFAULT_TOKEN, SERVER_URL
from kaas_cli.types import KaasCliException

from .types import Job

if TYPE_CHECKING:
    from .types import File_Data, Metadata

from kaas_cli.types import Cache

from .constants import (
    CONFIG_LOG_PATH,
    CONFIG_SESSION_PATH,
    DEVICE_LOGIN_URL,
    GRAPHQL_URL,
    KONTROL_JOB_URL,
    ORG_VAULT_CACHE_URLS,
    ORG_VAULT_CACHES_SYNC_S3_URL,
    ORG_VAULT_CACHES_URL,
    ORGANIZATIONS_URL,
    UPLOAD_SUCCESS_MESSAGE,
    USER_URL,
    VAULTS_ROOT_URL,
)


@dataclass(frozen=True)
class DeviceAuth:
    device_code: str
    expires_in: int
    interval: int
    user_code: str
    verification_uri: str


@dataclass(frozen=True)
class Confirmation:
    success: bool


class CustomSession(Session):
    def get(self, *args: Any, **kwargs: Any) -> Any:
        response = super().get(*args, **kwargs)
        try:
            json_response = response.json()
            if 'error' in json_response:
                raise ValueError(json_response['error'], json_response.get('message', 'No message provided'))
            return json_response
        except JSONDecodeError as e:
            logging.error(f"GET request JSON decode failed: {e}")
            raise e
        except ValueError as e:
            logging.error(f"GET request failed: {e}")
            raise e

    def post(self, *args: Any, **kwargs: Any) -> Any:
        response = super().post(*args, **kwargs)
        try:
            json_response = response.json()
            if 'error' in json_response:
                raise ValueError(json_response['error'], json_response.get('message', 'No message provided'))
            return json_response
        except JSONDecodeError as e:
            logging.error(f"POST request JSON decode failed: {e}")
            raise e
        except ValueError as e:
            logging.error(f"POST request failed: {e}")
            click.echo(f"POST request failed: {e}")
            raise e

    def post_return_no_content(self, *args: Any, **kwargs: Any) -> None:
        response = super().post(*args, **kwargs)
        try:
            if not response.ok:
                raise ValueError(response.text)
        except ValueError as e:
            logging.error(f"POST request failed: {e}")
            raise e

    def get_text(self, *args: Any, **kwargs: Any) -> Any:
        response = super().get(*args, **kwargs)
        return response.text


class AuthenticatedSession(CustomSession):
    def __init__(self, access_token: str) -> None:
        super().__init__()
        self.access_token = access_token
        self.headers.update({'Authorization': f'Bearer {self.access_token}'})


class KaasClient:
    _client: Client
    _session: CustomSession
    _url: str
    _token: str | None
    _vault: str | None
    _org: str | None

    def __init__(
        self,
        url: str,
        *,
        token: str | None = None,
        vault: str | None = None,
        org: str | None = None,
    ) -> None:
        self._url = url or SERVER_URL
        self._token = token or DEFAULT_TOKEN
        self._vault = vault
        self._org = org

        if not self._vault and DEFAULT_PROJECT_ID:
            self._vault = DEFAULT_PROJECT_ID.split('/')[1]
        if not self._org and DEFAULT_PROJECT_ID:
            self._org = DEFAULT_PROJECT_ID.split('/')[0]

        self._configure_logging()
        self._setup_client()
        self._session = CustomSession()
        if token:
            self._session = AuthenticatedSession(token)
        else:
            self._load_session_if_exists()

    def _setup_client(self) -> None:
        """Setup the GraphQL client."""
        transport = RequestsHTTPTransport(
            url=f'{self._url}{GRAPHQL_URL}',
            verify=True,
        )
        self._client = Client(transport=transport, fetch_schema_from_transport=True)

    def _configure_logging(self) -> None:
        """Configure logging for the application."""
        if not CONFIG_LOG_PATH.exists():
            CONFIG_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            CONFIG_LOG_PATH.touch()
        logging.basicConfig(
            filename=CONFIG_LOG_PATH,
            filemode='a',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.DEBUG,
        )

    def _load_session_if_exists(self) -> None:
        """Load session if the session file exists."""
        if CONFIG_SESSION_PATH.exists():
            self._load_session()

    def hello(self, name: str | None = None) -> None:
        click.echo(f"Hello, {name}!")

    def _save_session(self, file_path: Path = CONFIG_SESSION_PATH) -> None:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            pickle.dump(self._session, file)

    def _load_session(self, file_path: Path = CONFIG_SESSION_PATH) -> None:
        with file_path.open('rb') as file:
            self._session = pickle.load(file)

    def _remove_session(self, file_path: Path = CONFIG_SESSION_PATH) -> bool:
        file_path.unlink()
        return True

    def _list_local_files(self, directory: str) -> list[Path]:
        return [path for path in Path(directory).glob('**/*') if path.is_file()]

    def list_local_proofs(self, directory: str) -> list[dict[str, Any]]:
        list_local_files = [
            {
                'name': self._read_proof(path / 'proof.json').get('id'),
                'size': size(sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())),
                'last_update_date': self._read_proof(path / 'proof.json').get('last_update_date'),
            }
            for path in Path(directory).glob('**/*')
            if path.is_dir() and len(path.name.split(':')) == 2
        ]
        return list_local_files

    def _read_proof(self, proof_path: Path) -> dict[str, Any]:
        if not proof_path.exists():
            return {'id': None, 'last_update_date': None}

        with proof_path.open() as file:
            data = json.load(file)
            return {
                'id': data.get('id'),
                'last_update_date': datetime.fromtimestamp(os.path.getmtime(proof_path)).isoformat(),
            }

    def list_remote(self) -> Any:
        try:
            json_data = self._session.get(url=f'{self._url}{USER_URL}')
        except Exception:
            raise KaasCliException("List remote proofs failed") from None
        return json_data

    def _get_default_vault(self) -> str | None:
        try:
            json_data = self._session.get(url=f'{self._url}{USER_URL}')
        except Exception:
            raise KaasCliException("Get default vault failed") from None
        vault_hash = jmespath.search('vaults[0].hash', json_data)
        return vault_hash

    def _get_upload_urls(self, metadata: dict[str, Any], vault: str, org: str, tag: str | None) -> dict[str, Any]:
        data = self._session.post(
            url=f'{self._url}{ORG_VAULT_CACHE_URLS.format(org, vault)}',
            data=json.dumps(
                {
                    'files': metadata,
                    'tag': tag,
                }
            ),
            headers={
                'Content-Type': 'application/json',
            },
        )
        return data

    def _upload_presigned_url(self, files: dict[str, Any], tag: str | None, directory: str = '') -> dict[str, Any]:
        upload_results: Any = {}
        for file_name, url in files.items():
            file_path = Path(directory) / file_name
            with file_path.open('rb') as file:
                response = requests.put(url, data=file)

                # Check if the upload was successful
                if response.status_code in [200, 201]:  # Success status codes can vary, e.g., 200 OK or 201 Created
                    print(f"Successfully uploaded: {file_path}")
                    upload_results[file_name] = {'success': True, 'status_code': response.status_code}

                    # Create the cache record in database
                    self._session.post_return_no_content(
                        url=f'{self._url}{ORG_VAULT_CACHES_URL.format(self._org, self._vault)}',
                        data=json.dumps(
                            {
                                'fileName': file_name,
                                'tag': tag,
                            }
                        ),
                        headers={
                            'Content-Type': 'application/json',
                        },
                    )
                else:
                    print(f"Failed to upload {file_path.name} to {url}. Status code: {response.status_code}")
                    upload_results[file_name] = {
                        'success': False,
                        'status_code': response.status_code,
                        'error_message': response.text,
                    }

        # Trigger the sync-s3 endpoint to sync caches with the uploaded files on S3
        self._session.post_return_no_content(
            url=f'{self._url}{ORG_VAULT_CACHES_SYNC_S3_URL.format(self._org, self._vault)}'
        )

        return upload_results

    def archive_files(
        self, file_list: List[Path], archive_name: str, archive_format: str = 'zip', root_dir: Path | None = None
    ) -> str:
        """
        Archives a list of files into a single archive file while preserving the directory structure.

        Args: file_list (List[Path]): List of file paths to include in the archive. archive_name (str): The name of
        the output archive file without extension. archive_format (str): Format of the archive ('zip', 'tar',
        etc.). Default is 'zip'. root_dir (Path): The root directory to use for preserving the relative paths. If
        None, the common parent of all files will be used.

        Returns:
        str: The path to the created archive file.
        """
        if root_dir is None:
            # Find the common parent directory of all files
            common_paths: set[Path] = set(Path(file_list[0]).parents)
            for file_path in file_list[1:]:
                common_paths = set(common_paths) & set(Path(file_path).parents)
            root_dir = min(common_paths, key=lambda p: len(p.parts))

        # Ensure the archive name does not include an extension
        archive_path = Path(archive_name).with_suffix('')

        # Create a temporary directory to hold the files to be archived
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            for file_path in file_list:
                if file_path.is_file():
                    # Calculate relative path to the root_dir
                    relative_path = file_path.relative_to(root_dir)
                    # Create any necessary directories
                    (temp_dir_path / relative_path).parent.mkdir(parents=True, exist_ok=True)
                    # Copy file to the new location preserving the folder structure
                    shutil.copy(file_path, temp_dir_path / relative_path)

            # Create the archive from the temporary directory
            archive_final_path = shutil.make_archive(str(archive_path), archive_format, root_dir=temp_dir_path)

        # Move the archive to the desired directory and return the new path
        final_archive_path = Path(archive_final_path).with_suffix(f'.{archive_format}')
        shutil.move(archive_final_path, final_archive_path)

        return str(Path(archive_final_path))

    def get_archive_metadata(self, archive_path: str) -> dict[str, Any]:
        """
        Extracts metadata from an archive file.

        Args:
        archive_path (str): Path to the archive file.

        Returns:
        dict[str, Any]: Metadata extracted from the archive file.
        """
        # Initialize an empty dictionary for metadata
        metadata = {}

        # Create a Path object from the archive_path
        archive_file = Path(archive_path)

        # Check if the archive file exists
        if not archive_file.exists():
            raise FileNotFoundError(f"The archive file {archive_path} does not exist.")
        #             metadata[file_uuid] = {'filename': file_name_str, 'updated_at': updated_at}
        # Try to extract metadata from the archive file
        try:
            metadata[archive_file.name] = {
                'filename': archive_file.name,
                'updated_at': datetime.fromtimestamp(archive_file.stat().st_mtime).isoformat(),
            }
        except Exception as e:
            # Handle any exception that might occur during metadata extraction
            raise e

        return metadata

    def get_version_from_digest(self, file_list: Any) -> str:
        """
        Reads a JSON file named 'digest' from the provided file list, extracts hash values from specified fields,
        and returns them as a string.

        Args:
        file_list (list[Path]): List of file paths.

        Returns:
        str: A string containing the hash values from the 'digest' file.
        """
        # Find the 'digest' file in the file list
        digest_file = next((file for file in file_list if file.name == 'digest'), None)
        if digest_file is None:
            raise FileNotFoundError("No 'digest' file found in the provided file list.")

        # Read the 'digest' JSON file
        with open(digest_file, 'r') as file:
            data = json.load(file)

        # Extract the hash values from specified fields
        kompilation_hash = data.get('kompilation', 'Not found')
        foundry_hash = data.get('foundry', 'Not found')

        # Return the hash values as a string
        return f"{kompilation_hash}{foundry_hash}"

    def upload_files_s3(self, directory: str, tag: str | None = None) -> str | None:
        file_list = self._list_local_files(directory)
        if not file_list or len(file_list) == 0:
            raise KaasCliException(f'No files to upload in dir: {directory}')

        # Check if there is `digest` file
        digest_file = next((file for file in file_list if file.name == 'digest'), None)
        if digest_file is None:
            raise KaasCliException(f"No 'digest' file found in dir: {directory}")

        # Check if there is proof
        proofs = self.list_local_proofs(directory)
        if not proofs:
            raise KaasCliException(f'No proofs to upload in dir: {directory}')

        archive_name = self.get_version_from_digest(file_list)
        archive_path = self.archive_files(file_list, archive_name, archive_format='zip', root_dir=Path(directory))
        metadata = self.get_archive_metadata(archive_path)

        if self._vault is None or self._org is None:
            raise KaasCliException("vault and org must be provided")
        urls = self._get_upload_urls(metadata=metadata, vault=self._vault, tag=tag, org=self._org)

        filenames: list[str] = []
        for value in metadata.values():
            filenames.append(value['filename'])

        try:
            click.echo(f"Uploading {metadata} to S3...")
            self._upload_presigned_url(urls, tag=tag)
            click.echo(UPLOAD_SUCCESS_MESSAGE)
        except Exception as e:
            raise KaasCliException(f"Failed to upload {archive_path} to S3: {e}") from None

        # remove the archive file after uploading
        os.remove(archive_path)

        return None

    def download_version_or_tag(
        self, org_name: str, vault_name: str, version_or_tag: str, target_directory: str
    ) -> Any:
        caches = self.list_caches(org_name, vault_name, version_or_tag)
        if not caches or len(caches) == 0:
            raise KaasCliException(f"No cache found for {org_name}/{vault_name}:{version_or_tag}")
        try:
            latest_cache = caches[0]
            url_to_download = latest_cache.url
            downloaded_file_path = self.replace_path(
                f"{org_name}/{vault_name}/{latest_cache.fileName}", target_directory
            )
            self.download_file(url_to_download, downloaded_file_path)
            self.process_archive(downloaded_file_path, target_directory)
        except Exception as e:
            raise KaasCliException(f"Download {org_name}/{vault_name}:{version_or_tag} failed: {str(e)}") from e

        return f'Version {version_or_tag} downloaded to {target_directory}'

    def download_latest_version(self, org_name: str, vault_name: str, target_directory: str) -> Any:
        caches = self.list_caches(org_name, vault_name)
        if not caches or len(caches) == 0:
            raise KaasCliException(f"No cache found for {org_name}/{vault_name}")
        try:
            latest_cache = caches[0]
            url_to_download = latest_cache.url
            downloaded_file_path = self.replace_path(
                f"{org_name}/{vault_name}/{latest_cache.fileName}", target_directory
            )
            self.download_file(url_to_download, downloaded_file_path)
            self.process_archive(downloaded_file_path, target_directory)
        except Exception as e:
            raise KaasCliException(f"Download failed: {e}") from None

        return f'Latest version of {latest_cache.lastModified} downloaded to {target_directory}'

    def process_archive(self, archive_path: str, extract_to: str) -> None:
        """
        Extracts files from an archive to a specified directory and then removes the archive.

        Args:
        archive_path (str): The path to the archive file.
        extract_to (str): The directory to extract the files to.
        """
        # Ensure the target directory exists
        os.makedirs(extract_to, exist_ok=True)

        # Extract the archive
        with ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        # Remove the archive file after extraction
        os.remove(archive_path)
        # Delete the folder that contains archive file if it is empty
        if not os.listdir(os.path.dirname(archive_path)):
            os.rmdir(os.path.dirname(archive_path))
        click.echo(f"Extracted archive to {extract_to}")

    @staticmethod
    def _get_upload_data(file_list: list[Path], directory: Path) -> tuple[File_Data, Metadata]:
        data: File_Data = {}
        metadata = {}

        for file_path in file_list:
            file_uuid = str(uuid4())
            file_name_str = Path(file_path).relative_to(directory).as_posix()
            with file_path.open('rb') as file_object:
                data[f'file_{file_uuid}'] = (file_name_str, file_object.read(), None)
            updated_at = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            # Ensure the file path is converted to a string
            metadata[file_uuid] = {'filename': file_name_str, 'updated_at': updated_at}

        data['metadata'] = (None, json.dumps(metadata), 'application/json')

        return data, metadata

    @staticmethod
    def _get_metadata(file_list: list[Path], directory: Path) -> Metadata:
        data, metadata = KaasClient._get_upload_data(file_list, Path(directory))
        return metadata

    def login(self) -> DeviceAuth:
        try:
            data = self._session.post(url=f'{self._url}{DEVICE_LOGIN_URL}')
        except Exception:
            raise KaasCliException("Login failed") from None
        return DeviceAuth(**data)

    def confirm_login(self, device_code: str) -> Confirmation:
        try:
            data = self._session.get(url=f'{self._url}{DEVICE_LOGIN_URL}', params={'device_code': device_code})
        except Exception:
            raise KaasCliException("Login failed") from None
        self._session = AuthenticatedSession(data['token'])
        self._save_session()
        return Confirmation(True)

    def check(self) -> Confirmation:
        data = self._session.get(url=f'{self._url}{USER_URL}')
        if data:
            return Confirmation(True)
        else:
            return Confirmation(False)

    def _get_download_url(self, vault_hash: str, tag: str | None = None) -> dict:
        query = f"?tag={tag}" if tag else ""
        org_name, vault_name = vault_hash.split('/')
        data = self._session.get(url=f'{self._url}{ORG_VAULT_CACHE_URLS.format(org_name, vault_name)}{query}')
        return data

    def download_file(self, url: str, folder_path: str) -> None:
        file_path = Path(folder_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        is_run_by_ci = (
            os.getenv('CI', False)
            or os.getenv('GITHUB_ACTIONS', False)
            or os.getenv('GITLAB_CI', False)
            or os.getenv('CIRCLECI', False)
            or os.getenv('JENKINS_URL', False)
        )
        with open(file_path, 'wb') as file:
            print(f"Downloading {file_path}")
            with requests.get(url, stream=True) as response:
                # Check if the request was successful
                response.raise_for_status()

                total_length_str = response.headers.get('content-length')
                if total_length_str is None:
                    # Write the content of the response to the file in chunks
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                else:
                    dl = 0
                    total_length = int(total_length_str)
                    for data in response.iter_content(chunk_size=8192):
                        dl += len(data)
                        file.write(data)
                        done = int(50 * dl / total_length)
                        if not is_run_by_ci:
                            sys.stdout.write("\r[%s%s] %s%%" % ('=' * done, ' ' * (50 - done), done * 2))
                            sys.stdout.flush()
                    print("\n")

    def replace_path(self, input_string: str, target_directory: str) -> str:

        # Find the index of the first dash '/'
        dash_index = input_string.find('/')

        # Replace everything up to the first dash with 'test'
        result = target_directory + input_string[dash_index:]

        return result

    def read_new_files(self, files: list[str], target_directory: str) -> list[str]:
        new_files = []
        for file_name in files:
            file_path = Path(target_directory, file_name)
            if not file_path.exists():
                new_files.append(file_name)
        return new_files

    def list_orgs(self) -> list[str]:
        try:
            data = self._session.get(url=f'{self._url}{ORGANIZATIONS_URL}')
        except Exception as e:
            sys.exit(f"List orgs failed: {e}")
            raise KaasCliException("List orgs failed") from None
        return data

    def list_vaults(self) -> list[str]:
        try:
            data = self._session.get(url=f'{self._url}{VAULTS_ROOT_URL}')
        except Exception as e:
            sys.exit(f"List vaults failed: {e}")
            raise KaasCliException("List vaults failed") from None
        return data

    def list_caches(self, org_name: str, vault_name: str, search: str | None = None) -> list[Cache]:
        query = f"?search={search}" if search else ""
        try:
            data = self._session.get(url=f'{self._url}{ORG_VAULT_CACHES_URL.format(org_name, vault_name)}{query}')
            caches = [from_dict(Cache, cache) for cache in data]
            return caches
        except Exception as e:
            raise KaasCliException(f"List caches failed: {e}") from None

    def logout(self) -> bool:
        """
        Log out the user by clearing the session and authentication token.
        Returns True if the logout was successful, False otherwise.
        """
        try:
            return self._remove_session()
        except Exception as e:
            logging.error(f"Logout failed: {e}")
            return False

    def run_kontrol(
        self,
        org_name: str,
        vault_name: str,
        branch: str,
        out_folder: str,
        extra_build_args: str,
        extra_prove_args: str,
        kontrol_version: str,
    ) -> Job:
        try:
            data = self._session.post(
                url=f'{self._url}{KONTROL_JOB_URL.format(org_name, vault_name)}',
                json={
                    'branch': branch,
                    'outFolder': out_folder,
                    'kaas_extra_build_args': f"{extra_build_args}" if extra_build_args else " ",
                    'kaas_extra_prove_args': f"{extra_prove_args}" if extra_prove_args else " ",
                    "kontrol_version": kontrol_version,
                },
            )
            job = from_dict(Job, data)
            return job
        except Exception as e:
            raise KaasCliException(f"Run kontrol failed: {e}") from None

    @property
    def url(self) -> str:
        return self._url

    @property
    def get(self) -> Callable:
        return self._session.get


QUERY_HELLO: Final = gql(
    """
    query Hello($name: String!) {
        hello(name: $name)
    }
    """
)
