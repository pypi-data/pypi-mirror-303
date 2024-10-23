from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='PanoFF_Excel',
    version='0.2.5',
    description='Егэ 22 задание. Авто заполнение таблицы. Шаблонный алгоритм.',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
