# GenKey

A simple command-line tool to generate secure keys and passwords.

## Installation

```bash
pip install genkey
```

## Usage

Generate a key (default 32 characters):
```bash
genkey
```

Generate a 12-character key:
```bash
genkey -c 12
```

Generate a key without special characters:
```bash
genkey -s
```

Generate a key without numbers:
```bash
genkey -n
```

Combine options:
```bash
genkey -c 16 -s -n
```

## Features

- Generates cryptographically secure random keys
- Customizable length
- Option to exclude special characters
- Option to exclude numbers
- Automatically copies to clipboard
- Cross-platform (Windows, macOS, Linux)

## Requirements

For clipboard functionality:
- Windows: No additional requirements
- macOS: No additional requirements
- Linux: xclip (can be installed via `sudo apt-get install xclip` on Debian/Ubuntu)

## License

This project is licensed under the MIT License - see the LICENSE file for details.