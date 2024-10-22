# Hyrule Shield

Hyrule Shield is a Python library for anonymizing sensitive information in texts. The library uses Natural Language Processing (NLP) techniques to identify and anonymize data such as personal names, CPF, CNPJ, addresses, phone numbers, and more.

## Features
- Anonymization of personal information such as CPF, RG, CNPJ, phone numbers, and addresses.
- Uses pre-trained SpaCy models for entity recognition in Portuguese.
- Easy integration with other projects.

## Installation

You can install the library directly from PyPI (when available):

```sh
pip install hyrule_shield
```

Or install it locally after cloning this repository:

```sh
pip install -e .
```

## Usage

Here is a simple example of how to use the library to anonymize a message:

```python
from hyrule_shield.anonymizer import anonymize_message_spacy

message = "My name is Carlos Eduardo, my CPF is 111.222.333-44."
anonymized_message = anonymize_message_spacy(message)
print(anonymized_message)
```

**Output:**
```
My name is <PER>, my CPF is <CPF>.
```

## Dependencies
- Python 3.7, 3.8, 3.9, 3.10, 3.11
- spacy>=3.0.0
- transformers>=4.0.0

## Development

If you want to contribute to the development of this library, follow the steps below:

1. Clone the repository:
   ```sh
   git clone https://github.com/jadercampos/hyrule_shield.git
   ```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```sh
   python -m unittest discover tests
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## Author
- Jader Campos - [jadercampos@gmail.com](mailto:jadercampos@gmail.com)
