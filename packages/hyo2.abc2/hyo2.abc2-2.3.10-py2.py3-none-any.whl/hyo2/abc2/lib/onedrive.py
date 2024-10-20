import requests
import os
import traceback
import logging

from hyo2.abc2.lib.progress.abstract_progress import AbstractProgress
from hyo2.abc2.lib.progress.cli_progress import CliProgress

logger = logging.getLogger(__name__)


class OneDrive:

    def __init__(self, show_progress: bool = False, debug_mode: bool = False, progress: AbstractProgress = None) \
            -> None:
        if debug_mode:
            self.debug_level = 2
        else:
            self.debug_level = 0
        self.show_progress = show_progress
        self.chunk_count = None
        self.filesize = None
        self.file_count = None
        self.file_nr = None
        if progress is None:
            self.progress = CliProgress()
        else:
            self.progress = progress

    def get_file(self, file_src: str, file_dst: str, unzip_it: bool = False) -> None:

        file_dst = os.path.abspath(file_dst)
        if os.path.exists(file_dst):
            os.remove(file_dst)

        response = requests.get(file_src, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        logger.debug("size in bytes: %d" % total_size_in_bytes)
        block_size = 1024 * 1024
        blocks = total_size_in_bytes / block_size + 2.0
        quantum = 100.0 / blocks
        if self.show_progress:
            self.progress.start(text="Downloading", has_abortion=True)

        with open(file_dst, 'wb') as file:
            for data in response.iter_content(chunk_size=block_size):
                if self.show_progress:
                    if self.progress.canceled:
                        raise RuntimeError("download stopped by user")
                    self.progress.add(quantum=quantum)
                file.write(data)

        if self.show_progress:
            self.progress.end()

        if unzip_it:
            import zipfile

            try:
                z = zipfile.ZipFile(file_dst, "r")

                unzip_path = os.path.dirname(file_dst)

                logger.debug("unzipping %s to %s" % (file_dst, unzip_path))

                name_list = z.namelist()
                self.file_nr = len(name_list)
                if self.show_progress:
                    self.progress.start(text="Unzipping", has_abortion=True)

                self.file_count = 0
                for item in name_list:
                    # print(item)
                    z.extract(item, unzip_path)
                    self.file_count += 1
                    if self.show_progress:
                        if self.progress.canceled:
                            raise RuntimeError("unzip stopped by user")
                        pct = int((self.file_count / self.file_nr) * 100.0)
                        self.progress.update(pct)
                z.close()
                os.remove(file_dst)
                if self.show_progress:
                    self.progress.end()

            except Exception as e:
                traceback.print_exc()
                raise RuntimeError("unable to unzip the downloaded file: %s -> %s" % (file_dst, e))
