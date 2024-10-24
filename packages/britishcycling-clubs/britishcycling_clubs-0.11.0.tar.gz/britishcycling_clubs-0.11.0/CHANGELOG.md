# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project tries to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Historic and pre-release versions aren't necessarily included.


## [0.11.0] - 2024-10-23

### Added

- Support for Python 3.13

### Changed

- Docs: docstring fixes
- Update dev dependencies: mypy, pdoc, pytest, ruff

## [0.10.0] - 2024-07-15

### Changed

- *BREAKING CHANGES:*
  - `get_profile_info()` returns`ProfileInfo` `NamedTuple` instead of dict 
  - `get_manager_member_counts()` returns `ManagerMemberCounts` `NamedTuple` 
    instead of dict
  - `club_manager_url_via_login()` renamed to `manager_url_via_login()`
  - `club_profile_url()` renamed to `profile_url()`
- Only get logger once, rather than for every log message
- Docs: docstring simplification, improvements
- Dev dependencies: add pdoc
- Linting/CI: tighten ruff config 


## [0.9.1] - 2024-07-13

### Added

- CI: run tests

### Changed

- Dependencies: remove upper bounds when specifying versions 
- Dev dependencies: use ruff for formatting; drop black + isort
- CI: Reduce Dependabot frequency to monthly

### Fixed

- Removed unintended public logging constant
- Tests: warnings because Beautiful Soup parser wasn't specified
- Tests didn't use public API for imports


## [0.9.0] - 2023-12-20

### Added

- `club_profile_url` and `club_manager_url_via_login()` 

### Changed

- Update dev/test dependencies: black, ruff, types-beautifulsoup4


## [0.8.1] - 2023-12-19

### Fixed

- `get_manager_member_counts()` still returned `["pending"]` instead of
  `["new"]`


## [0.8.0] - 2023-12-19

### Changed

- **BREAKING CHANGES**: Functions renamed to `get_profile_info()` and 
  `get_manager_member_counts()`. `get_manager_member_counts()` returns `["new"]`
  instead of `["pending"]`

- Update dev/test dependencies: isort, mypy; CI dependencies actions/checkout, 
  actions/setup-python

### Added

- `get_profile_info()`: raise exception on redirect; better error messages; basic 
  unit tests
 
- `get_manager_member_counts()` basic unit tests
 
- Enable logging for Playwright operations in example script

### Fixed

- Duplicate logging message


## [0.7.0] - 2023-11-24

### Added

- Logging for Playwright operations in `get_private_member_counts()` 


## [0.6.0] - 2023-11-21

### Added

- Support Python 3.12 in CI workflow

### Changed

- `get_private_member_counts()`: raise exception if zero 'active members' would be 
  returned

- Update dev/test dependencies: mypy, ruff


## [0.5.0] - 2023-11-09

### Added

- Optional page load delay in `get_private_member_counts()` 

### Changed

- Update dev/test dependencies: black, ruff


## [0.4.2] - 2023-10-23

### Changed

- Update dependencies: requests, playwright

- Update dev/test dependencies: black, mypy, ruff, types-requests


## [0.4.1] - 2023-09-27

### Fixed

- Missing/outdated/broken package metadata

### Changed

- Update dev/test dependencies: ruff


## [0.4.0] - 2023-09-25

### Added

- PEP 561 typing compatibility

- Documentation: Explain how to install playwright system dependencies

### Changed

- Update dev/test dependencies: ruff


## [0.3.0] - 2023-09-21

### Added

- This changelog

- Documentation: Describe public functions in README 

- Dev/test dependencies: ruff

- Enforce linting with isort, black, ruff and static type checking with mypy in CI 
  using GitHub Actions

### Fixed

- Reliability issues when getting data from Club Manager pages with
 `get_private_member_counts()`. See 'Changed'

- Use of `assert` in production code

### Changed

- **BREAKING CHANGE**: Simplify package structure.
 
  `import britishcycling-clubs.main` should be replaced with `import 
  britishcycling-clubs`

- Use [Playwright](https://playwright.dev/python/) instead of Selenium when getting 
  data from Club Manager pages with `get_private_member_counts()`

  This makes deployment easier, as Playwright simplifies browser installation and
  updates, and a separate driver executable is no longer required. README updated to 
  cover this

- Update dev/test dependencies: black, mypy, pytest, types-requests, 
  types-beautifulsoup4

### Removed

- Trivial test which didn't have any real value

- Dev dependencies: pylint


## [0.2.5] - 2023-05-30

### Changed

- Minor code, type hinting and docstring improvements

- Update dev dependencies: mypy, pylint, test, types-requests, types-beautifulsoup4


[0.11.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.9.1...v0.10.0
[0.9.1]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.8.1...v0.9.0
[0.8.1]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.4.2...v0.5.0
[0.4.2]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.2.5...v0.3.0
[0.2.5]: https://github.com/elliot-100/britishcycling-clubs/compare/v0.2.3...v0.2.5
