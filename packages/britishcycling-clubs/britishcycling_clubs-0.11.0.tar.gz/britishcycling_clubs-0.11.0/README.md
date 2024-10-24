# britishcycling-clubs


## About

**Unofficial, not affiliated or endorsed by British/Scottish/Welsh Cycling.**

Library to automate aspects of British Cycling's Club Management Tool, in order to
simplify administration for clubs using it. It probably works for Scottish/Welsh
Cycling clubs too, but this hasn't been tested.

Priority is to read data in order to create reports/notifications to club
administrators.


## Prerequisites

- ID for a club
- for Club Management Tool functions, valid user credentials


## Installation

Install from PyPI, e.g:
```shell
pip install britishcycling-clubs
```

Some functions use [Playwright](https://playwright.dev/python/) to automate a headless Chromium browser. This needs
to be installed separately before first use, and after most Playwright updates, e.g.:
```shell
playwright install chromium
```

If you're installing in e.g. a bare-bones server/CI environment, you'll probably be 
prompted to install system dependencies, which you can do with e.g.:
```shell
playwright install-deps chromium
```

See also https://playwright.dev/python/docs/browsers#install-system-dependencies


## Usage

### Get info from a club's profile

```python
from britishcycling_clubs import get_profile_info
get_profile_info(club_id="123")
```
Returns an instance of `ProfileInfo`, a `NamedTuple` with attributes:

- `club_name`: Club name [str]
- `total_members`: Total club members [int]

Example script `example_profile_info.py` loads club ID from `config.ini` (you'll
need to copy `config_dist.ini`, populate club ID only and rename).
It then retrieves and prints the club name and total member count.


### Construct club's profile URL

```python
from britishcycling_clubs import profile_url
profile_url(club_id="123")
```

### Get member counts from Club Manager

```python
from britishcycling_clubs import get_manager_member_counts
get_manager_member_counts(
    club_id="123",
    username="USERNAME",
    password="PASSWORD",
    manager_page_load_delay=7,
)
```
Returns an instance of `ManagerMemberCounts`, a `NamedTuple` with attributes:

- `active`: count of 'Active Club Members' [int]
- `expired`: count of 'Expired Club Members' [int]
- `new`: count of 'New Club Subscriptions' i.e. pending members [int]

This takes about 10 s.

Example script `example_manager_member_counts.py` loads club ID and credentials from
`config.ini` (you'll need to copy `config_dist.ini`, populate and rename to 
`config.ini`).
It then retrieves and prints the number of active, expired and new 
club member counts from the club's Club Manager pages. 

### Construct club's Club Manager URL (via login)

```python
from britishcycling_clubs import manager_url_via_login
manager_url_via_login(club_id="123")
```
Returns URL which redirects to Club Manager URL, via login if needed.


