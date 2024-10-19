from setuptools import setup, find_packages

setup(
    name="byte_codec",
    version="0.1.3",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.7",
    author="Muhammad Daffa",
    author_email="mdaffa2301@gmail.com",
    description="A simple Python library for encoding and decoding bytes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords=["bytes", "encoding", "decoding"],
)
