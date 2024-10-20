# py2fa-cli

[![PyPI version](https://img.shields.io/pypi/v/py2fa-cli?logo=python&label=PyPI)](https://pypi.org/project/py2fa-cli/)
[![PePy downloads](https://img.shields.io/pepy/dt/py2fa-cli?logo=python&label=Downloads&color=%230C7DBE)](https://pepy.tech/project/py2fa-cli)

Calculates and displays time-based one-time passwords (TOTP) for two-factor
authentication:

```sh
$ py2fa pypi.org
One-time password: 123456 (valid for 13.7 seconds)
```

## Installation

For typical use:

```sh
python3 -m pip install py2fa-cli
```

For development:

```sh
git clone https://github.com/arcctgx/py2fa-cli
cd py2fa-cli
python3 -m pip install --editable .
```

## Dependencies

* `pyotp`
* `pyxdg`

These dependencies will be installed automatically when `py2fa-cli` is installed
by `pip`.

## Configuration

TOTP secrets are stored in user's XDG configuration directory. Unless you
changed your `XDG_CONFIG_HOME`, that will be `.config/py2fa/secrets.json` in
your `$HOME`. The secrets file must not be world-accessible (readable, writable
or executable): in such case `py2fa` will refuse to load it.

The secrets file is a dictionary represented in JSON format, e.g.:

```json
{
    "pypi.org": "MYPYPITOTPSECRET",
    "test.pypi.org": "MYTESTPYPITOTPSECRET"
}
```

The dictionary key is what you provide in the command-line, so just use any
name that's convenient. The value is the shared TOTP secret in base32 format.

### A note for Microsoft Authenticator users

It is not possible to extract the shared secret from the Microsoft Authenticator
application once it's been configured. You can only obtain the shared secret
when you first set up the authenticator app.

When presented with a QR code, **do not** scan it with Microsoft Authenticator.
Instead use some generic QR scanner app. You should get an URI similar to this
one:

```text
otpauth://totp/YourOrg%3Ayour.email%40your.org?secret=TWOJDZIENTWOJAWODA&issuer=Microsoft
```

Extract the secret from the URI and put it in your `secrets.json` file. If you
want to, you can scan the QR code with Microsoft Authenticator now. `py2fa` and
the authenticator app will generate the same TOTP codes.
