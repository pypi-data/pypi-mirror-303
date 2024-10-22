# DaoAI Inference Client for Python

## Build package
```shell
python -m build
```
This command will output a folder named `dist/`.

## Publish package
To TestPyPI (PyPI test environment):
```shell
python -m twine upload --verbose --repository testpypi dist/*
```
To PyPI (production environment):
```shell
python -m twine upload --verbose dist/*
```
