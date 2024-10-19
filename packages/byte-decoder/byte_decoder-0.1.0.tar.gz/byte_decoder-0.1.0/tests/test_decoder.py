import unittest
from byte_decoder import ByteDecoder


class TestByteDecoder(unittest.TestCase):
    def setUp(self):
        self.decoder = ByteDecoder()

    def test_decode_to_int(self):
        self.assertEqual(self.decoder.decode_to_int(b"\x00\x0f"), 15)

    def test_decode_to_string(self):
        self.assertEqual(self.decoder.decode_to_string(b"Hello"), "Hello")

    def test_decode_to_float(self):
        self.assertAlmostEqual(
            self.decoder.decode_to_float(b"@I\x0f\xdb"), 3.14159, places=5
        )

    def test_decode_to_list(self):
        self.assertEqual(
            self.decoder.decode_to_list(b"\x01\x02\x03\x04", 2),
            [b"\x01\x02", b"\x03\04"],
        )


if __name__ == "__main__":
    unittest.main()
