from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "A package containing essential and necessary things for Data Structures and Algorithms"
LONG_DESCRIPTION = ""

setup(
    name="dsa_pack",
    version=VERSION,
    author="Bobur Yusupov",
    author_email="bobur.yu06@mail.ru",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_required=[],

    keywords=['stack', 'queue', 'data structures', 'algorithms'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)