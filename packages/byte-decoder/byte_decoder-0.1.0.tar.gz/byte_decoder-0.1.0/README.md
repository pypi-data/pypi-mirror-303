# Byte Decoder

A simple Python Library for decoding bytes into various data types.

## Installation

```bash
pip install byte-decoder
```

## Usage

```python
from byte_decoder import ByteDecoder

decoder = ByteDecoder()

# Decode to integer
int_value = decoder.decode_to_int(b'\x00\0f')
print(int_value) # output: 15

# Decode to string
string_value = decoder.decode_to_string(b'Hello')
print(string_value)  # Output: 'Hello'

# Decode to float
float_value = decoder.decode_to_float(b'@I\x0f\xdb')
print(float_value)  # Output: 3.14159

# Decode to list
list_value = decoder.decode_to_list(b'\x01\x02\x03\x04', 2)
print(list_value)  # Output: [b'\x01\x02', b'\x03\x04']
```

## License

This Project is licensed under the MIT License - see the LICENSE file for details.
