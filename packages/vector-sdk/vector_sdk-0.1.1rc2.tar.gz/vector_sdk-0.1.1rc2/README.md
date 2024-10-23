# vector-sdk

[![Upload Python Package](https://github.com/dhruv-anand-aintech/vector-sdk/actions/workflows/python-publish.yml/badge.svg?branch=main)](https://github.com/dhruv-anand-aintech/vector-sdk/actions/workflows/python-publish.yml)

## Version Management

We use a custom script to manage version bumping. To use it:

1. For release candidates: `python bump_version.py rc`
   This will update the version to the next release candidate (e.g., 0.1.0rc1 to 0.1.0rc2)

2. For release versions: `python bump_version.py release`
   This will update the version to the final release version (e.g., 0.1.0rc2 to 0.1.0)

3. For other version bumps: `python bump_version.py major|minor|patch`
   This will update the version accordingly (e.g., 0.1.0 to 1.0.0 for major)