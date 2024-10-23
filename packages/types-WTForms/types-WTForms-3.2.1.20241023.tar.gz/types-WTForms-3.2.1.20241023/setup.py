from setuptools import setup

name = "types-WTForms"
description = "Typing stubs for WTForms"
long_description = '''
## Typing stubs for WTForms

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`WTForms`](https://github.com/pallets-eco/wtforms) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `WTForms`. This version of
`types-WTForms` aims to provide accurate annotations for
`WTForms~=3.2.1`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/WTForms`](https://github.com/python/typeshed/tree/main/stubs/WTForms)
directory.

This package was tested with
mypy 1.12.0,
pyright 1.1.385,
and pytype 2024.10.11.
It was generated from typeshed commit
[`ca65e087f1f9dfc28e89192b60ce7cfc2e92c674`](https://github.com/python/typeshed/commit/ca65e087f1f9dfc28e89192b60ce7cfc2e92c674).
'''.lstrip()

setup(name=name,
      version="3.2.1.20241023",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/WTForms.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['MarkupSafe'],
      packages=['wtforms-stubs'],
      package_data={'wtforms-stubs': ['__init__.pyi', 'csrf/__init__.pyi', 'csrf/core.pyi', 'csrf/session.pyi', 'fields/__init__.pyi', 'fields/choices.pyi', 'fields/core.pyi', 'fields/datetime.pyi', 'fields/form.pyi', 'fields/list.pyi', 'fields/numeric.pyi', 'fields/simple.pyi', 'form.pyi', 'i18n.pyi', 'meta.pyi', 'utils.pyi', 'validators.pyi', 'widgets/__init__.pyi', 'widgets/core.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
