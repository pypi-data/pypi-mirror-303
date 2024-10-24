from setuptools import setup

name = 'crealand'
version = '1.0.5'
description = 'Python SDK for Crealand'
author = 'UBTECH Robotics'
author_email = 'swenggroup@ubtrobot.com'

packages = [
    'crealand'
]

package_dir = {
    'crealand': 'crealand'
}

package_data = {
}

install_requires = [
    'websockets'
]

# require_data_files = ['requirements.txt']
require_data_files = []
example_data_files = [
]
doc_data_files = [
]

data_files = []
try:
    data_files.extend(require_data_files)
    data_files.extend(example_data_files)
    data_files.extend(doc_data_files)
except:
    pass

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    data_files=data_files,
    install_requires=install_requires
)
