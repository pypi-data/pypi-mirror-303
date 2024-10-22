
from setuptools import setup, find_packages

setup(
    name='async_elastic_logger',
    version='0.4.2',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'pydantic-settings',
        'elasticsearch[async]'
    ],
    author='Nima Miri',
    author_email='nimamiri9248@gmail.com',
    description='A custom asynchronous logging library with Elasticsearch integration.',
    url='https://github.com/nimamiri9248/async_elastic_logger',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging'
    ],
)