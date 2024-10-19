# main/decoder.py


from typing import Optional


def decode_bytes(byte_data: bytes) -> Optional[int]:
    """
    Extract the weight from a given byte sequence.

    Parameters:
        data (bytes): The byte data that contains encoded weight information.

    Returns:
        Optional[int]: The extracted weight if valid, otherwise None.
    """
    byte_to_digit_mapping = {
        0x30: "0",  # '0' encoded in some specific format
        0xB1: "1",  # '1' encoded as 0xb1
        0xB2: "2",  # '2' encoded as 0xb2
        0xB3: "3",  # '3' encoded as 0xb3
        0xB4: "4",  # '4' encoded as 0xb4
        0xB5: "5",  # '5' encoded as 0xb5
        0xB6: "6",  # '6' encoded as 0xb6
        0xB7: "7",  # '7' encoded as 0xb7
        0xB8: "8",  # '8' encoded as 0xb8
        0xB9: "9",  # '9' encoded as 0xb9
    }

    # Convert the input data (which is a bytes object) to a mutable bytearray
    # A bytearray allows us to iterate and access individual byte values
    data_array = bytearray(byte_data)

    # List to store the decoded digits (as strings) from the byte array
    weight_digits = []

    # Iterate over each byte in the byte array
    for byte in data_array:
        if 0x30 <= byte <= 0x39:
            weight_digits.append(chr(byte))

        elif byte in byte_to_digit_mapping:
            weight_digits.append(byte_to_digit_mapping[byte])

    if weight_digits:
        weight_str = "".join(weight_digits)
        try:
            weight = int(weight_str)
            return weight
        except ValueError:
            return None
    else:
        return None
