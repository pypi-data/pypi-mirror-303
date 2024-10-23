import os
from typing import List, Optional
from collections.abc import Callable
from pathlib import Path, PurePath
import pandas as pd
from io import BytesIO
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from ..exceptions import FileError, FileNotFound
from .O365Client import O365Client
from ..conf import (
    SHAREPOINT_APP_ID,
    SHAREPOINT_APP_SECRET,
    SHAREPOINT_TENANT_ID,
    SHAREPOINT_TENANT_NAME
)

class Sharepoint(O365Client):
    """
    Sharepoint Client.

    Managing connections to MS Sharepoint Resources.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Default credentials
        self._default_tenant_id = SHAREPOINT_TENANT_ID
        self._default_client_id = SHAREPOINT_APP_ID
        self._default_client_secret = SHAREPOINT_APP_SECRET
        self._default_tenant_name = SHAREPOINT_TENANT_NAME

    def get_context(self, url: str, *args) -> Callable:
        return ClientContext(url, *args)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        return self

    def _start_(self, **kwargs):
        # processing URL:
        site = f"sites/{self.site}/" if self.site is not None else ""
        self.url = f"https://{self.tenant}.sharepoint.com/{site}"
        if hasattr(self, '_srcfiles'):
            for file in self._srcfiles:
                fd = file.get('directory')
                if 'sites' in fd:
                    file['directory'] = f"{fd}"
                else:
                    file["directory"] = f"/{site}{fd}"
        return True

    def download_excel_from_sharepoint(
        self,
        file_url: str,
        destination: Path = None,
        as_pandas: bool = False
    ):
        try:
            response = self.context.web.get_file_by_server_relative_url(file_url).download().execute_query()
            content = response.content
            if as_pandas:
                bytes_buffer = BytesIO(content)
                df = pd.read_excel(bytes_buffer)
                return df
            else:
                with open(destination, "wb") as local_file:
                    local_file.write(content)
                return str(destination)
        except Exception as err:
            self._logger.error(f"Error downloading Excel file {file_url}: {err}")
            raise FileError(f"Error downloading Excel file {file_url}: {err}") from err

    async def file_search(self) -> List:
        destinations = []
        try:
            # Get the default document library and its drive
            drive = self.context.web.get_default_document_library().drive

            for file in self._srcfiles:
                directory = file["directory"]
                fname = file["filename"]

                # Search for the file within the drive
                items = drive.root.search(f"name:{fname}")
                self.context.load(items)
                self.context.execute_query()

                # Filter results to ensure they are within the specified directory
                paths_matched = [
                    item.serverRelativeUrl for item in items
                    if fname in item.name and directory in item.serverRelativeUrl
                ]

                if len(paths_matched) == 0:
                    self._logger.error(
                        f"Error downloading File: Pattern not match {fname}"
                    )
                    raise FileError(
                        f"Error downloading File: Pattern not match {fname}"
                    )
                else:
                    for path in paths_matched:
                        file = path[path.rfind("/") + 1: len(path)]
                        destination = "{}/{}".format(self.directory, file)
                        try:
                            with open(destination, "wb") as local_file:
                                self.context.web.get_file_by_server_relative_url(
                                    path
                                ).download(local_file).execute_query()
                                destinations.append(destination)
                        except Exception as err:
                            raise RuntimeError(
                                f"Sharepoint: Error downloading file {path}: {err}"
                            ) from err
            return destinations

        except Exception as e:
            print(e)

    async def file_download(self) -> List:
        destinations = []
        for file in self._srcfiles:
            directory = file.get('directory', self.directory)
            fname = file.get('filename', self.filename)
            if self.filename is None:
                self.filename = fname
                destination = self.directory.joinpath(fname)
            else:
                destination = self.filename if self.filename else fname
            source = f"{directory}{fname}"
            try:
                self.context.web.get_file_by_server_relative_url(
                    source
                ).get().execute_query()
                with open(destination, "wb") as local_file:
                    self.context.web.get_file_by_server_relative_url(source).download(
                        local_file
                    ).execute_query()
                destinations.append(destination)
            except Exception as err:
                if 'Not Found for url' in str(err):
                    raise FileNotFound(
                        f"File {fname} not found: {err}"
                    )
                else:
                    self._logger.error(
                        f"Error downloading file {fname}: {err}"
                    )
                    raise FileError(
                        f"Error downloading file {fname}: {err}"
                    ) from err
        return destinations

    async def download_files(self, files: List[dict], destination_dir: str) -> List:
        """
        Download a list of files from SharePoint to a specified destination directory.

        Args:
            files (List[dict]): A list of dictionaries with 'directory' and 'filename' keys.
            destination_dir (str): The local directory where files will be downloaded.

        Returns:
            List: A list of paths to the downloaded files.
        """
        destination_dir = Path(destination_dir).resolve()
        if not destination_dir.exists():
            destination_dir.mkdir(parents=True, exist_ok=True)

        destinations = []

        for file in files:
            directory = file.get('directory')
            fname = file.get('filename')

            if not directory or not fname:
                raise ValueError(
                    "Each file entry must have both 'directory' and 'filename'."
                )

            # Build the SharePoint source path (directory + filename)
            # Ensure forward slashes for SharePoint URLs
            source = f"{directory}/{fname}".replace("\\", "/")

            # Determine the destination file path
            destination = destination_dir.joinpath(fname)

            try:
                # Fetch the file from SharePoint
                self.context.web.get_file_by_server_relative_url(source).get().execute_query()

                # Download the file to the local destination
                with open(destination, "wb") as local_file:
                    self.context.web.get_file_by_server_relative_url(source).download(local_file).execute_query()

                # Append the local destination path to the results
                destinations.append(destination)
            except Exception as err:
                if 'Not Found for url' in str(err):
                    raise FileNotFound(
                        f"File {fname} not found: {err}"
                    )
                else:
                    self._logger.error(
                        f"Error downloading file {fname}: {err}"
                    )
                    raise FileError(
                        f"Error downloading file {fname}: {err}"
                    ) from err

        return destinations

    async def upload_files(self, filenames: Optional[list] = None):
        """Upload files to a SharePoint folder using a resumable upload session for large files."""
        files = []
        if not filenames:
            filenames = self._srcfiles
        for file in filenames:
            # Destination folder in SharePoint
            destination = self.directory
            try:
                file_size = os.path.getsize(str(file))
                target_folder_url = f"{destination}"
                file_name = file.name
                target_folder = self.context.web.get_folder_by_server_relative_url(
                    target_folder_url
                )
                # Ensure the target folder exists
                self.context.load(target_folder)
                self.context.execute_query()
                if file_size <= 4 * 1024 * 1024:  # 4 MB threshold
                    # Small file, upload directly
                    with open(str(file), "rb") as content_file:
                        file_content = content_file.read()
                    target_file = target_folder.upload_file(
                        file_name,
                        file_content
                    ).execute_query()
                else:
                    # Large file, use resumable upload
                    uploaded_file = target_folder.files.upload_large_file(
                        source_path=str(file),
                        chunk_size=5 * 1024 * 1024  # 5 MB chunks
                    ).execute_query()
                    target_file = uploaded_file  # For consistency
                files.append(
                    {"filename": target_file.serverRelativeUrl}
                )  # Return the URL of the uploaded file
            except Exception as err:
                self._logger.error(
                    f"Error uploading file {file}: {err}"
                )
                raise FileError(
                    f"Error uploading file {file}: {err}"
                ) from err
        return files

    async def upload_folder(self, local_folder: PurePath):
        destinations = []
        # destination:
        destination = self._destination
        try:
            for p in local_folder.glob('**/*'):
                # Check if it's a file or directory
                if p.is_dir():
                    # Create corresponding folder in SharePoint if it doesn't exist
                    folder_path = self._get_sharepoint_folder_path(
                        p, local_folder, destination
                    )
                    await self._create_sharepoint_folder(folder_path)
                elif p.is_file():
                    # Upload file to SharePoint
                    sharepoint_folder = self._get_sharepoint_folder_path(
                        p.parent, local_folder, destination
                    )
                    file_url = await self.upload_file(p, sharepoint_folder)
                    destinations.append(file_url)
            return destinations  # Return list of uploaded file URLs

        except Exception as err:
            self._logger.error(f"Error uploading folder {local_folder}: {err}")
            raise FileError(f"Error uploading folder {local_folder}: {err}") from err

    # Helper method to create folder paths in SharePoint
    def _get_sharepoint_folder_path(
        self,
        path: PurePath,
        local_folder: PurePath,
        destination: str
    ) -> str:
        """Get the corresponding SharePoint folder path for a local file or folder."""
        # Strip the local folder prefix and combine with SharePoint destination folder
        relative_path = path.relative_to(local_folder)
        sharepoint_folder_path = f"{destination}/{relative_path}".replace("\\", "/")  # Convert to forward slashes
        return sharepoint_folder_path

    # Helper method to create a folder in SharePoint
    async def _create_sharepoint_folder(
        self,
        folder_url: str
    ):
        """Create a folder in SharePoint if it doesn't exist."""
        try:
            folder = self.context.web.get_folder_by_server_relative_url(folder_url)
            folder.execute_query()  # Check if folder exists
        except Exception:
            # Folder does not exist, so create it
            parent_folder_url = "/".join(folder_url.split("/")[:-1])  # Parent folder path
            parent_folder = self.context.web.get_folder_by_server_relative_url(parent_folder_url)
            parent_folder.folders.add(folder_url.split("/")[-1]).execute_query()
            self._logger.info(f"Created folder: {folder_url}")
