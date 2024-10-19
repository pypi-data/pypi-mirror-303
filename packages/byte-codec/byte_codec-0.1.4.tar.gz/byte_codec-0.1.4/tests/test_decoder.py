import unittest
from byte_codec import ByteCodec


class TestByteCodec(unittest.TestCase):
    def setUp(self):
        self.codec = ByteCodec()

    def test_int_codec(self):
        original = 12345
        encoded = self.codec.encode_from_int(original)
        decoded = self.codec.decode_to_int(encoded)
        self.assertEqual(original, decoded)

    def test_string_codec(self):
        original = "Hello, World!"
        encoded = self.codec.encode_from_string(original)
        decoded = self.codec.decode_to_string(encoded)
        self.assertEqual(original, decoded)

    def test_float_codec(self):
        original = 3.14159
        encoded = self.codec.encode_from_float(original)
        decoded = self.codec.decode_to_float(encoded)
        self.assertAlmostEqual(original, decoded, places=5)

    def test_list_codec(self):
        original = [b"\x01\x02", b"\x03\x04"]
        encoded = self.codec.encode_from_list(original)
        decoded = self.codec.decode_to_list(encoded, 2)
        self.assertEqual(original, decoded)

    def test_encode_from_any(self):
        self.assertEqual(
            self.codec.encode_from_any(12345), self.codec.encode_from_int(12345)
        )
        self.assertEqual(
            self.codec.encode_from_any("test"), self.codec.encode_from_string("test")
        )
        self.assertEqual(
            self.codec.encode_from_any(3.14), self.codec.encode_from_float(3.14)
        )
        self.assertEqual(
            self.codec.encode_from_any([1, 2, 3]),
            self.codec.encode_from_list([1, 2, 3]),
        )
        with self.assertRaises(ValueError):
            self.codec.encode_from_any({1: 2})  # dict is not supported


if __name__ == "__main__":
    unittest.main()
