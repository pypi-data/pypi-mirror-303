import os.path
import re
from jinja2 import Environment, FileSystemLoader, Template

from edgeimpulse_ota.serve import serve
from edgeimpulse_ota.InputLibrary import InputLibrary
from edgeimpulse_ota.TensorData import TensorData
from edgeimpulse_ota.Quantization import Quantization


def get_template(template_name: str) -> Template:
    """
    Get jinja template
    :param template_name:
    :return:
    """
    return Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))).get_template(template_name)


def patch_header(contents: str, *args) -> str:
    """
    Add OTA functions prototypes to header
    :param contents:
    :return:
    """
    return contents.replace("#endif", get_template("ota.h.jinja").render())


def patch_cpp(contents: str, library: InputLibrary) -> str:
    """
    Implement OTA update logic
    :param contents:
    :param library:
    :return:
    """
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))
    template = env.get_template("ota.cpp.jinja")

    tensor_data = TensorData(contents)
    quantization = Quantization(contents)

    # remove const from tensors' data and quantization
    contents = re.sub(r"const TfArray<(\d+), (float|int)> quant", "TfArray<\g<1>, \g<2>> quant", contents)
    contents = contents.replace("const ALIGN", "ALIGN")
    original_weights, original_weights_size = serve(library=library)

    return template.render(
        contents=contents,
        tensor_data=tensor_data,
        quantization=quantization,
        patch_size=tensor_data.byte_size + quantization.bytes_size,
        original_weights=original_weights,
        original_weights_size=original_weights_size,
        as_array=lambda arr, fmt="%d": ", ".join(fmt % x for x in arr)
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
        # "tflite-model/tflite_learn_*.h": patch_header
    })

    return library.bytes
