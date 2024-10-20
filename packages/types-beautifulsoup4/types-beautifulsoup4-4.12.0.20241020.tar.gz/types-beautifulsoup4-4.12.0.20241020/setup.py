from setuptools import setup

name = "types-beautifulsoup4"
description = "Typing stubs for beautifulsoup4"
long_description = '''
## Typing stubs for beautifulsoup4

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`beautifulsoup4`](https://git.launchpad.net/beautifulsoup/tree) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `beautifulsoup4`. This version of
`types-beautifulsoup4` aims to provide accurate annotations for
`beautifulsoup4==4.12.*`.

This stub package is marked as [partial](https://peps.python.org/pep-0561/#partial-stub-packages).
If you find that annotations are missing, feel free to contribute and help complete them.


This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/beautifulsoup4`](https://github.com/python/typeshed/tree/main/stubs/beautifulsoup4)
directory.

This package was tested with
mypy 1.12.0,
pyright 1.1.385,
and pytype 2024.10.11.
It was generated from typeshed commit
[`b0d57cc03c83e6e75a7b9cf13fb89b06c5fa039f`](https://github.com/python/typeshed/commit/b0d57cc03c83e6e75a7b9cf13fb89b06c5fa039f).
'''.lstrip()

setup(name=name,
      version="4.12.0.20241020",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/beautifulsoup4.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-html5lib'],
      packages=['bs4-stubs'],
      package_data={'bs4-stubs': ['__init__.pyi', 'builder/__init__.pyi', 'builder/_html5lib.pyi', 'builder/_htmlparser.pyi', 'builder/_lxml.pyi', 'dammit.pyi', 'diagnose.pyi', 'element.pyi', 'formatter.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
