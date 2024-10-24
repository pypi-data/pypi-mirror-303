# Crealand SDK
Crealand SDK

## Requirements
- setuptools
- wheel
- twine
## build

需要先pip安装setuptools和wheel再编译打包：
```
python3 setup.py sdist --formats=gztar
python3 setup.py bdist_wheel
```

## Install

```bash
pip install crealand
```

## Uninstall

```bash
pip uninstall crealand
```

## Publish
### 前置条件
- 把根目录的`.pypirc`文件拷贝到系统用户根目录；
- 安装`twine`
### 发布测试环境
> https://test.pypi.org/
```bash
python3 -m twine upload --repository testpypi dist/*
```

### 发布正式环境
> https://pypi.org/
```bash
python3 -m twine upload --repository pypi dist/*
```