import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsfunctions", # Replace with your own username
    version="0.0.0-dev",
    author="Vivian Nguyen",
    author_email="nguy.vivian.vi@gmail.com",
    description="Collection of Often Used Data Science Functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="nothing_yet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
