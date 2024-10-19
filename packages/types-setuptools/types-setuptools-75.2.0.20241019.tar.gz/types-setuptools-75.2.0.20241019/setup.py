from setuptools import setup

name = "types-setuptools"
description = "Typing stubs for setuptools"
long_description = '''
## Typing stubs for setuptools

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`setuptools`](https://github.com/pypa/setuptools) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`setuptools`.

This version of `types-setuptools` aims to provide accurate annotations
for `setuptools==75.2.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/setuptools. All fixes for
types and metadata should be contributed there.

If using `setuptools >= 71.1` *only* for `pkg_resources`,
you don't need `types-setuptools` since `pkg_resources` is now typed.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit
[`b2f68ec2feff500ea9e8983396cead54218bb99c`](https://github.com/python/typeshed/commit/b2f68ec2feff500ea9e8983396cead54218bb99c) and was tested
with mypy 1.11.2, pyright 1.1.385, and
pytype 2024.10.11.
'''.lstrip()

setup(name=name,
      version="75.2.0.20241019",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/setuptools.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['distutils-stubs', 'setuptools-stubs', 'pkg_resources-stubs'],
      package_data={'distutils-stubs': ['_modified.pyi', 'archive_util.pyi', 'ccompiler.pyi', 'cmd.pyi', 'command/__init__.pyi', 'command/bdist.pyi', 'command/bdist_rpm.pyi', 'command/build.pyi', 'command/build_clib.pyi', 'command/build_ext.pyi', 'command/build_py.pyi', 'command/install.pyi', 'command/install_lib.pyi', 'command/install_scripts.pyi', 'command/sdist.pyi', 'compat/__init__.pyi', 'dep_util.pyi', 'dist.pyi', 'errors.pyi', 'extension.pyi', 'filelist.pyi', 'sysconfig.pyi', 'util.pyi', 'METADATA.toml', 'compat/py.typed', 'command/py.typed'], 'setuptools-stubs': ['__init__.pyi', '_distutils/_modified.pyi', '_distutils/archive_util.pyi', '_distutils/ccompiler.pyi', '_distutils/cmd.pyi', '_distutils/command/__init__.pyi', '_distutils/command/bdist.pyi', '_distutils/command/bdist_rpm.pyi', '_distutils/command/build.pyi', '_distutils/command/build_clib.pyi', '_distutils/command/build_ext.pyi', '_distutils/command/build_py.pyi', '_distutils/command/install.pyi', '_distutils/command/install_lib.pyi', '_distutils/command/install_scripts.pyi', '_distutils/command/sdist.pyi', '_distutils/compat/__init__.pyi', '_distutils/dep_util.pyi', '_distutils/dist.pyi', '_distutils/errors.pyi', '_distutils/extension.pyi', '_distutils/filelist.pyi', '_distutils/sysconfig.pyi', '_distutils/util.pyi', 'archive_util.pyi', 'build_meta.pyi', 'command/__init__.pyi', 'command/alias.pyi', 'command/bdist_egg.pyi', 'command/bdist_rpm.pyi', 'command/bdist_wheel.pyi', 'command/build.pyi', 'command/build_clib.pyi', 'command/build_ext.pyi', 'command/build_py.pyi', 'command/develop.pyi', 'command/dist_info.pyi', 'command/easy_install.pyi', 'command/editable_wheel.pyi', 'command/egg_info.pyi', 'command/install.pyi', 'command/install_egg_info.pyi', 'command/install_lib.pyi', 'command/install_scripts.pyi', 'command/rotate.pyi', 'command/saveopts.pyi', 'command/sdist.pyi', 'command/setopt.pyi', 'command/test.pyi', 'compat/__init__.pyi', 'compat/py310.pyi', 'compat/py311.pyi', 'compat/py312.pyi', 'compat/py39.pyi', 'config/__init__.pyi', 'config/expand.pyi', 'config/pyprojecttoml.pyi', 'config/setupcfg.pyi', 'depends.pyi', 'discovery.pyi', 'dist.pyi', 'errors.pyi', 'extension.pyi', 'glob.pyi', 'installer.pyi', 'launch.pyi', 'logging.pyi', 'modified.pyi', 'monkey.pyi', 'msvc.pyi', 'namespaces.pyi', 'package_index.pyi', 'sandbox.pyi', 'unicode_utils.pyi', 'version.pyi', 'warnings.pyi', 'wheel.pyi', 'windows_support.pyi', 'METADATA.toml', 'py.typed'], 'pkg_resources-stubs': ['__init__.pyi', '_vendored_packaging/__init__.pyi', '_vendored_packaging/markers.pyi', '_vendored_packaging/requirements.pyi', '_vendored_packaging/specifiers.pyi', '_vendored_packaging/version.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
