from setuptools import setup, find_packages

setup(
    name="sonal-fastapi",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi"
        "uvicorn"
    ],
    python_requires=">=3.6",
)