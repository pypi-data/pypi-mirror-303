"""Calculate one-time passwords for two-factor authentication."""

import argparse
import binascii
import sys
from time import time

from pyotp import TOTP

from py2fa import VERSION
from py2fa.config import load_secrets


def _parse_args():
    parser = argparse.ArgumentParser(
        description="""Calculate one-time passwords for two-factor authentication.""")

    parser.add_argument('secret_name', help='name of secret to display TOTP code for')
    parser.add_argument('-v', '--version', action='version', version=VERSION)

    return parser.parse_args()


def main():
    args = _parse_args()

    secrets = load_secrets()
    if secrets is None:
        print('ERR: Failed to load secrets file!')
        sys.exit(1)

    try:
        secret = secrets[args.secret_name]
    except KeyError:
        print(f'ERR: No secret for {args.secret_name} is available!')
        sys.exit(1)

    totp = TOTP(secret)
    valid_for = 30.0 - time() % 30

    try:
        print(f'One-time password: {totp.now()} (valid for {valid_for:.1f} seconds)')
    except binascii.Error as err:
        print(f'ERR: Failed to generate TOTP: {err}. Verify your secret.')
        sys.exit(1)


if __name__ == '__main__':
    main()
