# uHugo

[![PyPI version](https://badge.fury.io/py/uhugo.svg)](https://badge.fury.io/py/uhugo) [![Docs](https://img.shields.io/badge/Documentation-Documentation%20for%20uHugo-green)](https://akshaybabloo.github.io/uHugo/)

uHugo is a CLI tool to install and update Hugo binary as well as updating any cloud providers

## Instillation

uHugo depends on Python 3.6+, on your terminal:

```sh
pip install uhugo
```

Once installed you can test it by:

```sh
uhugo --version
```

## Usage

uHugo provides two main commands - `install` and `update`

### Install

Using `uhugo install`, will download the latest binary file from [Hugo's repository](https://github.com/gohugoio/hugo) and adds it to `$HOME/bin` folder. You can force install by using `uhugo install --force`.

> Note: Make sure you have `$HOME/bin` in your `$PATH` environment variable

![uhugo install](https://github.com/akshaybabloo/uHugo/raw/main/screenshots/cmd-install.gif)

### Update

Using `uhugo update`, will update the current binary to the latest one. You can use `--to` flag to specify the version you want to rather update to. Example `uhugo update --to 0.80.0`

![uhugo update](https://github.com/akshaybabloo/uHugo/raw/main/screenshots/cmd-update.gif)

## Providers

Providers can be used to update Hugo environment variables or configuration files of a cloud provider. See the [provider docs](https://akshaybabloo.github.io/uHugo/providers/index.html) for more information.
