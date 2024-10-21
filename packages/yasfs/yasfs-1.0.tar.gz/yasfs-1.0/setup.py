import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='yasfs',
    version='1.0',
    author="ashaider",
    author_email="ahmedsyedh1+gh@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    description="Python-based command-line tool that organizes and sorts files by their extension types",
    long_description=README,
    long_description_content_type="text/MARKDOWN",
    url="https://github.com/ashaider/yet-another-simple-file-sorter/",
    entry_points={
        'console_scripts': [
            'yasfs=yasfs.__main__:main',
        ],
    },
    license="MIT",
    python_requires='>=3.8',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
