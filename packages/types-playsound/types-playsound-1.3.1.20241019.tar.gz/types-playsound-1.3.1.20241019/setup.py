from setuptools import setup

name = "types-playsound"
description = "Typing stubs for playsound"
long_description = '''
## Typing stubs for playsound

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`playsound`](https://github.com/TaylorSMarks/playsound) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `playsound`. This version of
`types-playsound` aims to provide accurate annotations for
`playsound==1.3.*`.

*Note:* `types-playsound` is unmaintained and won't be updated.


This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/playsound`](https://github.com/python/typeshed/tree/main/stubs/playsound)
directory.

This package was tested with
mypy 1.11.2,
pyright 1.1.385,
and pytype 2024.10.11.
It was generated from typeshed commit
[`890a38f424831978469d9bbbe3b570607b122bfb`](https://github.com/python/typeshed/commit/890a38f424831978469d9bbbe3b570607b122bfb).
'''.lstrip()

setup(name=name,
      version="1.3.1.20241019",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/playsound.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['playsound-stubs'],
      package_data={'playsound-stubs': ['__init__.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
