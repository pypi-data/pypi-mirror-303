# Byte Codec

A simple Python Library for encoding and decoding various data types to and from bytes.

## Installation

```bash
pip install byte-codec
```

## Usage

```python
from byte_codec import ByteCodec

codec = ByteCodec()

# Encoding
int_bytes = codec.encode_from_int(12345)
string_bytes = codec.encode_from_string("Hello, World!")
float_bytes = codec.encode_from_float(3.14159)
list_bytes = codec.encode_from_list([b'\x01\x02', b'\x03\x04'])

# Decoding
int_value = codec.decode_to_int(int_bytes)
string_value = codec.decode_to_string(string_bytes)
float_value = codec.decode_to_float(float_bytes)
list_value = codec.decode_to_list(list_bytes, 2)

# Generic encoding
any_bytes = codec.encode_from_any(12345)  # Works with int, str, float, list, or bytes
```

## License

This Project is licensed under the MIT License - see the LICENSE file for details.
