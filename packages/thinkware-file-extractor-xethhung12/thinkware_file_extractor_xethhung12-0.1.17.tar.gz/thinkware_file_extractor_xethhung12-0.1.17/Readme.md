# Dev

build
```shell
rm -fr dist && python -m build
```

deploy
```shell
python -m twine upload dist/*
```