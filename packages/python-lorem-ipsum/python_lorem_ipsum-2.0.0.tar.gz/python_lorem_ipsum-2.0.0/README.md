# Lorem ipsum generator

* [Installation](#installation)
* [Usage](#usage)
* [Testing](#testing)

-------------------------------------------------------------------------------

> NB: uses [semantic versioning](https://semver.org).

In publishing and graphic design, *lorem ipsum* is a placeholder text commonly
used to demonstrate the visual form of a document or a typeface without
relying on meaningful content.

The `lorem` module provides a generic access to generating the *lorem ipsum*
text from its very original text:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
> tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
> veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
> commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
> esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
> cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
> est laborum.

## Installation

> Note that the `lorem` module only supports Python versions __since 3.5__ 🐍

Simply run the following to install the current version from PyPI:

```sh
pip install python-lorem-ipsum
```

Or install the latest version from the git repository:

```sh
git clone https://github.com/adambirds/python-lorem-ipsum.git
cd lorem
pip install -e .
# and to update at any time
git pull
```

## Usage

Usage of the `lorem` module is rather simple. Depending on your needs, the
`lorem` module provides generation of **word**s, **sentence**s, and
**paragraph**s:

```python
import lorem

print(lorem.get_sentence(count=3))
```

> Eu consectetur ad et, exercitation fugiat occaecat exercitation cillum non ullamco, elit mollit est consectetur. In ex proident esse est aute est mollit, id minim lorem tempor sunt elit. Dolor aliqua non eiusmod officia esse adipiscing.

Please refer to the [documentation](https://jarryshaw.github.io/lorem/)
for more details.

## Testing

The `lorem` module utilised `unittest.mock` to *patch* the builtin functions
from `random` module. Test cases can be found in [`test_lorem.py`](test_lorem.py).
**Contributions are welcome.**
