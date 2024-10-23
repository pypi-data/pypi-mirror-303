import re
from struct import pack
from typing import Generator


class TensorData:
    """
    Match tensor data structure in Edge Impulse model.
    Patch format is (for each tensor):
        index: 1 byte
        bits: 1 byte (either 8 or 32)
        size: 2 bytes
        data: size * (bits // 8) bytes
    """
    def __init__(self, contents: str):
        """

        :param contents:
        """
        def eval_data(data: str) -> list:
            return [int(x) for x in eval("[" + re.sub(r'/\*.+?\*/', "", data) + "]")]

        tensors = re.findall(r'int(32|8)_t tensor_data(\d+)\[([0-9*]+)] = \{([\s\S]+?)};', contents)
        assert len(tensors) > 0, "Can't find tensor data"
        self.tensors = [(int(index), int(bits), eval(size), eval_data(data)) for bits, index, size, data in tensors]

    @property
    def byte_size(self) -> int:
        return len(self.bytes)

    @property
    def bytes(self) -> bytes:
        """
        Convert data to binary format
        :return:
        """
        packs = []

        for index, bits, size, data in self.tensors:
            assert bits in [8, 32], f'unknown bit depth for tensor {index}: {bits}'
            dtype = 'i' if bits == 32 else 'b'
            packs.append(pack(f">BBH{dtype * len(data)}", index, bits, size, *data))

        return b"".join(packs)

    @property
    def patches(self) -> Generator:
        """
        Generate code to patch tensor data
        :return:
        """
        for index, bits, size, data in self.tensors:
            yield f"""if (!ei_patch_tensor_data<int{bits}_t>(stream, {index}, {bits}, {size})) return false;"""
