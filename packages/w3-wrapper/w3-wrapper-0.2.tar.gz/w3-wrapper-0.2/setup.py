from setuptools import setup, find_packages

setup(
    name='w3-wrapper',
    version='0.2',
    description='an object-oriented wrapper over the web3py library',
    author='ilyx',
    author_email='felinooper@gmail.com',
    url='',
    packages=find_packages(),
    install_requires=[
        'web3',
        'asyncio',
        'hexbytes',
        'pydantic',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
