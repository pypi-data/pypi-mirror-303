import os
from collections.abc import Callable
import asyncio
import logging
from pathlib import Path
import aiofiles
from ..exceptions import (
    FileError,
    ConfigError
)
from .UploadTo import UploadToBase
from ..interfaces.Sharepoint import Sharepoint


class UploadToSharepoint(UploadToBase, Sharepoint):
    """
    UploadToSharepoint.

    Upload a file (or collection of files) to a Sharepoint Site.
    """
    # dict of expected credentials
    _credentials: dict = {
        "username": str,
        "password": str,
        "tenant": str,
        "site": str
    }

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop = None,
        job: Callable = None,
        stat: Callable = None,
        **kwargs,
    ):
        self.mdate = None
        self.local_name = None
        self.filename: str = ""
        self.whole_dir: bool = False
        self.preserve = True
        self.ContentType: str = "binary/octet-stream"
        self.recursive: bool = kwargs.get('recursive', False)
        UploadToBase.__init__(
            self, loop=loop,
            job=job,
            stat=stat,
            **kwargs
        )
        params = self._params.copy()
        Sharepoint.__init__(self, **params)

    async def start(self, **kwargs):
        """start Method."""
        await super(UploadToSharepoint, self).start(**kwargs)
        if hasattr(self, "source"):
            self.source_dir = self.source.get('directory')
            if isinstance(self.source_dir, str):
                self.source_dir = Path(self.source_dir).resolve()
            self.filename = self.source.get("filename", None)
            self.whole_dir = (
                self.source["whole_dir"] if "whole_dir" in self.source else False
            )
            if self.whole_dir is True:
                # if whole dir, is all files in source directory
                logging.debug(
                    f"Uploading all files on directory {self.source_dir}"
                )
                p = self.source_dir.glob("**/*")
                self._filenames = [
                    x for x in p if x.is_file()
                ]
            else:
                if "filename" in self.source:
                    filename = self.mask_replacement(self.source["filename"])
                    p = self.source_dir.glob(filename)
                    self._filenames = [
                        x for x in p if x.is_file()
                    ]
                elif 'extension' in self.source:
                    extension = self.source["extension"]
                    pattern = self.source.get("pattern", None)
                    if pattern:
                        # TODO: fix recursive problem from Glob
                        if self.recursive is True:
                            p = self.source_dir.rglob(f"**/*{pattern}*{extension}")
                        else:
                            p = self.source_dir.glob(f"*{pattern}*{extension}")
                    else:
                        if self.recursive is True:
                            p = self.source_dir.rglob(f"**/*{extension}")
                        else:
                            p = self.source_dir.glob(f"*{pattern}*{extension}")
                    self._filenames = [
                        x for x in p if x.is_file()
                    ]
                else:
                    raise ConfigError(
                        "UploadToSharepoint: No filename or extension in source"
                    )
        if hasattr(self, "destination"):
            # Destination in Sharepoint:
            self.directory = self.destination["directory"]
            if not self.directory.endswith("/"):
                self.directory = self.source_dir + "/"
            self.directory = self.mask_replacement(self.destination["directory"])
        else:
            if self.previous and self.input:
                self._filenames = self.input
            if hasattr(self, "file"):
                filenames = []
                for f in self._filenames:
                    p = self.source_dir.glob(f)
                    fp = [x for x in p if x.is_file()]
                    filenames = filenames + fp
                self._filenames = filenames
            elif 'extension' in self.source:
                extension = self.source["extension"]
                pattern = self.source.get("pattern", None)
                # check if files in self._filenames ends with extension
                filenames = []
                for f in self._filenames:
                    if f.suffix == extension:
                        # check if pattern is in the filename
                        if pattern:
                            if pattern in f.name:
                                filenames.append(f)
                            continue
                        else:
                            filenames.append(f)
                self._filenames = filenames
        return self

    async def close(self):
        pass

    async def run(self):
        """Upload a File to Sharepoint"""
        self._result = None
        async with self.connection():
            if not self.context:
                self.context = self.get_context(self.url)
        if not self._filenames:
            raise FileError("No files to upload")
        if self.whole_dir is True:
            # Using Upload entire Folder:
            self._result = await self.upload_folder(
                local_folder=self.source_dir
            )
        else:
            self._result = await self.upload_files(
                filenames=self._filenames
            )
        self.add_metric("SHAREPOINT_UPLOADED", self._result)
        return self._result
