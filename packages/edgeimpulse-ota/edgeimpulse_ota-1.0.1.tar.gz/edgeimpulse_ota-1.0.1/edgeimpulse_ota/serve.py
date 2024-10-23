import struct
import zipfile
from io import BytesIO

from edgeimpulse_ota.InputLibrary import InputLibrary
from edgeimpulse_ota.TensorData import TensorData
from edgeimpulse_ota.Quantization import Quantization


def serve(zip: str | bytes = None, api_key: str = None, project_id: str = None, **kwargs):
    """
    Convert model's weights to OTA patch
    :param zip: if str, it is interpreted as a path to a local file. If bytes, it is interpreted as the zip contents
    :param api_key: Edge Impulse API key
    :param project_id: Edge Impulse project ID
    :return:
    """
    library = InputLibrary(zip=zip, api_key=api_key, project_id=project_id, **kwargs)

    with zipfile.ZipFile(BytesIO(library.bytes), "r") as zip:
        for info in zip.infolist():
            filename = info.filename

            if "/tflite-model/tflite_learn_" in filename and filename.endswith(".cpp"):
                with zip.open(filename) as file:
                    contents = file.read().decode("utf-8")
                    tensor_data = TensorData(contents)
                    quantization = Quantization(contents)
                    patch_size = tensor_data.byte_size + quantization.bytes_size

                    return struct.pack('>I', patch_size) + tensor_data.bytes + quantization.bytes, 4 + patch_size

    return None
