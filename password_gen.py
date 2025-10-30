#!/usr/bin/env python3
import argparse, secrets, string

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{};:,.<>?"
    if length < 4:
        raise ValueError("Minimum length is 4.")
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        if use_upper and not any(c.isupper() for c in pwd): continue
        if use_digits and not any(c.isdigit() for c in pwd): continue
        if use_symbols and not any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in pwd): continue
        return pwd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple password generator")
    parser.add_argument("length", type=int, nargs="?", default=16, help="Password length (default: 16)")
    parser.add_argument("--no-upper", action="store_true", help="Disable uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Disable digits")
    parser.add_argument("--no-symbols", action="store_true", help="Disable special characters")
    args = parser.parse_args()
    print(generate_password(
        args.length,
        not args.no_upper,
        not args.no_digits,
        not args.no_symbols
    ))
