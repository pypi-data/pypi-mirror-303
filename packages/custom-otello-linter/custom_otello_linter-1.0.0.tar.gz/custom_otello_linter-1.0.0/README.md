# custom-otello-linter
Flake8 based linter for frontend tests

## Installation

```bash
pip install custom-otello-linter
```

## Configuration
Custom-otello-linter is flake8 plugin, so the configuration is the same as [flake8 configuration](https://flake8.pycqa.org/en/latest/user/configuration.html).

You can ignore rules via
- file `setup.cfg`: parameter `ignore`
```editorconfig
[flake8]
ignore = OCS101
```
- comment in code `#noqa: OCS101`

```

## Rules

### Scenario Rules
1. [OCS101. Decorator @vedro.params should not be presented](./custom_otello_linter/rules/OCS101.md)

###  Scenario Steps Rules
1. [OCS300. Function make_screenshot used once](./custom_otello_linter/rules/OCS300.md)