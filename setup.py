from setuptools import setup, find_packages

setup(
    name="uxtbpy",
    version="0.1",
    url="https://github.com/hkneiding/uxtbpy",
    author="Hannes Kneiding",
    author_email="hannes.kneiding@outlook.com",
    packages=find_packages(exclude=["test"]),
)
