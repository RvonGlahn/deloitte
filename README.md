# Installation

![tests](https://github.com/RvonGlahn/CPP-BattleSnake/actions/workflows/pytest.yml/badge.svg)

Create conda env:

``` Bash
conda create -n deloitte python=3.9
conda activate deloitte
cd deloitte
```

Install all dependencies (tests included)

``` Bash
pip install .
```

## Test Code

Run all tests with pytest and see coverage.
Tests are run per default on every commit.

``` Bash
pytest --cov
```
