import setuptools

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()
setuptools.setup(
    name='MBQQ',
    version='0.8.7',
    url='https://pypi.org/manage/account/token/',
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    license='',
    author='Magpie Bridge',
    author_email='',
    description='',
    install_requires=[
        'MDQTools',
        'protobuf==4.23.4',
        'pydantic==2.1.1',
        'cryptography',
        'bs4',
        'urllib3==1.26.16',
        'pydantic',
        'requests',
        'python-box',
        'PySocks',
        'python-box',
        'loguru'

    ]

)
