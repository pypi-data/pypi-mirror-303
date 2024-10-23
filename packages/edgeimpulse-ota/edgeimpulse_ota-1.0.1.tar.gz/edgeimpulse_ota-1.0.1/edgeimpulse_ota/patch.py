import os.path
import re
from jinja2 import Environment, FileSystemLoader

from edgeimpulse_ota.InputLibrary import InputLibrary
from edgeimpulse_ota.TensorData import TensorData
from edgeimpulse_ota.Quantization import Quantization


def patch_header(contents: str) -> str:
    """
    Add OTA functions prototypes to header
    :param contents:
    :return:
    """
    return contents.replace("#endif", "bool ei_ota(Stream& stream);\nbool ei_restore();\n\n#endif")


def patch_cpp(contents: str) -> str:
    """
    Implement OTA update logic
    :param contents:
    :return:
    """
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))
    template = env.get_template("ota.jinja")

    tensor_data = TensorData(contents)
    quantization = Quantization(contents)

    # remove const from tensors' data and quantization
    contents = re.sub(r"const TfArray<(\d+), (float|int)> quant", "TfArray<\g<1>, \g<2>> quant", contents)
    contents = contents.replace("const ALIGN", "ALIGN")

    return template.render(
        contents=contents,
        tensor_data=tensor_data,
        quantization=quantization,
        patch_size=tensor_data.byte_size + quantization.bytes_size
    )


def patch(zip: str | bytes = None, api_key: str = None, project_id: str = None, **kwargs):
    """
    Apply patch to library
    :param zip: if str, it is interpreted as a path to a local file. If bytes, it is interpreted as the zip contents
    :param api_key: Edge Impulse API key
    :param project_id: Edge Impulse project ID
    :return:
    """
    library = InputLibrary(zip=zip, api_key=api_key, project_id=project_id, **kwargs)
    library.replace({
        "tflite-model/tflite_learn_*.cpp": patch_cpp,
        "tflite-model/tflite_learn_*.h": patch_header
    })

    return library.bytes
