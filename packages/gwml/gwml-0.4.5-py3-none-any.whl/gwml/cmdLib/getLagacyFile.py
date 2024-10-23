import zlib
import base64

def compress_file_to_file(input_file_path, output_file_path):
    """Compress the contents of the input file and save it to the output file as a base64 encoded string."""
    with open(input_file_path, 'r') as file:
        original_data = file.read()
    
    compressed_data = zlib.compress(original_data.encode())
    base64_encoded_data = base64.b64encode(compressed_data).decode()

    with open(output_file_path, 'w') as output_file:
        output_file.write(base64_encoded_data)

def decompress_file_to_file(input_file_path, output_file_path):
    """Read a base64 encoded compressed string from the input file, decompress it, and save it to the output file."""
    with open(input_file_path, 'r') as file:
        base64_encoded_data = file.read()

    compressed_data = base64.b64decode(base64_encoded_data.encode())
    decompressed_data = zlib.decompress(compressed_data).decode()

    with open(output_file_path, 'w') as output_file:
        output_file.write(decompressed_data)

# Usage example
# if __name__ == "__main__":
#     original_file_path = '/Users/dmshin/Downloads/model.tar (1)/dockerfile'  # Path to the original file
#     compressed_file_path = './lagacy/dockerfile'  # Path to save the compressed file
#     # decompressed_file_path = 'decompressed_file.txt'  # Path to save the decompressed file

#     # Compress the contents of the original file and save to the compressed file
#     compress_file_to_file(original_file_path, compressed_file_path)
#     print(f"File compressed and saved to {compressed_file_path}")

#     # Decompress the contents of the compressed file and save to the decompressed file
#     # decompress_file_to_file(compressed_file_path, decompressed_file_path)
#     # print(f"File decompressed and saved to {decompressed_file_path}")
