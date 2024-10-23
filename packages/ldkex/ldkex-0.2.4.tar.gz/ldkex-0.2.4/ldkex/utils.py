import decimal
import struct


def read_int(file):
    bytes_data = read_fully(file, 4)
    return struct.unpack('>i', bytes_data)[0]


def read_coordinate(file):
    bytes_data = read_fully(file, 4)
    value = struct.unpack('>i', bytes_data)[0] * 1e-7
    bd = decimal.Decimal(value).quantize(decimal.Decimal('1.0000000'), rounding=decimal.ROUND_HALF_UP)
    return float(bd)


def read_long(file):
    bytes_data = read_fully(file, 8)
    return struct.unpack('>q', bytes_data)[0]


def read_double(file):
    bytes_data = read_fully(file, 8)
    return struct.unpack('>d', bytes_data)[0]


def read_pointer(file):
    bytes_data = read_fully(file, 8)
    return struct.unpack('>Q', bytes_data)[0]


def read_string(file, length):
    buffer = []
    buffer_size = 1024  # Read in chunks of 1 KB

    while length > 0:
        bytes_to_read = min(length, buffer_size)
        chunk = read_fully(file, bytes_to_read)
        if not chunk:
            break
        buffer.append(chunk.decode('utf-8'))
        length -= len(chunk)

    return ''.join(buffer).strip()


def read_boolean(file):
    byte = file.read(1)
    if len(byte) == 0:
        raise EOFError("End of file reached before reading a boolean")
    return byte != b'\x00'


def read_fully(file, size):
    data = bytearray()
    while len(data) < size:
        print(f"Reading {size - len(data)} bytes;")  # Debug
        chunk = file.read(size - len(data))
        if not chunk:
            raise EOFError("End of file reached before reading the required number of bytes")
        data.extend(chunk)
    return bytes(data)


def get_metadata_version(magic_number, file_type):
    if magic_number > 100:
        return 3
    elif file_type == "trk":
        return 2 if magic_number == 3 else 1
    else:
        return 2 if magic_number == 2 else 1
