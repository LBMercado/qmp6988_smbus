from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='piqmp6988_abst',
    version='1.1.0',
    author='Akihisa ONODA, Luis Mercado',
    author_email='akihisa.onoda@osarusystem.com, luisbzmercado1776@gmail.com',
    description='QMP6988 with abstracted i2c interface, smbus-capable',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LBMercado/qmp6988_smbus',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
    ],
    package_dir={"": "src"},
    packages=['piqmp6988'],
    install_requires=['pigpio', 'smbus-cffi'],
    license='MIT',
    keywords='piqmp6988 qmp6988 env3hat pigpio temperature pressure sensor i2c smbus',
    
)
