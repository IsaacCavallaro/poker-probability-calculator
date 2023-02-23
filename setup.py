from setuptools import setup, find_packages

setup(
    name='poker_probability_calculator',
    version='0.1.0',
    description='A package for calculating probabilities in a game of poker',
    author='Isaac Cavallaro',
    author_email='isaaccavallaro@gmail.com',
    url='https://github.com/yourusername/poker_probability_calculator',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    tests_require=[
        'pytest',
    ],
)
