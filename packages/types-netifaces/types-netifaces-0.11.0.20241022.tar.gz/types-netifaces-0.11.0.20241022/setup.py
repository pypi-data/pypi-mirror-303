from setuptools import setup

name = "types-netifaces"
description = "Typing stubs for netifaces"
long_description = '''
## Typing stubs for netifaces

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`netifaces`](https://github.com/al45tair/netifaces) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `netifaces`. This version of
`types-netifaces` aims to provide accurate annotations for
`netifaces==0.11.*`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/netifaces`](https://github.com/python/typeshed/tree/main/stubs/netifaces)
directory.

This package was tested with
mypy 1.12.0,
pyright 1.1.385,
and pytype 2024.10.11.
It was generated from typeshed commit
[`e8c2e5bb20ab0e64287b92fb6e77e579d0ba8da0`](https://github.com/python/typeshed/commit/e8c2e5bb20ab0e64287b92fb6e77e579d0ba8da0).
'''.lstrip()

setup(name=name,
      version="0.11.0.20241022",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/netifaces.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['netifaces-stubs'],
      package_data={'netifaces-stubs': ['__init__.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
