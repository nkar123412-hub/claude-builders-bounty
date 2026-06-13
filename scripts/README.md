# Changelog Generator
A simple Python script to generate a structured CHANGELOG.md from git history.

## Setup
1. Place  in your project root.
2. Run .

## How it works
It fetches commits since the last git tag and categorizes them based on keywords:
- Added: feat, add, new
- Fixed: fix, bug, patch
- Changed: refactor, update, change, improve
- Removed: remove, delete, drop
- Other: everything else
