# minrecord

<p align="center">
    <a href="https://github.com/durandtibo/minrecord/actions">
        <img alt="CI" src="https://github.com/durandtibo/minrecord/workflows/CI/badge.svg">
    </a>
    <a href="https://github.com/durandtibo/minrecord/actions">
        <img alt="Nightly Tests" src="https://github.com/durandtibo/minrecord/workflows/Nightly%20Tests/badge.svg">
    </a>
    <a href="https://github.com/durandtibo/minrecord/actions">
        <img alt="Nightly Package Tests" src="https://github.com/durandtibo/minrecord/workflows/Nightly%20Package%20Tests/badge.svg">
    </a>
    <br/>
    <a href="https://durandtibo.github.io/minrecord/">
        <img alt="Documentation" src="https://github.com/durandtibo/minrecord/workflows/Documentation%20(stable)/badge.svg">
    </a>
    <a href="https://durandtibo.github.io/minrecord/">
        <img alt="Documentation" src="https://github.com/durandtibo/minrecord/workflows/Documentation%20(unstable)/badge.svg">
    </a>
    <br/>
    <a href="https://codecov.io/gh/durandtibo/minrecord">
        <img alt="Codecov" src="https://codecov.io/gh/durandtibo/minrecord/branch/main/graph/badge.svg">
    </a>
    <a href="https://codeclimate.com/github/durandtibo/minrecord/maintainability">
        <img src="https://api.codeclimate.com/v1/badges/d6e3047eedfd2e1e0d86/maintainability" />
    </a>
    <a href="https://codeclimate.com/github/durandtibo/minrecord/test_coverage">
        <img src="https://api.codeclimate.com/v1/badges/d6e3047eedfd2e1e0d86/test_coverage" />
    </a>
    <br/>
    <a href="https://github.com/psf/black">
        <img  alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
    <a href="https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings">
        <img  alt="Doc style: google" src="https://img.shields.io/badge/%20style-google-3666d6.svg">
    </a>
    <a href="https://github.com/astral-sh/ruff">
        <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;">
    </a>
    <a href="https://github.com/guilatrova/tryceratops">
        <img  alt="Doc style: google" src="https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black">
    </a>
    <br/>
    <a href="https://pypi.org/project/minrecord/">
        <img alt="PYPI version" src="https://img.shields.io/pypi/v/minrecord">
    </a>
    <a href="https://pypi.org/project/minrecord/">
        <img alt="Python" src="https://img.shields.io/pypi/pyversions/minrecord.svg">
    </a>
    <a href="https://opensource.org/licenses/BSD-3-Clause">
        <img alt="BSD-3-Clause" src="https://img.shields.io/pypi/l/minrecord">
    </a>
    <br/>
    <a href="https://pepy.tech/project/minrecord">
        <img  alt="Downloads" src="https://static.pepy.tech/badge/minrecord">
    </a>
    <a href="https://pepy.tech/project/minrecord">
        <img  alt="Monthly downloads" src="https://static.pepy.tech/badge/minrecord/month">
    </a>
    <br/>
</p>

## Overview

`minrecord` is a minimalist Python library to record values in a ML workflow.
In particular, it provides functionalities to track the best value, or the most recent values by
storing a limiting number of values.
It is possible to customize the library e.g. it is possible to define a new logic to track the best
value.
Below is an example to show how to track the best scalar value when the best value is the maximum
value and when the best value is the minimum value.

```pycon

>>> from minrecord import MaxScalarRecord, MinScalarRecord
>>> record_max = MaxScalarRecord("accuracy")
>>> record_max.update([(0, 42), (None, 45), (2, 46)])
>>> record_max.add_value(40)
>>> record_max.get_best_value()
46
>>> record_min = MinScalarRecord("loss")
>>> record_min.update([(0, 42), (None, 45), (2, 46)])
>>> record_min.add_value(50)
>>> record_min.get_best_value()
42

```

## Documentation

- [latest (stable)](https://durandtibo.github.io/minrecord/): documentation from the latest stable
  release.
- [main (unstable)](https://durandtibo.github.io/minrecord/main/): documentation associated to the
  main branch of the repo. This documentation may contain a lot of work-in-progress/outdated/missing
  parts.

## Installation

We highly recommend installing
a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
`minrecord` can be installed from pip using the following command:

```shell
pip install minrecord
```

To make the package as slim as possible, only the minimal packages required to use `minrecord` are
installed.
To include all the dependencies, you can use the following command:

```shell
pip install minrecord[all]
```

Please check the [get started page](https://durandtibo.github.io/minrecord/get_started) to see how
to
install only some specific dependencies or other alternatives to install the library.
The following is the corresponding `minrecord` versions and tested dependencies.

| `minrecord` | `coola`        | `objectory`              | `python`      |
|-------------|----------------|--------------------------|---------------|
| `main`      | `>=0.8.4,<1.0` | `>=0.2,<1.0`<sup>*</sup> | `>=3.9,<3.14` |
| `0.1.0`     | `>=0.8.4,<1.0` | `>=0.2,<1.0`<sup>*</sup> | `>=3.9,<3.14` |
| `0.0.2`     | `>=0.7.2,<1.0` | `>=0.1,<1.0`<sup>*</sup> | `>=3.9,<3.13` |
| `0.0.1`     | `>=0.7,<1.0`   | `>=0.1,<1.0`             | `>=3.9,<3.13` |

<sup>*</sup> indicates an optional dependency

## Contributing

Please check the instructions in [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Suggestions and Communication

Everyone is welcome to contribute to the community.
If you have any questions or suggestions, you can
submit [Github Issues](https://github.com/durandtibo/minrecord/issues).
We will reply to you as soon as possible. Thank you very much.

## API stability

:warning: While `minrecord` is in development stage, no API is guaranteed to be stable from one
release to the next.
In fact, it is very likely that the API will change multiple times before a stable 1.0.0 release.
In practice, this means that upgrading `minrecord` to a new version will possibly break any code
that
was using the old version of `minrecord`.

## License

`minrecord` is licensed under BSD 3-Clause "New" or "Revised" license available
in [LICENSE](LICENSE)
file.
