import re
import requests
from io import BytesIO
from typing import Union
from zipfile import ZipFile, ZIP_DEFLATED


class InputLibrary:
    """
    Read an Edge Impulse library from many sources:
     - raw zip bytes
     - local file
     - API
    """
    def __init__(self, zip: str | bytes = None, api_key: str = None, project_id: str = None, model_type: str = "int8", engine: str = "tflite-eon"):
        """
        Constructor
        :param zip: if str, it is interpreted as a path to a local file. If bytes, it is interpreted as the zip contents
        :param api_key: Edge Impulse API key
        :param project_id: Edge Impulse project ID
        :param model_type: int8 | float32
        :param engine: tflite | tflite-eon | tflite-eon-ram-optimized
        """
        self.bytes = None

        if isinstance(zip, str):
            self.bytes = self.from_local(zip)
        elif isinstance(zip, bytes):
            self.bytes = zip
        else:
            assert len(api_key) >= 50 and len(project_id) >= 6, "Missing either zip source or api_key/project_id"
            assert model_type in ["int8", "float32"], f"Unknown model type {model_type}"
            assert engine in ["tflite", "tflite-eon", "tflite-eon-ram-optimized"], f"Unknown engine {engine}"
            self.bytes = self.fetch(api_key, project_id, engine=engine, model_type=model_type)

    def from_local(self, path: str) -> bytes:
        """
        Read local zip file
        :param path:
        :return:
        """
        with open(path, "rb") as f:
            return f.read()

    def fetch(self, api_key: str, project_id: str, model_type: str, engine: str):
        """
        Fetch library from API
        :param api_key:
        :param project_id:
        :param model_type: #todo not used for now
        :param engine:
        :return:
        """
        content = b""
        url = f"https://studio.edgeimpulse.com/v1/api/{project_id}/deployment/download?type=arduino&engine={engine}"
        res = requests.get(url, headers={"X-Api-Key": api_key}, stream=True)
        assert res.status_code == 200, f"Bad response: {res.text}"

        # assert model is not larger than 10 MB
        for chunk in res.iter_content(chunk_size=1024 * 1024):
            content += chunk
            assert len(content) < 10 * 1024 * 1024, f"Model is too large: >10 MB"

        return content

    def replace(self, replacements: dict[str, Union[str, callable]]):
        """
        Replace contents of files
        :param replacements: {file pattern: replacement function}
        :return:
        """
        dest_io = BytesIO()

        def matches(filename: str, pattern: str) -> bool:
            """
            Check if filename matches glob-like pattern
            :param filename:
            :param pattern:
            :return:
            """
            return re.search(pattern.replace("*", ".*"), filename) is not None

        with ZipFile(BytesIO(self.bytes), "r") as zip:
            with ZipFile(dest_io, "w", ZIP_DEFLATED) as dest:
                for info in zip.infolist():
                    filename = info.filename
                    contents = zip.read(filename)

                    for pattern, replacement_function in replacements.items():
                        if matches(filename, pattern):
                            contents = replacement_function(contents.decode(), self)
                            break

                    dest.writestr(info, contents)

        self.bytes = dest_io.getvalue()
