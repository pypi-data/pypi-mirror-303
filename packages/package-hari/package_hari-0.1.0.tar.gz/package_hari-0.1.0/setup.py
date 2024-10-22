# setup.py

from setuptools import setup, find_packages

setup(
    name='package_hari',            # The package name
    version='0.1.0',                   # Initial release version
    author='Hari kowshik',
    author_email='harikowshik.molugu@drishyta.ai',
    description='for testing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),  # Automatically finds all packages in the folder
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

