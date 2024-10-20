from setuptools import setup, find_packages

setup(
    name='finance-calculator-sk1',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'finance-calculator=finance_calculator_sk1.__main__:main',
        ],
    },
    description='A package for calculating net profit and ROI.',
    author='Stanislav Kuleshov',
    author_email='phtschmth171@gmail.com',
)