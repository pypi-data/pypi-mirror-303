![darkdown](./logo.webp)

# darkdown

A Python 3 `http.server` wrapper that supports ssl, basic auth, markdown rendering, and styling support for directory listings and markdown files.

## Installation

```sh
python3 -m pip install darkdown
```

## Manual Installation

```sh
git clone https://github.com/phx/darkdown
cd darkdown
python3 -m pip install -r requirements.txt
```

## Usage

```
usage: darkdown [-h] [-p PORT] [-b ADDRESS] [--directory DIRECTORY] [-u USERNAME] [-P PASSWORD] [-c CERTFILE] [-k KEYFILE]

Secure Markdown HTTP server with GitHub-style rendering, authentication, and HTTPS support.

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Specify alternate port [default: 8000]
  -b ADDRESS, --bind ADDRESS
                        Specify alternate bind address [default: all interfaces]
  --directory DIRECTORY
                        Specify alternate directory [default: current directory]
  -u USERNAME, --user USERNAME
                        Set a username for basic authentication
  -P PASSWORD, --password PASSWORD
                        Set a password for basic authentication
  -c CERTFILE, --cert CERTFILE
                        Path to the SSL certificate file (for HTTPS)
  -k KEYFILE, --key KEYFILE
                        Path to the SSL key file (for HTTPS)
```

