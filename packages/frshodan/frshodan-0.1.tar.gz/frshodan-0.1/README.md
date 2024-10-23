
# FrShodan
A library for querying **shodan** with no API key.
## Features
- No API key Required
- No login requiered
- Can search premium tags such as the **vuln** tag and **tag** tag for free
## Installation
>Make sure to use **sudo**!
### Easy Way
```sudo pip3 install frshodan```
### Hard Way
```
pip install setuptools wheel
git clone https://github.com/LavedenC1/frshodan
cd frshodan
# First edit setup.py
python setup.py sdist bdist_wheel
sudo pip3 install .
```
## Usage
### Python3 Utility
*Make Sure to use quotation marks around the query to avoid problems*
```
from frshodan import frshodan # Import the package

frshodan(query,sleep) # Usage

print(frshodan("port:22 OpenSSL", 0.5)) # Example
```
### CLI utility
*Make Sure to use quotation marks around the query to avoid problems*
```
user@localhost:~$ frshodan "<query>"
```
> <query\> is optional, not using it will give the option to dump to a file and gives an interactive quote.

The function returns the results in a list, and if an error occurs, it will return the status code.

## Sources
- [Shodan IDOR](https://github.com/sahar042/Shodan-IDOR)
-- Thanks for giving me the idea.
- Myself
