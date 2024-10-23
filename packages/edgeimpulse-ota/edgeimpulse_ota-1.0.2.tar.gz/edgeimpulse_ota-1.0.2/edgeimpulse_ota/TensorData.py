import re
from collections import namedtuple
from struct import pack
from typing import Generator, Iterable


Tensor = namedtuple("Tensor", "index, size, bits, align, data")


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

        tensors = re.findall(r'ALIGN\((\d+)\) int(32|8)_t tensor_data(\d+)\[([0-9*]+)] = \{([\s\S]+?)};', contents)
        assert len(tensors) > 0, "Can't find tensor data"
        self.tensors = [Tensor(index=int(index), bits=int(bits), size=eval(size), data=eval_data(data), align=int(align)) for align, bits, index, size, data in tensors]
        # self.tensors = [(int(index), int(bits), eval(size), eval_data(data)) for bits, index, size, data in tensors]

    @property
    def byte_size(self) -> int:
        return len(self.bytes)

    @property
    def iterator(self) -> Iterable:
        return self.tensors

    @property
    def bytes(self) -> bytes:
        """
        Convert data to binary format
        :return:
        """
        packs = []

        for tensor in self.tensors:
            assert tensor.bits in [8, 32], f'unknown bit depth for tensor {tensor.index()}: {tensor.bits}'
            dtype = 'i' if tensor.bits == 32 else 'b'
            packs.append(pack(f">BBH{dtype * len(tensor.data)}", tensor.index, tensor.bits, tensor.size, *tensor.data))

        return b"".join(packs)

