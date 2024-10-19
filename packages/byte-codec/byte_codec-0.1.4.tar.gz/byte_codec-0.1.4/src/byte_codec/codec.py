import struct


class ByteCodec:
    def __init__(self):
        pass

    def decode_to_int(self, byte_data: bytes) -> int:
        return int.from_bytes(byte_data, byteorder="big")  # expected int

    def decode_to_string(self, byte_data: bytes, encoding: str = "utf-8") -> str:
        return byte_data.decode(encoding)

    def decode_to_float(self, byte_data: bytes) -> float:
        return struct.unpack(">f", byte_data)[0]

    def decode_to_list(self, byte_data: bytes, item_size: int) -> list:
        return list(
            byte_data[i : i + item_size] for i in range(0, len(byte_data), item_size)
        )

    def encode_from_int(self, value: int, byte_length: int = 4) -> bytes:
        return value.to_bytes(byte_length, byteorder="big")

    def encode_from_string(self, value: str, encoding: str = "utf-8") -> bytes:
        return value.encode(encoding)

    def encode_from_float(self, value: float) -> bytes:
        return struct.pack(">f", value)

    def encode_from_list(self, value: list) -> bytes:
        return b"".join(
            item if isinstance(item, bytes) else bytes(item) for item in value
        )

    def encode_from_any(self, value) -> bytes:
        if isinstance(value, int):
            return self.encode_from_int(value)
        elif isinstance(value, str):
            return self.encode_from_string(value)
        elif isinstance(value, float):
            return self.encode_from_float(value)
        elif isinstance(value, list):
            return self.encode_from_list(value)
        elif isinstance(value, bytes):
            return value
        else:
            raise ValueError(f"Unsupported type for encoding: {type(value)}")
