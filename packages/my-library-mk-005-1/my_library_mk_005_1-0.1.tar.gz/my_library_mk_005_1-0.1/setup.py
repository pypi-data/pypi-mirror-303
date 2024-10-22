from setuptools import setup, find_packages

setup(
    name='my-library-mk-005_1',
    version='0.1',
    description='A Python library',
    author='Mushaim Khan',
    author_email='mushaimk01@gmail.com',
    packages=find_packages(),  # Automatically find packages
    include_package_data=True,  # Include package data files
    package_data={
        'my_library_mk_005_1': ['input.py'],  # Include input.py
    },
)
