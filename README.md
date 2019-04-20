# SportBruter
> Tool to brute-force the login page of the official SportPesa website.

[<img src="https://img.shields.io/badge/Python-3.5%20%7C%203.6%20%7C%203.7-red.svg">](https://python.org)
[<img src="https://img.shields.io/badge/Requirements-Up%20To%20Date-green.svg">]
[<img src="https://img.shields.io/badge/License-MIT-blue.svg">](https://github.com/briancanspit/sportbruter/license)
[<img src="https://img.shields.io/badge/Rating-3.0%2F5-orange.svg">]
[<img src="https://img.shields.io/badge/Updated-Today-brightgreen.svg">]

SportBruter is a little script I wrote (cause I was bored) to try and authenticate as a user against a defined list of passwords.

Depending on user preference, it gathers a list of free proxies to use should the user choose a bit of anonymity, and attacks. 

The script has been written in Python 3, as such, trying to run it using Python 2 will cause it to fail.

![](header.png)
![](header2.png)

## Installation

To get started, you pretty much just have to clone the script:

```sh
git clone https://github.com/briancanspit/sportbruter.git
```

Then, get into the directory itself:

```sh
cd
```

Finally, install the dependencies it needs by running:

```sh
python3 -m pip install -r requirements.txt
```

## Usage example

This script depends on Python 3 or its variants. To run it, simply execute:

```sh
python3 sportbruter.py
```

## 

If you run into any issues concerning failed module importation, it means you did not install the modules found in the requirements.txt file.

To fix this, run the command below in your terminal (not the Python console):

```sh
python3 -m pip install -r requirements.txt
```

Or, if that doesn't work, directly invoke pip, by running:

```sh
pip install -r requirements.txt
```

This should fix any import errors you might have.

## Meta

Shoot me a message – [@briancanspit](https://twitter.com/briancanspit) – briancanspit@gmail.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/briancanspit/sportbruter](https://github.com/briancanspit/)

