# Internetspeed

Open-source CLI internet speed tool.

## Features

- Download speed
- Upload speed
- Public IP detection
- Live monitoring
- CLI interface

## Install

### From GitHub

on any linux distro that has python and pip insttalled

if not installed :
sudo apt install pipx
pipx install internetspeed

if already present:
python3 -m venv ~/internetspeed-env
export PATH=~/internetspeed-env/bin:$PATH
pip install internetspeed
internetspeed

```bash
pip install git+https://github.com/cranky420/internetspeed.git
```

## Usage

```bash
internetspeed test
internetspeed ip
internetspeed live
```

## Contributing

PRs welcome.
