from PIL import Image

def get_image_data(filename):
    with Image.open(filename) as img:
        img = img.convert("RGB")
        return list(img.tobytes())

def lzw_compress_image(image_data):
    dictionary = {bytes([i]): i for i in range(256)}
    current_sequence = b""
    compressed_data = []
    dict_size = 256

    for byte in image_data:
        combined_sequence = current_sequence + bytes([byte])
        if combined_sequence in dictionary:
            current_sequence = combined_sequence
        else:
            compressed_data.append(dictionary[current_sequence])
            dictionary[combined_sequence] = dict_size
            dict_size += 1
            current_sequence = bytes([byte])

    if current_sequence:
        compressed_data.append(dictionary[current_sequence])

    return compressed_data

def generate_keys():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def rsa_encrypt(data, public_key):
    e, n = public_key
    return [pow(byte, e, n) for byte in data]

def convert_to_bytes(data):
    byte_array = bytearray()
    for number in data:
        byte_array.extend(number.to_bytes((number.bit_length() + 7) // 8, 'big'))
    return byte_array

def convert_to_byte_list(data):
    byte_list = []
    for number in data:
        byte_list.extend(number.to_bytes((number.bit_length() + 7) // 8, 'big'))
    return byte_list

def process_image(filename):
    image_data = get_image_data(filename)
    public_key, private_key = generate_keys()
    compressed_data = lzw_compress_image(image_data)
    encrypted_compressed_data = rsa_encrypt(compressed_data, public_key)
    with open("compressed_then_encrypted.bin", "wb") as f:
        f.write(convert_to_bytes(encrypted_compressed_data))
    encrypted_data = rsa_encrypt(image_data, public_key)
    encrypted_data_bytes = convert_to_byte_list(encrypted_data)
    compressed_encrypted_data = lzw_compress_image(encrypted_data_bytes)
    with open("encrypted_then_compressed.bin", "wb") as f:
        f.write(convert_to_bytes(compressed_encrypted_data))
    print("Archivos generados: 'compressed_then_encrypted.bin' y 'encrypted_then_compressed.bin'")

process_image("images.jpg")