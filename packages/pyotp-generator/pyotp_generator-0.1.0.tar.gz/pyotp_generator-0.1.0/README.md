# OTP Generator

A simple Python package for generating and validating One-Time Passwords (OTPs) using the Time-Based One-Time Password (TOTP) algorithm. This package utilizes the `pyotp` library for OTP generation.

## Features

- Generate a new OTP based on a secret key.
- Validate provided OTPs against the generated ones.
- Simple command-line interface for easy usage.

## Installation

1. Clone the repository or download the package files.
2. Install the required dependencies:

   ```bash
   pip install pyotp
   ```

## Package Structure

```
otp_generator/
    ├── __init__.py
    ├── main.py
    └── otp.py
```

## Usage

### Generating a Secret Key

To generate a secure secret key for your OTP generator, you can use the following Python script:

```python
import pyotp

def generate_secret():
    secret = pyotp.random_base32()  # Generates a random base32 secret
    return secret

if __name__ == "__main__":
    secret_key = generate_secret()
    print(f"Your generated secret key is: {secret_key}")
```

Run the script:

```bash
python generate_secret.py
```

### Generating an OTP

To generate an OTP, use the command line:

```bash
python main.py --secret YOUR_SECRET --generate
```

### Validating an OTP

To validate an OTP, use the command line:

```bash
python main.py --secret YOUR_SECRET --validate YOUR_OTP
```

Replace `YOUR_SECRET` with the secret key you generated, and `YOUR_OTP` with the OTP you want to validate.

## Example

1. Generate a secret key:

   ```bash
   python generate_secret.py
   ```

   Output:
   ```
   Your generated secret key is: JBSWY3DPEHPK3PXP
   ```

2. Generate an OTP:

   ```bash
   python main.py --secret JBSWY3DPEHPK3PXP --generate
   ```

3. Validate an OTP:

   ```bash
   python main.py --secret JBSWY3DPEHPK3PXP --validate YOUR_OTP
   ```

## Notes

- Keep your secret key secure. Anyone with access to the key can generate valid OTPs.
- This implementation is for educational purposes. For production use, consider additional security measures.
```