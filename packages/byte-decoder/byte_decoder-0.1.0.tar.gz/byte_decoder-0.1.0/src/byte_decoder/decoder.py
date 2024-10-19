import struct


class ByteDecoder:
    def __init__(self):
        pass

    def decode_to_int(self, byte_data: bytes) -> int:
        return int.from_bytes(byte_data, byteorder="big")

    def decode_to_string(self, byte_data: bytes, encoding: str = "utf-8") -> str:
        return byte_data.decode(encoding)

    def decode_to_float(self, byte_data: bytes) -> float:
        return struct.unpack(">f", byte_data)[0]

    def decode_to_list(self, byte_data: bytes, item_size: int) -> list:
        return list(
            byte_data[i : i + item_size] for i in range(0, len(byte_data), item_size)
        )
