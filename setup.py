import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="npwPy",
    version="0.0.1",
    author="Fajrin Imam Arif",
    author_email="fajrinimamarif@gmail.com",
    description="this package for checking NPWP number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sendaljpt/npwPy",
    packages=['npwPy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)