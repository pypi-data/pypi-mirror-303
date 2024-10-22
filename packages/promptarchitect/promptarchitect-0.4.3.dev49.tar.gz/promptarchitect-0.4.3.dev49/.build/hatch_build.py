import json
import os
from pathlib import Path

from hatchling.metadata.plugin.interface import MetadataHookInterface


class JSONMetaDataHook(MetadataHookInterface):
    def update(self, metadata):
        dev_build = os.getenv("DEV_BUILD", "0") == "1"
        run_number = os.getenv("GITHUB_RUN_NUMBER", "0")

        version_file_path = Path(__file__).parent / "version.json"

        with version_file_path.open() as f:
            version_metadata = json.load(f)

        version_number = version_metadata["version"]

        if dev_build:
            version_number = f"{version_number}.dev{run_number}"

        metadata["version"] = version_number
