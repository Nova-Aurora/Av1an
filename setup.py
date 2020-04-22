import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Av1an", # Replace with your own username
    version="1.7.0",
    author="Master_Of_Zen",
    author_email="master_of_zen@protonmail.com",
    description="All-in-one encode toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/master-of-zen/Av1an",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)