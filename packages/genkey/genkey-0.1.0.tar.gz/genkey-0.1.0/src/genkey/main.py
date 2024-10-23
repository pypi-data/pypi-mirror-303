#!/usr/bin/env python3

import secrets
import string
import platform
import subprocess
import argparse


def generate_secure_key(length=32, use_special=True, use_numbers=True):
    """Generate a secure random key with specified parameters."""
    letters = string.ascii_letters
    chars = letters
    
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    return ''.join(secrets.choice(chars) for _ in range(length))


def copy_to_clipboard(text):
    """Copy text to system clipboard."""
    system = platform.system()
    try:
        if system == 'Darwin':  # macOS
            subprocess.run('pbcopy', input=text.encode())
        elif system == 'Windows':
            subprocess.run('clip', input=text.encode(), shell=True)
        elif system == 'Linux':
            subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode())
    except Exception as e:
        print(f"\033[31mWarning: Could not copy to clipboard: {e}\033[0m")


def main():
    """Main entry point for the command-line tool."""
    parser = argparse.ArgumentParser(description='Generate a secure key')
    parser.add_argument('-c', '--chars', type=int, default=32,
                      help='number of characters (default: 32)')
    parser.add_argument('-s', '--no-special', action='store_true',
                      help='exclude special characters')
    parser.add_argument('-n', '--no-numbers', action='store_true',
                      help='exclude numbers')

    args = parser.parse_args()

    secret_key = generate_secure_key(
        length=args.chars,
        use_special=not args.no_special,
        use_numbers=not args.no_numbers
    )

    copy_to_clipboard(secret_key)

    GREEN = '\033[32m'
    RESET = '\033[0m'
    print(f"{GREEN}{secret_key}{RESET}")


if __name__ == "__main__":
    main()