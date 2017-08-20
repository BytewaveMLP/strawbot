# strawbot

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Automated voting in strawpoll.com polls

# Install

```
$ pip install -r requirements.txt
```

# Usage

```
$ python strawbot.py
usage: strawbot.py [-h] pid oids

Spam-vote in strawpoll.com polls

positional arguments:
  pid         The poll ID to vote in (found at end of URL).
  oids        The checkbox ID(s) to submit votes for. Separated by #s. You can
              find this with inspect element (name= attribute on
              input[type=checkbox]).

optional arguments:
  -h, --help  show this help message and exit
```

# Maintainers

- [BytewaveMLP](https://github.com/BytewaveMLP)

# Contribute

**Questions? Comments? Concerns?** Shoot me an issue!

**Want to add something?** Shoot me a PR!

# License

Copyright (c) Eliot Partridge, 2017. Licensed under the [MIT license](/LICENSE).