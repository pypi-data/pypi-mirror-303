from pathlib import Path
import logging

from icsystemutils.network.remote import RemoteHost

logger = logging.getLogger(__name__)


class Model:
    """
    A basic 'model' abstraction. Models can be referenced via a name and
    location, which can be remote.
    """

    def __init__(
        self, name: str, host_name: str, location: Path, archive_name: str = ""
    ) -> None:
        self.name = name
        self.host = RemoteHost(host_name)
        self.archive_name = archive_name
        self.location = location

    def get_archive_path(self):
        return self.location / Path(self.name) / Path(self.archive_name)

    def upload(self, local_location):
        self.host.upload(local_location, self.get_archive_path())

    def download(self, local_location):
        self.host.download(self.get_archive_path(), local_location)
