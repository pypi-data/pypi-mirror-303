from setuptools import setup, find_packages
import os

lib_path = os.path.join('cpt_module', 'libcpt_module.so')

setup(
    name='cpt_module',
    version='1.0.2',
    description='A Python module wrapping a Rust shared library for encryption and decryption - CPT',
    packages=find_packages(),
    package_data={'cpt_module': ['libcpt_module.so']},
    include_package_data=True,
)
