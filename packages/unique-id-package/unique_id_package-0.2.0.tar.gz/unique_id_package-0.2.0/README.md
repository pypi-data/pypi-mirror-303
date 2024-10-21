# Unique ID Package

This package generates unique IDs similar to UUID, either as a string or digits only.

## Installation

```bash
pip install unique_id_package
```

## Usage

```python
from unique_id_package import UniqueID

# Generate a unique ID as a string
unique_id = UniqueID.generate_id()

# Generate a unique ID as digits only
unique_id_digits = UniqueID.generate_id(digits_only=True)
```

## License

This package is licensed under the MIT License.

