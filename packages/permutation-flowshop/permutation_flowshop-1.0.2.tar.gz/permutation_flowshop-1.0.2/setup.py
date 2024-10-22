from setuptools import setup

with open("README.md", "r") as file:
    read_me = file.read()

setup(
    name='permutation-flowshop',
    version='1.0.2',
    author='Bruno, Raphael',
    packages=['pfsp'],
    long_description=read_me,
    long_description_content_type="text/markdown",
    author_email='bruno.development3@gmail.com',
    keywords='permutation flowshop',
    description=u'Package to facilitate studies about Permutation Flow Shop Scheduling Problem (PFSP)',
    classifiers=[
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',],
    python_requires='>=3.10',
    install_requires=['numpy', 'plotly'],
)
