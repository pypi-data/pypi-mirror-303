# fast2app package

<!-- STATUS HEADERs -->

[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![coverage](https://git.mydh.io/shared/fast2app/badges/main/coverage.svg?job=coverage)

<!-- RELATIONSHIIPS -->

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Nuxtjs](https://img.shields.io/badge/Nuxt-002E3B?style=for-the-badge&logo=nuxtdotjs&logoColor=#00DC82)

## Description

A simple tool designed to automatically generate usable types, functions, and other useful server-side code from a list of [FastAPI](https://fastapi.tiangolo.com/) application to a given framework.

This is particularly helpful when working with FasttAPI backends applications and wanting to generate types and functions for the frontend.

## Currently supported frameworks

- [Nuxt3](https://nuxt.com/)

# Installation

```powershell
#  Install fast2app
pip install fast2app
```

## Requirements

This package is currently compatible with python 3.11 and above.

It requires that you have the [quicktype](https://quicktype.io/) CLI utility installed.

```powershell
#  Install quicktype
npm install -g quicktype
```

# Usage and examples

This package is used as a CLI tool.

```powershell
# Nuxt3
# You must ammend your nuxt.config.ts file and environement variables in order to use the new generated files. See documentations below.

fast2nuxt --fast-api-app path/to/fastapi/app.py::app_name --export-path path/to/nuxt/app/root/folder -composables
```

For specific instructions, please see :

- [Nuxt Documentation](./NUXT_DOCUMENTATION.md)

# Helpdesk

[Go here to report an issue](https://helpdesk.mydh.io/issue-form)

- [Current Issues](https://git.mydh.io/shared/fast2app/-/issues)
- [Known limitations](./KNOWN_LIMITATIONS.md)

# Current Features

## Core

- Command line interface with fast2app
- Export FastAPI pydantic model as typescript interfaces in nuxt, including Enums
- Export FastApi as Nuxt API Server
- Export FastApi as Nuxt Composables

## Tests

- Base Tests
- Utils Tests
- Export Tests
- CLI Tests
- Integration tests :
  - Nuxt :
    - Api Server
    - Composables
- Coverage as artifacts
- Junit reports

# Roadmap

## Future releases

- Create e more robust documentation in a website
- make it compatible with older python versions
- Refactor package to more easily add support for more frameworks.
- Refactor testing in order to use the same parameters and edge cases for all frameworks.
- Add python framework support.

## Ambitions

- Add support for more frameworks (React, Vue, Angular, etc.) with contributions from the community.

# Contributing

I've launched into this project as a side task of a bigger endeavor.

Considerig the growing popularity of [FastAPI](https://fastapi.tiangolo.com/), I think that this tool could be a great addition to the ecosystem and I have decided to make it open source.

I'm new to open source and am open to any ideas, contribution or constructive feedback.

[Go here to contact me](https://helpdesk.mydh.io/contact-form)

## Retrieve the repository

```powershell
cd existing_repo
git remote add origin https://git.mydh.io/shared/fast2app.git
git branch -M main
git pull origin main
```

# License

This project is licensed under the terms of the MIT license.
