from setuptools import setup

name = "types-icalendar"
description = "Typing stubs for icalendar"
long_description = '''
## Typing stubs for icalendar

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`icalendar`](https://github.com/collective/icalendar) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `icalendar`. This version of
`types-icalendar` aims to provide accurate annotations for
`icalendar~=6.0.1`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/icalendar`](https://github.com/python/typeshed/tree/main/stubs/icalendar)
directory.

This package was tested with
mypy 1.12.0,
pyright 1.1.385,
and pytype 2024.10.11.
It was generated from typeshed commit
[`e8c2e5bb20ab0e64287b92fb6e77e579d0ba8da0`](https://github.com/python/typeshed/commit/e8c2e5bb20ab0e64287b92fb6e77e579d0ba8da0).
'''.lstrip()

setup(name=name,
      version="6.0.1.20241022",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/icalendar.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-python-dateutil', 'backports.zoneinfo; python_version < "3.9"'],
      packages=['icalendar-stubs'],
      package_data={'icalendar-stubs': ['__init__.pyi', 'cal.pyi', 'caselessdict.pyi', 'parser.pyi', 'parser_tools.pyi', 'prop.pyi', 'timezone/__init__.pyi', 'timezone/provider.pyi', 'timezone/pytz.pyi', 'timezone/tzp.pyi', 'timezone/windows_to_olson.pyi', 'timezone/zoneinfo.pyi', 'tools.pyi', 'version.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
