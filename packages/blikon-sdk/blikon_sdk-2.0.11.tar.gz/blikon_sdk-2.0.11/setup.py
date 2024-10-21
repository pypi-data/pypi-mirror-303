from setuptools import setup, find_packages

setup(
    name="blikon_sdk",
    version="2.0.11",
    packages=find_packages(include=["blikon_sdk", "blikon_sdk.*"]),
    install_requires=[
        "fastapi",
        "pydantic-settings",
        "uvicorn",
        "python-jose",
        "httpx",
        "opencensus-ext-azure",
        "setuptools",
        "googletrans==4.0.0-rc1",
    ],
    description="Blikon SDK for security and middleware services",
    author="Raúl Díaz Peña",
    author_email="rdiaz@yosoyblueicon.com",
    license="BlikonⓇ",
    url="https://github.com/blikon/blikon_sdk",
)
