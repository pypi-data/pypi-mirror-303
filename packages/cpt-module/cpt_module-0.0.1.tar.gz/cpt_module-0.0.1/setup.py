from setuptools import setup, find_packages
import os

# Path to the .so file inside the package
lib_path = os.path.join('cpt_module', 'libcpt_module.so')

setup(
    name='cpt_module',
    version='0.0.1',
    description='A Python module wrapping a Rust shared library for encryption and decryption - CPT',
    packages=find_packages(),
    package_data={'cpt_module': ['libcpt_module.so']},  # Include the .so file
    include_package_data=True,
)
