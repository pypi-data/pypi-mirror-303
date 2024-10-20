import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fletmd",
    version="1.0.1",
    author="Alexander White",
    author_email="pip@mail83.ru",
    description="Visual editor using flet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/white124bk/fletmd",
    packages=setuptools.find_packages(),
    install_requires=[
        'flet',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)