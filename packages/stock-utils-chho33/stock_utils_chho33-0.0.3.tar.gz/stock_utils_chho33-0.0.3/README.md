## Packaging
Please refer to:
- https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#package-discovery
- https://packaging.python.org/en/latest/tutorials/packaging-projects/#

## Upload
python3 -m build
edit version in pyproject.toml
python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload dist/*
