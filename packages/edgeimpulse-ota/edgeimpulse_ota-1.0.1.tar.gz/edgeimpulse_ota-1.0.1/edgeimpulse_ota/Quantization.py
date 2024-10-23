import re
from struct import pack
from typing import Generator


class Quantization:
    """
    Match quantization data in Edge Impulse model.
    Patch format is (for each layer):
        index: 1 byte
        size: 2 bytes
        data: size * 8 bytes
            scale: 4 bytes (float)
            zero point: 4 bytes (int)
    """
    def __init__(self, contents: str):
        def eval_data(data: str, dtype) -> list:
            return [dtype(x) for x in eval("[" + re.sub(r'/\*.+?\*/', "", data) + "]")]

        scales = re.findall(r'TfArray<(\d+), float> quant(\d+)_scale = \{ \d+, \{([\s\S]+?)}', contents)
        zeros = re.findall(r'TfArray<(\d+), int> quant(\d+)_zero = \{ \d+, \{([\s\S]+?)}', contents)
        assert len(scales) > 0, "Can't find quantization data"

        self.scales = [(int(index), eval(size), eval_data(data, float)) for size, index, data in scales]
        self.zeros = [eval_data(data, int) for size, index, data in zeros]

        assert len(self.scales) == len(self.zeros), f"quantization data size mismatch ({len(self.scales)} scales vs {len(self.zeros)} zeros)"

    @property
    def bytes_size(self) -> int:
        return len(self.bytes)

    @property
    def bytes(self):
        """
        Convert data to binary format
        :return:
        """
        packs = []

        for (index, size, scale), zero in zip(self.scales, self.zeros):
            data = [x for pair in zip(scale, zero) for x in pair]
            packs.append(pack(f">BH{'fi' * len(scale)}", index, size, *data))

        return b"".join(packs)

    @property
    def patches(self) -> Generator:
        """
        Generate code to patch quantization data.
        :return:
        """
        for index, size, _ in self.scales:
            yield f"""if (!ei_patch_tensor_quantization(stream, {index}, {size})) return false;"""
