from setuptools import setup, find_packages

setup(
    name='letme',
    version='1.0',
    author='hamodirtyeza',
    author_email='hamodirtyeza97@gmail.com',
    description='A package to simplify working with Delta Lake and Spark-SQL',
    packages=find_packages(include=['letme',], exclude=[]),
    python_requires='>=3.12',
)