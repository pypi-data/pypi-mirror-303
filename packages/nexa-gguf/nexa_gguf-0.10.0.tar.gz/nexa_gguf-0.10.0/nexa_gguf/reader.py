#!/usr/bin/env python3
import logging
import sys
from pathlib import Path
from nexa_gguf.gguf_reader import GGUFReader
from nexa_gguf.constants import GGUFValueType
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("reader")

sys.path.insert(0, str(Path(__file__).parent.parent))


def convert_value(value, value_type):
    """
    Converts the value based on its type to a more readable format.
    """
    if value_type == GGUFValueType.STRING:
        return bytes(value).decode('utf-8')
    elif value_type in [GGUFValueType.UINT8, GGUFValueType.INT8, GGUFValueType.UINT16, 
                        GGUFValueType.INT16, GGUFValueType.UINT32, GGUFValueType.INT32, 
                        GGUFValueType.UINT64, GGUFValueType.INT64]:
        return int(value) if isinstance(value, np.number) else int(value[0])
    elif value_type in [GGUFValueType.FLOAT32, GGUFValueType.FLOAT64]:
        return float(value) if isinstance(value, np.number) else float(value[0])
    elif value_type == GGUFValueType.BOOL:
        return bool(value) if isinstance(value, np.number) else bool(value[0])
    elif value_type == GGUFValueType.ARRAY:
        if isinstance(value, np.ndarray):
            return value.tolist()
        elif isinstance(value, (list, tuple)):
            return [convert_value(v, value_type) for v in value]
        else:
            return value
    else:
        return value  # Return as-is for unknown types

def read_gguf_file(gguf_file_path):
    """
    Reads and prints key-value pairs and tensor information from a GGUF file in an improved format.

    Parameters:
    - gguf_file_path: Path to the GGUF file.
    """

    reader = GGUFReader(gguf_file_path)

    # List all key-value pairs in a columnized format
    print("Key-Value Pairs:") # noqa: NP100
    max_key_length = max(len(key) for key in reader.fields.keys())
    for key, field in reader.fields.items():
        value = field.parts[field.data[0]]
        converted_value = convert_value(value, field.types[0])
        print(f"{key:{max_key_length}} : {converted_value}") # noqa: NP100
    print("----") # noqa: NP100

    # List all tensors
    print("Tensors:") # noqa: NP100
    
    # Get max lengths for each column
    max_name_len = max(len(tensor.name) for tensor in reader.tensors)
    max_shape_len = max(len("x".join(map(str, tensor.shape))) for tensor in reader.tensors)
    max_size_len = max(len(str(tensor.n_elements)) for tensor in reader.tensors)
    max_quant_len = max(len(tensor.tensor_type.name) for tensor in reader.tensors)

    # Create the format string with dynamic column widths
    tensor_info_format = "{{:<{}}} | Shape: {{:<{}}} | Size: {{:<{}}} | Quantization: {{:<{}}}"
    tensor_info_format = tensor_info_format.format(max_name_len, max_shape_len, max_size_len, max_quant_len)

    # Print header
    print(tensor_info_format.format("Tensor Name", "Shape", "Size", "Quantization")) # noqa: NP100
    print("-" * (max_name_len + max_shape_len + max_size_len + max_quant_len + 30)) # noqa: NP100

    # Print tensor info
    for tensor in reader.tensors:
        shape_str = "x".join(map(str, tensor.shape))
        size_str = str(tensor.n_elements)
        quantization_str = tensor.tensor_type.name
        print(tensor_info_format.format(tensor.name, shape_str, size_str, quantization_str)) # noqa: NP100


def read_gguf_file_for_result(gguf_file_path):
    """
    Reads key-value pairs and tensor information from a GGUF file and returns them as a dictionary.

    Parameters:
    - gguf_file_path: Path to the GGUF file.

    Returns:
    A dictionary with two keys:
    - 'key_value_pairs': A dictionary of key-value pairs from the GGUF file.
    - 'tensors': A list of dictionaries, each containing information about a tensor.
    """
    reader = GGUFReader(gguf_file_path)

    # Process key-value pairs
    key_value_pairs = {}
    for key, field in reader.fields.items():
        value = field.parts[field.data[0]]
        key_value_pairs[key] = convert_value(value, field.types[0])

    # Process tensors
    tensors = []
    for tensor in reader.tensors:
        tensor_info = {
            "name": tensor.name,
            "shape": "x".join(map(str, tensor.shape)),
            "size": tensor.n_elements,
            "quantization": tensor.tensor_type.name
        }
        tensors.append(tensor_info)

    return {
        "key_value_pairs": key_value_pairs,
        "tensors": tensors
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.error("Usage: reader.py <path_to_gguf_file>")
        sys.exit(1)
    gguf_file_path = sys.argv[1]
    read_gguf_file(gguf_file_path)
