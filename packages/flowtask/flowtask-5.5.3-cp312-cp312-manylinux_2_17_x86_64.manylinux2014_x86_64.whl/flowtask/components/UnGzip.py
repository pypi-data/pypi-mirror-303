import os
import logging
import asyncio
from typing import List
from collections.abc import Callable
from pathlib import PosixPath, Path, PurePath
import tarfile
from ..exceptions import FileError, ComponentError, FileNotFound
from .abstract import FlowComponent
from ..interfaces.compress import CompressSupport


class UnGzip(FlowComponent, CompressSupport):
    """
    UnGzip

    Overview:
        Uncompress a Gzip (.gz) file, including compressed tarballs (e.g., .tar.gz, .tar.bz2, .tar.xz).
        This component uncompresses the given gzip file or tarball into the specified directory.

    Properties:
    - filename: The gzip file to uncompress.
    - directory: The output directory where the files will be extracted.
    - delete_source: Whether to delete the source file after extraction.

    """

    _namelist = []
    _directory = ""

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop = None,
        job: Callable = None,
        stat: Callable = None,
        **kwargs,
    ):
        """Init Method."""
        self.filename: str = None
        self.directory: PurePath = None
        self._path: PurePath = None
        self._output: PurePath = None
        self._filenames: List = []
        self.delete_source: bool = False
        super(UnGzip, self).__init__(loop=loop, job=job, stat=stat, **kwargs)

    async def start(self, **kwargs):
        # Handle the directory and file path setup
        if isinstance(self.directory, str):
            self.directory = PosixPath(self.directory).resolve()
            self._path = PosixPath(self.directory, self.filename)

        if self.filename is not None:
            if hasattr(self, "masks"):
                self.filename = self.mask_replacement(self.filename)
            self._path = PosixPath(self.directory, self.filename)
        elif self.previous:
            if isinstance(self.input, PosixPath):
                self.filename = self.input
            elif isinstance(self.input, list):
                self.filename = PosixPath(self.input[0])
            elif isinstance(self.input, str):
                self.filename = PosixPath(self.input)
            else:
                filenames = list(self.input.keys())
                if filenames:
                    try:
                        self.filename = PosixPath(filenames[0])
                    except IndexError as err:
                        raise FileError("File is empty or doesn't exist") from err
            self._variables["__FILEPATH__"] = self.filename
            self._variables["__FILENAME__"] = os.path.basename(self.filename)
            self._path = self.filename
        else:
            raise FileError("UnGzip: File is empty or doesn't exist")

        # Handle extraction settings
        if hasattr(self, "extract"):
            for _, filename in enumerate(self.extract["filenames"]):
                filename = self.mask_replacement(filename)
                self._filenames.append(filename)
            if "directory" in self.extract:
                self._output = Path(self.extract["directory"]).resolve()
                # Create directory if not exists
                try:
                    self._output.mkdir(parents=True, exist_ok=True)
                except Exception as err:
                    logging.error(f"Error creating directory {self._output}: {err}")
                    raise ComponentError(
                        f"Error creating directory {self._output}: {err}"
                    ) from err
            else:
                # same directory:
                self._output = Path(self.directory)

        self.add_metric("OUTPUT_DIRECTORY", self._output)
        self.add_metric("GZIP_FILE", self.filename)
        return True

    async def close(self):
        pass

    async def run(self):
        # Check if file exists
        self._result = None
        if not self._path.exists() or not self._path.is_file():
            raise FileNotFound(
                f"Compressed File doesn't exist: {self._path}"
            )

        # Uncompress the gzip/tar.gz file
        try:
            files = await self.uncompress_gzip(
                source=self._path,
                destination=self._output,
                remove_source=self.delete_source,
            )
        except (FileNotFoundError, ComponentError) as err:
            raise FileError(f"UnGzip failed: {err}")

        if self.delete_source:
            self._path.unlink(missing_ok=True)

        filenames = []
        for filename in files:
            f = self._output.joinpath(filename)
            filenames.append(f)
        self._result = filenames

        return self._result
