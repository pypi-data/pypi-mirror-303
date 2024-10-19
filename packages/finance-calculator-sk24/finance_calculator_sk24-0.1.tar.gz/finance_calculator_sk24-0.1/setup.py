from setuptools import setup, find_packages

setup(
    name='finance_calculator_sk24',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'finance-calculator=finance_calculator.calculator:main',
        ],
    },
    install_requires=[],
    description='A package for calculating net profit and ROI.',
    author='Stanislav Kuleshov',
    author_email='phtschmth171@gmail.com',
)