from setuptools import setup, find_packages

setup(
    name='caseChange',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi>=0.68.0',
        'uvicorn>=0.15.0',
    ],
    python_requires='>=3.6',
)