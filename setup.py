from setuptools import setup, find_packages

setup(
    name="uxtbpy",
    version="1.0",
    description="Python interface for executing and parsing results from xTB and sTDA calculations.",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    url="https://github.com/hkneiding/uxtbpy",
    author="Hannes Kneiding",
    author_email="hannes.kneiding@outlook.com",
    license="MIT",
    python_requires=">=3.x",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["test"]),
)
