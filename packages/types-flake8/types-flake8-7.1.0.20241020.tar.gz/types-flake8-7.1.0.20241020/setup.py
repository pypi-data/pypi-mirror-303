from setuptools import setup

name = "types-flake8"
description = "Typing stubs for flake8"
long_description = '''
## Typing stubs for flake8

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`flake8`](https://github.com/pycqa/flake8) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `flake8`. This version of
`types-flake8` aims to provide accurate annotations for
`flake8==7.1.*`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/flake8`](https://github.com/python/typeshed/tree/main/stubs/flake8)
directory.

This package was tested with
mypy 1.12.0,
pyright 1.1.385,
and pytype 2024.10.11.
It was generated from typeshed commit
[`b0d57cc03c83e6e75a7b9cf13fb89b06c5fa039f`](https://github.com/python/typeshed/commit/b0d57cc03c83e6e75a7b9cf13fb89b06c5fa039f).
'''.lstrip()

setup(name=name,
      version="7.1.0.20241020",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/flake8.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-pyflakes'],
      packages=['flake8-stubs'],
      package_data={'flake8-stubs': ['__init__.pyi', '_compat.pyi', 'api/__init__.pyi', 'api/legacy.pyi', 'checker.pyi', 'defaults.pyi', 'discover_files.pyi', 'exceptions.pyi', 'formatting/__init__.pyi', 'formatting/_windows_color.pyi', 'formatting/base.pyi', 'formatting/default.pyi', 'main/__init__.pyi', 'main/application.pyi', 'main/cli.pyi', 'main/debug.pyi', 'main/options.pyi', 'options/__init__.pyi', 'options/aggregator.pyi', 'options/config.pyi', 'options/manager.pyi', 'options/parse_args.pyi', 'plugins/__init__.pyi', 'plugins/finder.pyi', 'plugins/pycodestyle.pyi', 'plugins/pyflakes.pyi', 'plugins/reporter.pyi', 'processor.pyi', 'statistics.pyi', 'style_guide.pyi', 'utils.pyi', 'violation.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
