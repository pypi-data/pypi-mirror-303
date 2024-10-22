from setuptools import setup, find_packages

setup(
    name='PanoFF_Excel',
    version='0.1',
    description='Python library for automatic creation of a table for 22 exam assignments',
    author='S4CBS',
    author_email='aap200789@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
        'xlrd',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
